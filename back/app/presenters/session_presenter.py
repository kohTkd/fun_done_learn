class SessionPresenter():
    def __init__(self, session):
        self.session = session

    def detail(self) -> dict:
        return {
            'title': self.session.title,
            'token': self.session.token,
            'created_at': str(self.session.created_at)
        }
