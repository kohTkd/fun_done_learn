from app.entities.session import Session
from app.errors.not_found_error import NotFoundError
from app.services.sessions_service import SessionsService
from app.services.activities_service import ActivitiesService


class FindActivitiesUseCase():
    @classmethod
    def execute(cls, session_token: str) -> list:
        session = SessionsService.find(session_token)
        if not session:
            raise NotFoundError(Session, token=session_token)

        return ActivitiesService.query(session_token)
