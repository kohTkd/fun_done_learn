from app.entities.session import Session
from app.services.sessions_service import SessionsService
from app.services.connections_service import ConnectionsService


class BloadcastUseCase():
    @classmethod
    def execute(cls, body: dict, resource_name: str, action: str):
        session_token = body.get('session_token') or body.get('session')
        session = SessionsService.find(session_token)
        if not session:
            return

        connections = ConnectionsService.query(session_token)
        if not connections:
            return

        connection_ids = [connection.id for connection in connections]
        ConnectionsService.bloadcast(connection_ids, body, resource_name, action)
