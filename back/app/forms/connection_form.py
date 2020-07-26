from app.lib.mixin.validatable import Validatable, model_name
from app.validations.blank_validation import BlankValidation
from app.lib.mixin.validatable import validate


@model_name('connection')
@validate('session_token', BlankValidation)
@validate('id', BlankValidation)
class ConnectionForm(Validatable):
    def __init__(self, **params):
        super().__init__()
        self.session_token = params.get('session_token')
        self.id = params.get('id')
