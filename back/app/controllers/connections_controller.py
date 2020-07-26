from app.controllers.decorators.controller_methods import error_handleable
from app.forms.connection_form import ConnectionForm
from app.use_cases.create_session_use_case import CreateSessionUseCase
from app.use_cases.find_session_use_case import FindSessionUseCase
from app.presenters.session_presenter import SessionPresenter
from app.lib.api_response import ApiResponse


class ConnectionsController():
    @classmethod
    @error_handleable
    def create(cls, params: dict) -> ApiResponse:
        form = ConnectionForm(**params)
        session = CreateSessionUseCase.execute(form)
        return ApiResponse.created(cls._detail(session))

    @classmethod
    @error_handleable
    def destroy(cls, params: dict) -> ApiResponse:
        pass

    @classmethod
    def _detail(cls, session) -> dict:
        return SessionPresenter(session).detail()
