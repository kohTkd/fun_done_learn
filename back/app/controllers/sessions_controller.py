from app.errors.invalid_entity_error import InvalidEntityError
from app.errors.not_found_error import NotFoundError
from app.forms.session_form import SessionForm
from app.use_cases.create_session_use_case import CreateSessionUseCase
from app.use_cases.find_session_use_case import FindSessionUseCase
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
            return ApiResponse.created(cls._detail(session))
        except InvalidEntityError as e:
            return ApiResponse.unprocessable_entity(e.error_messages())

    @classmethod
    def show(cls, params: dict) -> ApiResponse:
        try:
            session = FindSessionUseCase.execute(params.get('token'))
            return ApiResponse.ok(cls._detail(session))
        except NotFoundError as e:
            return ApiResponse.not_found(e.error_messages())

    @classmethod
    def _detail(cls, session) -> dict:
        return SessionPresenter(session).detail()
