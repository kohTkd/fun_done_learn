import random
import string


from app.constants.session_constants import MAX_TITLE_LENGTH
from app.entities.application_entity import ApplicationEntity
from app.lib.mixin.validatable import model_name
from app.validations.blank_validation import BlankValidation
from app.validations.max_length_validation import MaxLengthValidation
from app.lib.mixin.validatable import validate


@model_name('session')
@validate('title', BlankValidation)
@validate('title', MaxLengthValidation, MAX_TITLE_LENGTH)
@validate('token', BlankValidation)
@validate('created_at', BlankValidation)
class Session(ApplicationEntity):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.title = attrs.get('title')
        self.token = attrs.get('token')
        if attrs.get('persisted'):
            self.persist()
            self.created_at = attrs.get('created_at')

    def generate_token(self):
        seeds = string.digits + string.ascii_lowercase + string.ascii_uppercase
        self.token = ''.join([random.choice(seeds) for i in range(12)])
