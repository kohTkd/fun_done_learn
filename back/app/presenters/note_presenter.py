class NotePresenter():
    def __init__(self, note):
        self.note = note

    def detail(self) -> dict:
        return {
            'content': self.note.content,
            'session_token': self.note.session_token,
            'token': self.note.token,
            'created_at': str(self.note.created_at),
            'updated_at': str(self.note.updated_at)
        }
