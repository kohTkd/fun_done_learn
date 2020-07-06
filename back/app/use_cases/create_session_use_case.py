from app.entities.session import Session
from app.forms.session_form import SessionForm
from app.services.sessions_service import SessionsService


class CreateSessionUseCase():
    @classmethod
    def execute(cls, form: SessionForm) -> Session:
        session = SessionsService.generate(form)
        SessionsService.save(session)
        return session
