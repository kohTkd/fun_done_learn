from app.validations.validation import Validation, validation_method


class IntegerValidation(Validation):
    @validation_method
    def _execute(self):
        self._valid = (not self._value()) or isinstance(self._value(), int)
        return self._valid

    def message(self):
        return f"{self._translated_attr()}は数値を設定してください"
