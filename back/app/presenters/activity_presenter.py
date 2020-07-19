class ActivityPresenter():
    def __init__(self, activity):
        self.activity = activity

    def detail(self) -> dict:
        return {
            'content': self.activity.content,
            'session_token': self.activity.session_token,
            'token': self.activity.token,
            'created_at': str(self.activity.created_at),
            'updated_at': str(self.activity.updated_at)
        }
