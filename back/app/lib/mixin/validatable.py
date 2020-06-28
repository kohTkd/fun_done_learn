from abc import ABCMeta
from app.validations.validation import Validation


class Validatable(metaclass=ABCMeta):
    def __init__(self):
        self.validations = {}

    def is_valid(self) -> bool:
        return self._validate()

    def is_invalid(self) -> bool:
        return not self.is_valid()

    def error_messages(self) -> list:
        return [
            error.message for error in [
                v for v in self._all_validations() if v.is_invalid()]]

    def _register_validation(
            self,
            attr_name: str,
            validator_class: Validation,
            check_value=None):
        validator = validator_class(self, attr_name, check_value)
        validations = [
            v for v in self.validations.get(
                attr_name, []) if not isinstance(
                v, validator_class)]
        validations.append(validator)
        self.validations[attr_name] = validations

    def _all_validations(self):
        validations = []
        for v in self.validations.values():
            validations.extend(v)
        return validations

    def _validate(self) -> bool:
        return all(validation.is_valid()
                   for validation in self._all_validations())


def model_name(key):
    def decoratee(klass):
        setattr(klass, 'model_name', key)
        return klass
    return decoratee
