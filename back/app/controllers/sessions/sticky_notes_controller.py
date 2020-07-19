from app.errors.invalid_entity_error import InvalidEntityError
from app.errors.not_found_error import NotFoundError
from app.forms.sticky_note_form import StickyNoteForm
from app.use_cases.create_sticky_note_use_case import CreateStickyNoteUseCase
from app.use_cases.query_sticky_notes_use_case import QueryStickyNotesUseCase
from app.presenters.sticky_note_presenter import StickyNotePresenter
from app.lib.api_response import ApiResponse


class StickyNotesController():
    @classmethod
    def create(cls, params: dict) -> ApiResponse:
        form = StickyNoteForm(**params)
        if form.is_invalid():
            return ApiResponse.unprocessable_entity(form.error_messages())
        try:
            sticky_note = CreateStickyNoteUseCase.execute(form)
            return ApiResponse.created(cls._detail(sticky_note))
        except NotFoundError as e:
            return ApiResponse.not_found(e.error_messages())
        except InvalidEntityError as e:
            return ApiResponse.unprocessable_entity(e.error_messages())

    @classmethod
    def index(cls, params: dict) -> ApiResponse:
        try:
            sticky_notes = QueryStickyNotesUseCase.execute(params.get('session_token'))
            return ApiResponse.ok(cls._details(sticky_notes))
        except NotFoundError as e:
            return ApiResponse.not_found(e.error_messages())

    @classmethod
    def _detail(cls, sticky_note) -> dict:
        return StickyNotePresenter(sticky_note).detail()

    @classmethod
    def _details(cls, sticky_notes) -> list:
        return [cls._detail(sticky_note) for sticky_note in sticky_notes]

    # @classmethod
    # def show(cls, params: dict) -> ApiResponse:
    #     try:
    #         session = FindSessionUseCase.execute(params.get('token'))
    #         return ApiResponse.ok(cls._detail(session))
    #     except NotFoundError as e:
    #         return ApiResponse.not_found(e.error_messages())
