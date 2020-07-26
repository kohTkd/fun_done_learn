from app.constants.activities import MAX_CONTENT_LENGTH
from app.lib.mixin.validatable import Validatable, model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation
from app.lib.mixin.validatable import validate


@model_name('activity')
@validate('session_token', BlankValidation)
@validate('content', BlankValidation)
@validate('content', MaxLengthValidation, limit=MAX_CONTENT_LENGTH)
class ActivityForm(Validatable):
    def __init__(self, **params):
        super().__init__()
        self.session_token = params.get('session_token')
        self.token = params.get('token')
        self.content = params.get('content')
