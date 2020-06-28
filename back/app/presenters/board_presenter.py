class BoardPresenter():
    def __init__(self, board):
        self.board = board

    def detail(self):
        return {
            'title': self.board.title,
            'token': self.board.token,
            'created_at': str(self.board.created_at)
        }
