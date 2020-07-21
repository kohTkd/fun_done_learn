from app.lib.mixin.validatable import Validatable, model_name
from app.validations.blank_validation import BlankValidation
from app.validations.integer_validation import IntegerValidation
from app.validations.min_integer_validation import MinIntegerValidation
from app.lib.mixin.validatable import validate


@model_name('placement')
@validate('session_token', BlankValidation)
@validate('activity_token', BlankValidation)
@validate('left', BlankValidation)
@validate('left', IntegerValidation)
@validate('left', MinIntegerValidation, limit=0)
@validate('top', BlankValidation)
@validate('top', IntegerValidation)
@validate('top', MinIntegerValidation, limit=0)
class PlacementForm(Validatable):
    def __init__(self, **params):
        super().__init__()
        self.session_token = params.get('session_token')
        self.activity_token = params.get('activity_token')
        self.left = params.get('left')
        self.top = params.get('top')
