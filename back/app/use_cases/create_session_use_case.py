from app.entities.session import Session
from app.errors.invalid_parameters_error import InvalidParametersError
from app.forms.session_form import SessionForm
from app.services.sessions_service import SessionsService


class CreateSessionUseCase():
    @classmethod
    def execute(cls, form: SessionForm) -> Session:
        if form.is_invalid():
            raise InvalidParametersError(form.errors)
        session = SessionsService.generate(form)
        SessionsService.save(session)
        return session
