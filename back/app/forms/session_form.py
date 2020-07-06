from app.constants.session_constants import MAX_TITLE_LENGTH
from app.lib.mixin.validatable import Validatable, model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation


@model_name('session')
class SessionForm(Validatable):
    def __init__(self, **params):
        super().__init__()
        self.title = params.get('title')

        self._register_validation('title', BlankValidation)
        self._register_validation('title', MaxLengthValidation, MAX_TITLE_LENGTH)