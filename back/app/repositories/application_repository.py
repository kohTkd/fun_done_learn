from abc import ABCMeta, abstractmethod
import logging
import os

import boto3
from botocore.exceptions import ClientError

from app.errors.invalid_entity_error import InvalidEntityError


def table_name(name):
    def decoratee(klass):
        setattr(klass, 'table_name', name)
        return klass
    return decoratee


def hash_key(name):
    def decoratee(klass):
        setattr(klass, 'hash_key', name)
        return klass
    return decoratee


def entity_repository(entity_class):
    def decoratee(klass):
        setattr(klass, 'entity_class', entity_class)
        return klass
    return decoratee


def require_validation(func):
    def wrapper(self, entity):
        valid = all(e.is_valid() for e in entity) if isinstance(entity, list) else entity.is_valid()
        if not valid:
            raise InvalidEntityError(entity)
        return func(self, entity)
    return wrapper


class ApplicationRepository(metaclass=ABCMeta):
    def __init__(self):
        endpoint = os.environ['DYNAMODB_ENDPOINT']
        region_name = os.environ['DYNAMODB_REGION']
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint, region_name=region_name)

    @require_validation
    def save(self, entity):
        item = self._to_save_format(entity)
        self._table().put_item(Item=item)
        return entity.persist()

    def find(self, value):
        condition = {}
        condition[self.hash_key] = value
        try:
            response = self._table().get_item(Key=condition)
        except ClientError as e:
            logging.error(e.response['Error']['Message'])
            return None
        else:
            return self.entity_class(**response.get('Item'))

    def scan(self, **kwargs):
        return [item for item in self._scan(**kwargs)]

    def _scan(self, **kwargs) -> list:
        response = self._table().scan(**kwargs)
        items = [item for item in response['Items']]
        if 'LastEvaluatedKey' not in response:
            return items
        return items + self._scan(**dict(kwargs, ExclusiveStartKey=response['LastEvaluatedKey']))

    @abstractmethod
    def _to_save_format(self, record):
        raise NotImplementedError()

    def _table(self):
        return self.dynamodb.Table(self.table_name)
