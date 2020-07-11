from app.repositories.application_repository import (
    ApplicationRepository, table_name, hash_key, range_key, entity_repository
)
from app.entities.sticky_note import StickyNote


@table_name('sticky_notes')
@hash_key('session_token')
@range_key('token')
@entity_repository(StickyNote)
class StickyNotesRepository(ApplicationRepository):
    def _to_save_format(self, sticky_note) -> dict:
        return {
            'content': sticky_note.content,
            'token': sticky_note.token,
            'session_token': sticky_note.session_token,
            'created_at': str(sticky_note.created_at),
            'updated_at': str(sticky_note.updated_at),
        }
