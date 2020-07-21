from app.entities.application_entity import ApplicationEntity
from app.lib.mixin.validatable import model_name
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
@validate('session_token', BlankValidation)
@validate('created_at', BlankValidation)
class Placement(ApplicationEntity):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.session_token = attrs.get('session_token')
        self.activity_token = attrs.get('activity_token')
        self.left = attrs.get('left')
        self.top = attrs.get('top')

    def update(self, **attrs):
        if 'left' in attrs:
            self.left = attrs.get('left')
        if 'top' in attrs:
            self.top = attrs.get('top')
