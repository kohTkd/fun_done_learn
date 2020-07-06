import random
import string


from app.constants.session_constants import MAX_TITLE_LENGTH
from app.entities.application_entity import ApplicationEntity
from app.lib.mixin.validatable import model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation


@model_name('session')
class Session(ApplicationEntity):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.title = attrs.get('title')
        self.token = attrs.get('token')

        self._register_validation('title', BlankValidation)
        self._register_validation('title', MaxLengthValidation, MAX_TITLE_LENGTH)
        self._register_validation('token', BlankValidation)
        self._register_validation('created_at', BlankValidation)

    def generate_token(self):
        seeds = string.digits + string.ascii_lowercase + string.ascii_uppercase
        self.token = ''.join([random.choice(seeds) for i in range(12)])
