from app.entities.session import Session
from app.forms.session_form import SessionForm
from app.repositories.sessions_repository import SessionsRepository


class SessionsService():
    @classmethod
    def generate(cls, form: SessionForm) -> Session:
        session = Session(title=form.title)
        session.generate_token()
        return session

    @classmethod
    def save(cls, session):
        session.set_time_stamp()
        SessionsRepository().save(session)
