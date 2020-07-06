from abc import ABCMeta, abstractmethod
import os
import yaml


def validation_method(func):
    def wrapper(self, *args, **kwargs):
        valid = func(self, *args, **kwargs)
        self.valid = valid
        return valid

    return wrapper


class Validation(metaclass=ABCMeta):
    def __init__(self, model, attr_name, threshold=None):
        self._model = model
        self._attr_name = attr_name
        self._threshold = threshold
        self._valid = None
        self._last_value = None

    @abstractmethod
    def _execute(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def message(self) -> str:
        raise NotImplementedError()

    def is_valid(self):
        if self._last_value != self._value():
            self._valid = None
        self._last_value = self._value()

        return self._valid if self._valid is not None else self._execute()

    def is_invalid(self):
        return not self.is_valid()

    def _value(self):
        return getattr(self._model, self._attr_name)

    def _translated_attr(self):
        with open(f"{self._locale_path()}/{self._model.model_name}.yml", 'r') as yml:
            locale = yaml.load(yml, Loader=yaml.FullLoader)

        return locale['attributes'][self._attr_name]

    def _locale_path(self):
        return f"{os.path.dirname(__file__)}/../../config/locale/ja"
