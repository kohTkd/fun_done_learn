from app.entities.session import Session
from app.entities.sticky_note import StickyNote
from app.errors.not_found_error import NotFoundError
from app.forms.sticky_note_form import StickyNoteForm
from app.services.sessions_service import SessionsService
from app.services.sticky_notes_service import StickyNotesService


class CreateStickyNoteUseCase():
    @classmethod
    def execute(cls, form: StickyNoteForm) -> StickyNote:
        session = SessionsService.find(form.session_token)
        if not session:
            raise NotFoundError(Session, token=form.session_token)

        sticky_note = StickyNotesService.generate(form)
        StickyNotesService.save(sticky_note)
        return sticky_note
