from app.controllers.decorators.controller_methods import error_handleable
from app.forms.note_form import NoteForm
from app.use_cases.create_note_use_case import CreateNoteUseCase
from app.use_cases.find_notes_use_case import FindNotesUseCase
from app.presenters.note_presenter import NotePresenter
from app.lib.api_response import ApiResponse


class NotesController():
    @classmethod
    @error_handleable
    def create(cls, params: dict) -> ApiResponse:
        form = NoteForm(**params)
        note = CreateNoteUseCase.execute(form)
        return ApiResponse.created(cls._detail(note))

    @classmethod
    @error_handleable
    def index(cls, params: dict) -> ApiResponse:
        notes = FindNotesUseCase.execute(params.get('session_token'))
        return ApiResponse.ok(cls._details(notes))

    @classmethod
    def _detail(cls, note) -> dict:
        return NotePresenter(note).detail()

    @classmethod
    def _details(cls, notes) -> list:
        return [cls._detail(note) for note in notes]
