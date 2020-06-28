from abc import ABCMeta
import datetime

import dateutil.parser

from app.lib.mixin.validatable import Validatable


class ApplicationEntity(Validatable, metaclass=ABCMeta):
    def __init__(self, **attrs):
        super().__init__()
        self._persisted = False
        self.created_at = attrs.get('created_at')
        if isinstance(self.created_at, str):
            self.created_at = dateutil.parser.parse(self.created_at)

    def set_time_stamp(self):
        now = datetime.datetime.now()
        if hasattr(self, 'created_at') and not self.created_at:
            self.created_at = now
        if hasattr(self, 'updated_at'):
            self.updated_at = now

    def persist(self):
        self.persisted = True
        return self.is_persisted()

    def is_persisted(self):
        return self._persisted
