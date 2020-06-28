import boto3
import json
import os


class DynamoDbMigrator():
    def __init__(self, region=None):
        if not region:
            region = os.environ['DYNAMODB_REGION']
        self._dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=os.environ['DYNAMODB_ENDPOINT'],
            region_name=region)
        self._table_names = [t.table_name for t in self._dynamodb.tables.all()]
        self._dir = f"{os.path.dirname(__file__)}/../config/dynamodb/tables"

    def truncate(self, file):
        with open(self._path_to(file)) as json_file:
            definition = json.load(json_file)
        table_name = definition['TableName']
        if table_name in self._table_names:
            self._dynamodb.Table(table_name).delete()
        else:
            self._table_names.append(table_name)
        self._dynamodb.create_table(**definition)

    def truncate_all(self):
        for file in os.listdir(self._dir):
            if not os.path.isfile(self._path_to(file)):
                continue
            self.truncate(file)

    def _path_to(self, file):
        return os.path.join(self._dir, file)


if __name__ == '__main__':
    DynamoDbMigrator().truncate_all()
