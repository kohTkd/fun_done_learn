from app.errors.invalid_entity_error import InvalidEntityError
from app.forms.board_form import BoardForm
from app.use_cases.create_board_use_case import CreateBoardUseCase
from app.presenters.board_presenter import BoardPresenter
from app.lib.api_response import ApiResponse


class BoardsController():
    @classmethod
    def create(cls, params: dict) -> ApiResponse:
        form = BoardForm(**params)
        if form.is_invalid():
            return ApiResponse.unprocessable_entity(form.error_messages())
        try:
            board = CreateBoardUseCase.execute(form)
            return ApiResponse.created(BoardPresenter(board).detail())
        except InvalidEntityError as e:
            return ApiResponse.unprocessable_entity(e.error_messages())
