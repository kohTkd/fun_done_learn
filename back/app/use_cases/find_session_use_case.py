from app.entities.session import Session
from app.services.sessions_service import SessionsService


class FindSessionUseCase():
    @classmethod
    def execute(cls, token: str) -> Session:
        return SessionsService.find(token)
