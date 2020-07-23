from app.entities.note import Note
from app.errors.invalid_parameters_error import InvalidParametersError
from app.forms.note_form import NoteForm
from app.repositories.notes_repository import NotesRepository


class NotesService():
    @classmethod
    def generate(cls, form: NoteForm) -> Note:
        if form.is_invalid():
            raise InvalidParametersError(form)
        note = Note(content=form.content, session_token=form.session_token)
        note.generate_token()
        return note

    @classmethod
    def save(cls, note):
        NotesRepository().save(note)

    @classmethod
    def find(cls, session_token, token) -> Note:
        return NotesRepository().find(session_token, token)

    @classmethod
    def query(cls, session_token):
        notes = NotesRepository().query(session_token)

        return sorted(notes, key=lambda note: note.created_at)
