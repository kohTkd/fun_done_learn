from app.repositories.application_repository import (
    ApplicationRepository, table_name, hash_key, range_key, entity_repository
)
from app.entities.activity import Activity


@table_name('activities')
@hash_key('session_token')
@range_key('token')
@entity_repository(Activity)
class ActivitiesRepository(ApplicationRepository):
    def _to_save_format(self, activity) -> dict:
        return {
            'content': activity.content,
            'token': activity.token,
            'session_token': activity.session_token,
            'created_at': str(activity.created_at),
            'updated_at': str(activity.updated_at),
        }
