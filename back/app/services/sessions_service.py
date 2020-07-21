from app.entities.session import Session
from app.errors.invalid_parameters_error import InvalidParametersError
from app.forms.session_form import SessionForm
from app.repositories.sessions_repository import SessionsRepository


class SessionsService():
    @classmethod
    def generate(cls, form: SessionForm) -> Session:
        if form.is_invalid():
            raise InvalidParametersError(form)
        session = Session(title=form.title)
        session.generate_token()
        return session

    @classmethod
    def save(cls, session):
        SessionsRepository().save(session)

    @classmethod
    def find(cls, token) -> Session:
        return SessionsRepository().find(token)
