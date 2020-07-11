class StickyNotePresenter():
    def __init__(self, sticky_note):
        self.sticky_note = sticky_note

    def detail(self) -> dict:
        return {
            'content': self.sticky_note.content,
            'session_token': self.sticky_note.session_token,
            'token': self.sticky_note.token,
            'created_at': str(self.sticky_note.created_at),
            'updated_at': str(self.sticky_note.updated_at)
        }
