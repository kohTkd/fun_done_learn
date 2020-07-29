import json
import os

import boto3

from app.entities.connection import Connection
from app.errors.invalid_parameters_error import InvalidParametersError
from app.forms.connection_form import ConnectionForm
from app.repositories.connections_repository import ConnectionsRepository


class ConnectionsService():
    @classmethod
    def generate(cls, form: ConnectionForm) -> Connection:
        if form.is_invalid():
            raise InvalidParametersError(form)
        return Connection(id=form.id, session_token=form.session_token)

    @classmethod
    def save(cls, connection):
        ConnectionsRepository().save(connection)

    @classmethod
    def query(cls, session_token):
        return ConnectionsRepository().query(session_token)

    @classmethod
    def destroy(cls, connection):
        return ConnectionsRepository().destroy(connection)

    @classmethod
    def bloadcast(cls, connection_ids, body, resource_name, action):
        gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url=os.environ.get('API_GATEWAY_ENDPOINT'))
        data = {'resource': resource_name, 'action': action, 'body': body}
        for id in connection_ids:
            gatewayapi.post_to_connection(ConnectionId=id, Data=json.dumps(data).encode('utf-8'))
