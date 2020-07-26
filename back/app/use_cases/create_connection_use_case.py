from app.entities.session import Session
from app.entities.connection import Connection
from app.errors.not_found_error import NotFoundError
from app.forms.connection_form import ConnectionForm
from app.services.sessions_service import SessionsService
from app.services.connections_service import ConnectionsService


class CreateConnectionUseCase():
    @classmethod
    def execute(cls, form: ConnectionForm) -> Connection:
        session = SessionsService.find(form.session_token)
        if not session:
            raise NotFoundError(Session, token=form.session_token)

        connection = ConnectionsService.generate(form)
        ConnectionsService.save(connection)

        return connection
