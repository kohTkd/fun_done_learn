from app.entities.session import Session
from app.entities.connection import Connection
from app.errors.not_found_error import NotFoundError
from app.services.sessions_service import SessionsService
from app.services.connections_service import ConnectionsService


class DestroyConnectionUseCase():
    @classmethod
    def execute(cls, session_token: str, id: str) -> Connection:
        session = SessionsService.find(session_token)
        if not session:
            raise NotFoundError(Session, token=session_token)

        connection = ConnectionsService.find(session_token, id)
        ConnectionsService.destroy(connection)

        return connection
