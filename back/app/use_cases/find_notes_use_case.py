from app.entities.session import Session
from app.errors.not_found_error import NotFoundError
from app.services.sessions_service import SessionsService
from app.services.notes_service import NotesService


class FindNotesUseCase():
    @classmethod
    def execute(cls, session_token: str) -> list:
        session = SessionsService.find(session_token)
        if not session:
            raise NotFoundError(Session, token=session_token)

        return NotesService.query(session_token)
