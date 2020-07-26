from app.constants.notes import MAX_CONTENT_LENGTH
from app.entities.application_entity import ApplicationEntity
from app.lib.mixin.validatable import model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation
from app.lib.mixin.validatable import validate
from app.lib.mixin.token_generatable import TokenGeneratable


@model_name('note')
@validate('content', BlankValidation)
@validate('content', MaxLengthValidation, limit=MAX_CONTENT_LENGTH)
@validate('session_token', BlankValidation)
@validate('token', BlankValidation)
class Note(ApplicationEntity, TokenGeneratable):
    def _attribute_names(self):
        return ('session_token', 'token', 'content')

    def _updatable_attribute_names(self):
        return ('content',)
