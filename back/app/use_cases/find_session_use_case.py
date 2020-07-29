from app.entities.session import Session
from app.errors.not_found_error import NotFoundError
from app.services.sessions_service import SessionsService


class FindSessionUseCase():
    @classmethod
    def execute(cls, token: str) -> Session:
        session = SessionsService.find(token)
        if not session:
            raise NotFoundError(Session, token=token)
        return session
