from abc import ABCMeta, abstractmethod
import functools
import os

import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

from app.errors.invalid_entity_error import InvalidEntityError
from app.errors.not_found_error import NotFoundError


def table_name(name):
    return __add_attr('table_name', name)


def hash_key(name):
    return __add_attr('hash_key', name)


def range_key(name):
    return __add_attr('range_key', name)


def entity_repository(name):
    return __add_attr('entity_class', name)


def __add_attr(attr_name, value):
    def decoratee(klass):
        setattr(klass, attr_name, value)
        return klass
    return decoratee


def set_timestamp(func):
    @functools.wraps(func)
    def wrapper(self, entity):
        if isinstance(entity, list):
            for e in entity:
                e.set_time_stamp()
        else:
            entity.set_time_stamp()
        return func(self, entity)
    return wrapper


def require_validation(func):
    @functools.wraps(func)
    def wrapper(self, entity):
        valid = all(e.is_valid() for e in entity) if isinstance(entity, list) else entity.is_valid()
        if not valid:
            raise InvalidEntityError(entity)
        return func(self, entity)
    return wrapper


class ApplicationRepository(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        endpoint = kwargs.get('endpoint') or os.environ['DYNAMODB_ENDPOINT']
        region_name = kwargs.get('region_name') or os.environ['DYNAMODB_REGION']
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint, region_name=region_name)

    @set_timestamp
    @require_validation
    def save(self, entity):
        if isinstance(entity, list):
            return self._save_entities(entity)
        self._table().put_item(Item=self._to_save_format(entity))
        return entity.persist()

    def find(self, hash_key, range_key=None):
        condition = {}
        condition[self.hash_key] = hash_key
        if range_key:
            condition[self.range_key] = range_key
        try:
            response = self._table().get_item(Key=condition)
            item = response.get('Item')
            if not item:
                raise NotFoundError(self.entity_class)
            return self._build_entity(item)
        except ClientError:
            return None

    def scan(self, **kwargs):
        return self._build_entities(self._scan(**kwargs))

    def query(self, key_value):
        return self._build_entities(self._query(key_value))

    def delete(self, hash_key, range_key=None):
        condition = {}
        condition[self.hash_key] = hash_key
        if range_key:
            condition[self.range_key] = range_key
        self._table().delete_item(Key=condition)

    def _scan(self, **kwargs) -> list:
        response = self._table().scan(**kwargs)
        items = [item for item in response['Items']]
        if 'LastEvaluatedKey' not in response:
            return items
        return items + self._scan(**dict(kwargs, ExclusiveStartKey=response['LastEvaluatedKey']))

    def _query(self, key_value):
        response = self._table().query(KeyConditionExpression=Key(self.hash_key).eq(key_value))
        return response['Items']

    def _build_entity(self, item):
        return self.entity_class(**dict(item, persisted=True))

    def _build_entities(self, items):
        return [self._build_entity(item) for item in items]

    def _save_entities(self, entities):
        with self._table().batch_writer() as batch:
            for entity in entities:
                batch.put_item(Item=self._to_save_format(entity))

        return all([entity.persist() for entity in entities])

    @abstractmethod
    def _to_save_format(self, record):
        raise NotImplementedError()

    def _table(self):
        return self.dynamodb.Table(self.table_name)
