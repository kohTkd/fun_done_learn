from app.validations.validation import Validation, validation_method


class BlankValidation(Validation):
    @validation_method
    def _execute(self):
        self._valid = self._value() is not None and self._value() != ''
        return self._valid

    def message(self):
        return f"{self._translated_attr()}は必須です"
