from app.constants.activities import MAX_CONTENT_LENGTH
from app.entities.application_entity import ApplicationEntity
from app.entities.placement import Placement
from app.lib.mixin.validatable import model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation
from app.lib.mixin.validatable import validate
from app.lib.mixin.token_generatable import TokenGeneratable


@model_name('activity')
@validate('content', BlankValidation)
@validate('content', MaxLengthValidation, limit=MAX_CONTENT_LENGTH)
@validate('token', BlankValidation)
@validate('session_token', BlankValidation)
@validate('created_at', BlankValidation)
class Activity(ApplicationEntity, TokenGeneratable):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.content = attrs.get('content')
        self.token = attrs.get('token')
        self.session_token = attrs.get('session_token')
        self._placement = Placement(session_token=self.session_token, activity_token=self.token)

    @property
    def placement(self):
        return self._placement

    @placement.setter
    def placement(self, placement: Placement):
        self._placement = placement

    def generate_token(self):
        super().generate_token()
        self._placement.activity_token = self.token
