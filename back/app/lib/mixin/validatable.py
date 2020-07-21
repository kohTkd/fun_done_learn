from abc import ABCMeta
from app.validations.validation import Validation


def validate(attr_name: str, validation: Validation, **kwargs):
    def decoratee(klass):
        if not hasattr(klass, 'registerable_validations'):
            setattr(klass, 'registerable_validations', [])
        klass.registerable_validations.append(
            {'attr_name': attr_name, 'validation': validation, 'options': kwargs}
        )
        return klass
    return decoratee


class Validatable(metaclass=ABCMeta):
    def __init__(self):
        self._validations = {}
        self.__register_validations()

    def is_valid(self) -> bool:
        return self._validate()

    def is_invalid(self) -> bool:
        return not self.is_valid()

    def error_messages(self) -> list:
        return [
            error.message() for error in [
                v for v in self._all_validations() if v.is_invalid()]]

    def _register_validation(
            self,
            attr_name: str,
            validator_class: Validation,
            **kwargs):

        validator = validator_class(self, attr_name, **kwargs)
        validations = [
            v for v in self._validations.get(
                attr_name, []) if not isinstance(
                v, validator_class)]
        validations.append(validator)
        self._validations[attr_name] = validations

    def _all_validations(self):
        validations = []
        for v in self._validations.values():
            validations.extend(v)
        return validations

    def _validate(self) -> bool:
        return all(validation.is_valid()
                   for validation in self._all_validations())

    def __register_validations(self):
        for v in self.registerable_validations:
            self._register_validation(
                v['attr_name'], v['validation'], **v['options']
            )


def model_name(key):
    def decoratee(klass):
        setattr(klass, 'model_name', key)
        return klass
    return decoratee
