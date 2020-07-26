from app.repositories.application_repository import (
    ApplicationRepository, table_name, hash_key, range_key, entity_repository
)
from app.entities.connection import Connection


@table_name('connections')
@hash_key('session_token')
@range_key('id')
@entity_repository(Connection)
class ConnectionsRepository(ApplicationRepository):
    def _to_save_format(self, connection: Connection) -> dict:
        return {
            'session_token': connection.session_token,
            'id': connection.id,
            'expired_at': connection.expired_at,
            'created_at': str(connection.created_at),
            'updated_at': str(connection.updated_at),
        }
