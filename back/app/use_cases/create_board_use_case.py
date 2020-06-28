from app.entities.board import Board
from app.errors.invalid_parameters_error import InvalidParametersError
from app.forms.board_form import BoardForm
from app.services.boards_service import BoardsService


class CreateBoardUseCase():
    @classmethod
    def execute(cls, form: BoardForm) -> Board:
        if form.is_invalid():
            raise InvalidParametersError(form.errors)
        board = BoardsService.generate(form)
        BoardsService.save(board)
        return board
