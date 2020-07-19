from app.constants.sessions import MAX_TITLE_LENGTH
from app.entities.application_entity import ApplicationEntity
from app.lib.mixin.validatable import model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation
from app.lib.mixin.validatable import validate
from app.lib.mixin.token_generatable import TokenGeneratable


@model_name('session')
@validate('title', BlankValidation)
@validate('title', MaxLengthValidation, MAX_TITLE_LENGTH)
@validate('token', BlankValidation)
@validate('created_at', BlankValidation)
class Session(ApplicationEntity, TokenGeneratable):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.title = attrs.get('title')
        self.token = attrs.get('token')
