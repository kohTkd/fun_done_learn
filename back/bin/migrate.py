import boto3
import json
import os
import sys


class DynamoDbMigrator():
    def __init__(self, region=None, logging=None):
        self.__logging = logging
        self.region = region if region else os.environ['DYNAMODB_REGION']
        self._dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=os.environ['DYNAMODB_ENDPOINT'],
            region_name=self.region)
        self._table_names = [t.table_name for t in self._dynamodb.tables.all()]
        self._dir = f"{os.path.dirname(__file__)}/../config/dynamodb/tables"

    def set_test_region(self):
        os.environ['DYNAMODB_REGION'] = self.region

    def truncate_all(self):
        self._execute_all_file(self.truncate)

    def migrate_all(self):
        self._execute_all_file(self.migrate)

    def truncate(self, definition):
        table_name = definition['TableName']
        if table_name in self._table_names:
            self.delete(table_name)
        self.migrate(definition)

    def migrate(self, definition):
        table_name = definition['TableName']
        if table_name not in self._table_names:
            self._dynamodb.create_table(**definition)
            self._table_names.append(table_name)
            if self.__logging:
                print(f"{table_name} is migrated.")
        elif self.__logging:
            print(f"{table_name} already exists.")

    def delete(self, table_name):
        self._dynamodb.Table(table_name).delete()
        self._table_names.remove(table_name)

    def _path_to(self, file):
        return os.path.join(self._dir, file)

    def _execute_all_file(self, method):
        for file in os.listdir(self._dir):
            if not os.path.isfile(self._path_to(file)):
                continue
            definition = self._read_definition(file)
            method(definition)

    def _read_definition(self, file):
        with open(self._path_to(file)) as json_file:
            definition = json.load(json_file)
        return definition


if __name__ == '__main__':
    DynamoDbMigrator(logging=sys.argv[0]).migrate_all()
