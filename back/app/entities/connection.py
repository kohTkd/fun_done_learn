from datetime import datetime

from app.entities.application_entity import ApplicationEntity
from app.lib.mixin.validatable import model_name
from app.validations.blank_validation import BlankValidation
from app.lib.mixin.validatable import validate


@model_name('connection')
@validate('expired_at', BlankValidation)
@validate('session_token', BlankValidation)
@validate('id', BlankValidation)
class Connection(ApplicationEntity):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self._expired_at = self.__generate_expired_at()

    @property
    def expired_at(self):
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at: int):
        self._expired_at = expired_at

    def _attribute_names(self):
        return ('session_token', 'id')

    def __generate_expired_at(self):
        now = datetime.datetime.now()
        return now.timedelta(days=1)
