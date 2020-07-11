from app.entities.sticky_note import StickyNote
from app.errors.invalid_parameters_error import InvalidParametersError
from app.forms.sticky_note_form import StickyNoteForm
from app.repositories.sticky_notes_repository import StickyNotesRepository


class StickyNotesService():
    @classmethod
    def generate(cls, form: StickyNoteForm) -> StickyNote:
        if form.is_invalid():
            raise InvalidParametersError(form.errors)
        sticky_note = StickyNote(content=form.content, session_token=form.session_token)
        sticky_note.generate_token()
        return sticky_note

    @classmethod
    def save(cls, sticky_note):
        StickyNotesRepository().save(sticky_note)

    @classmethod
    def find(cls, session_token, token) -> StickyNote:
        return StickyNotesRepository().find(session_token, token)
