from app.controllers.decorators.controller_methods import error_handleable
from app.forms.session_form import SessionForm
from app.use_cases.create_session_use_case import CreateSessionUseCase
from app.use_cases.find_session_use_case import FindSessionUseCase
from app.presenters.session_presenter import SessionPresenter
from app.lib.api_response import ApiResponse


class SessionsController():
    @classmethod
    @error_handleable
    def create(cls, params: dict) -> ApiResponse:
        form = SessionForm(**params)
        session = CreateSessionUseCase.execute(form)
        return ApiResponse.created(cls._detail(session))

    @classmethod
    @error_handleable
    def show(cls, params: dict) -> ApiResponse:
        session = FindSessionUseCase.execute(params.get('token'))
        return ApiResponse.ok(cls._detail(session))

    @classmethod
    def _detail(cls, session) -> dict:
        return SessionPresenter(session).detail()
