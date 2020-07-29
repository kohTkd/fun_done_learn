from app.entities.session import Session
from app.entities.activity import Activity
from app.errors.not_found_error import NotFoundError
from app.services.sessions_service import SessionsService
from app.services.activities_service import ActivitiesService
from app.services.placements_service import PlacementsService


class DestroyActivityUseCase():
    @classmethod
    def execute(cls, session_token: str, token: str) -> Activity:
        session = SessionsService.find(session_token)
        if not session:
            raise NotFoundError(Session, token=session_token)

        activity = ActivitiesService.find(session_token, token)
        if not activity:
            raise NotFoundError(Activity, token=token)

        placement = PlacementsService.find(session_token, token)
        PlacementsService.destroy(placement)

        ActivitiesService.destroy(activity)
        return activity
