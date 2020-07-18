from app.validations.validation import Validation, validation_method


class MaxLengthValidation(Validation):
    @validation_method
    def _execute(self):
        self._valid = (not self._value()) or len(self._value()) <= self._threshold
        return self._valid

    def message(self):
        return f"{self._translated_attr()}は{self._threshold}文字以内で設定してください"
