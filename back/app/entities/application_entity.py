from abc import ABCMeta
import datetime

import dateutil.parser

from app.lib.mixin.validatable import Validatable


class ApplicationEntity(Validatable, metaclass=ABCMeta):
    def __init__(self, **attrs):
        super().__init__()
        if attrs.get('persisted'):
            self._persisted = True
            self._restore_timestamp(attrs, 'created_at')
            self._restore_timestamp(attrs, 'updated_at')
        else:
            self._persisted = False
            self.created_at = None
            self.updated_at = None

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

    def _restore_timestamp(self, attrs, attr_name):
        timestamp = attrs.get(attr_name)
        if isinstance(timestamp, str):
            timestamp = dateutil.parser.parse(timestamp)
        setattr(self, attr_name, timestamp)
