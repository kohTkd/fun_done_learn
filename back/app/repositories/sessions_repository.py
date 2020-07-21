from app.repositories.application_repository import ApplicationRepository, table_name, hash_key, entity_repository
from app.entities.session import Session


@table_name('sessions')
@hash_key('token')
@entity_repository(Session)
class SessionsRepository(ApplicationRepository):
    def _to_save_format(self, session: Session) -> dict:
        return {
            'title': session.title,
            'token': session.token,
            'created_at': str(session.created_at),
            'updated_at': str(session.updated_at),
        }
