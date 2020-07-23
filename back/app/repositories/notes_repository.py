from app.repositories.application_repository import (
    ApplicationRepository, table_name, hash_key, range_key, entity_repository
)
from app.entities.note import Note


@table_name('notes')
@hash_key('session_token')
@range_key('token')
@entity_repository(Note)
class NotesRepository(ApplicationRepository):
    def _to_save_format(self, note: Note) -> dict:
        return {
            'session_token': note.session_token,
            'token': note.token,
            'content': note.content,
            'created_at': str(note.created_at),
            'updated_at': str(note.updated_at),
        }
