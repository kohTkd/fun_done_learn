from app.entities.board import Board
from app.forms.board_form import BoardForm
from app.repositories.boards_repository import BoardsRepository


class BoardsService():
    @classmethod
    def generate(cls, form: BoardForm) -> Board:
        board = Board(title=form.title)
        board.generate_token()
        return board

    @classmethod
    def save(cls, board):
        board.set_time_stamp()
        BoardsRepository().save(board)
