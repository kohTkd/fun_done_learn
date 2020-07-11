from app.constants.sticky_note_constants import MAX_CONTENT_LENGTH
from app.lib.mixin.validatable import Validatable, model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation
from app.lib.mixin.validatable import validate


@model_name('sticky_note')
@validate('content', BlankValidation)
@validate('content', MaxLengthValidation, MAX_CONTENT_LENGTH)
class StickyNoteForm(Validatable):
    def __init__(self, **params):
        super().__init__()
        self.session_token = params.get('session_token')
        self.content = params.get('content')
