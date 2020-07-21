from app.constants.sessions import MAX_TITLE_LENGTH
from app.lib.mixin.validatable import Validatable, model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation
from app.lib.mixin.validatable import validate


@model_name('session')
@validate('title', BlankValidation)
@validate('title', MaxLengthValidation, limit=MAX_TITLE_LENGTH)
class SessionForm(Validatable):
    def __init__(self, **params):
        super().__init__()
        self.title = params.get('title')
