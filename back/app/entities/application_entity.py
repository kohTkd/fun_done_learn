from abc import ABCMeta, abstractmethod
import datetime

import dateutil.parser

from app.lib.mixin.validatable import Validatable


class ApplicationEntity(Validatable, metaclass=ABCMeta):
    def __init__(self, **attrs):
        super().__init__()
        self._set_attributes(self._attribute_names, **attrs)
        self._destroyed = False
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

    def update(self, **attrs):
        self._set_attributes(self._updatable_attribute_names, **attrs)

    def persist(self):
        self.persisted = True
        return self.is_persisted()

    def is_persisted(self):
        return self._persisted

    def destroy(self):
        self.persisted = False
        self._destroyed = True
        return self.is_destroyed()

    def is_destroyed(self):
        return self._destroyed

    def _restore_timestamp(self, attrs, attr_name):
        timestamp = attrs.get(attr_name)
        if isinstance(timestamp, str):
            timestamp = dateutil.parser.parse(timestamp)
        setattr(self, attr_name, timestamp)

    def _set_attributes(self, attribute_names, **attrs):
        for attr_name in attribute_names():
            if attr_name in attrs:
                setattr(self, attr_name, attrs[attr_name])
            elif not hasattr(self, attr_name):
                setattr(self, attr_name, None)

    def _updatable_attribute_names(self):
        return []

    @abstractmethod
    def _attribute_names(self):
        raise NotImplementedError()
