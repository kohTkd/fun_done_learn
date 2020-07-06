from app.errors.invalid_entity_error import InvalidEntityError
from app.forms.session_form import SessionForm
from app.use_cases.create_session_use_case import CreateSessionUseCase
from app.presenters.session_presenter import SessionPresenter
from app.lib.api_response import ApiResponse


class SessionsController():
    @classmethod
    def create(cls, params: dict) -> ApiResponse:
        form = SessionForm(**params)
        if form.is_invalid():
            return ApiResponse.unprocessable_entity(form.error_messages())
        try:
            session = CreateSessionUseCase.execute(form)
            return ApiResponse.created(SessionPresenter(session).detail())
        except InvalidEntityError as e:
            return ApiResponse.unprocessable_entity(e.error_messages())
