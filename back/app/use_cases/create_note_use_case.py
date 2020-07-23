from app.entities.session import Session
from app.entities.note import Note
from app.errors.not_found_error import NotFoundError
from app.forms.note_form import NoteForm
from app.services.sessions_service import SessionsService
from app.services.notes_service import NotesService


class CreateNoteUseCase():
    @classmethod
    def execute(cls, form: NoteForm) -> Note:
        session = SessionsService.find(form.session_token)
        if not session:
            raise NotFoundError(Session, token=form.session_token)

        note = NotesService.generate(form)
        NotesService.save(note)
        return note
