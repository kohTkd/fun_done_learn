from abc import ABCMeta, abstractmethod
import functools
import os

import boto3
from botocore.exceptions import ClientError

from app.errors.invalid_entity_error import InvalidEntityError
from app.errors.not_found_error import NotFoundError


def table_name(name):
    return __add_attr('table_name', name)
    # def decoratee(klass):
    #     setattr(klass, 'table_name', name)
    #     return klass
    # return decoratee


def hash_key(name):
    return __add_attr('hash_key', name)
    # def decoratee(klass):
    #     setattr(klass, 'hash_key', name)
    #     return klass
    # return decoratee


def range_key(name):
    return __add_attr('range_key', name)
    # def decoratee(klass):
    #     setattr(klass, 'range_key', name)
    #     return klass
    # return decoratee


def entity_repository(name):
    return __add_attr('entity_class', name)
    # def decoratee(klass):
    #     setattr(klass, 'entity_class', name)
    #     return klass
    # return decoratee


def __add_attr(attr_name, value):
    def decoratee(klass):
        setattr(klass, attr_name, value)
        return klass
    return decoratee


def set_timestamp(func):
    @functools.wraps(func)
    def wrapper(self, entity):
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
        item = self._to_save_format(entity)
        self._table().put_item(Item=item)
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
        return [self._build_entity(item) for item in self._scan(**kwargs)]

    def _scan(self, **kwargs) -> list:
        response = self._table().scan(**kwargs)
        items = [item for item in response['Items']]
        if 'LastEvaluatedKey' not in response:
            return items
        return items + self._scan(**dict(kwargs, ExclusiveStartKey=response['LastEvaluatedKey']))

    def _build_entity(self, item):
        return self.entity_class(**dict(item, persisted=True))

    @abstractmethod
    def _to_save_format(self, record):
        raise NotImplementedError()

    def _table(self):
        return self.dynamodb.Table(self.table_name)
