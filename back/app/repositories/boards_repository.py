from app.repositories.application_repository import ApplicationRepository, table_name, hash_key, entity_repository
from app.entities.board import Board


@table_name('boards')
@hash_key('token')
@entity_repository(Board)
class BoardsRepository(ApplicationRepository):
    def _to_save_format(self, board) -> dict:
        return {
            'title': board.title,
            'token': board.token,
            'created_at': str(board.created_at),
        }
