from app.repositories.application_repository import (
    ApplicationRepository, table_name, hash_key, range_key, entity_repository
)
from app.entities.placement import Placement


@table_name('placements')
@hash_key('session_token')
@range_key('activity_token')
@entity_repository(Placement)
class PlacementsRepository(ApplicationRepository):
    def _to_save_format(self, placement: Placement) -> dict:
        return {
            'session_token': placement.session_token,
            'activity_token': placement.activity_token,
            'left': placement.left,
            'top': placement.top,
            'created_at': str(placement.created_at),
            'updated_at': str(placement.updated_at),
        }
