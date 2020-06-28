from app.validations.validation import Validation


class MaxLengthValidation(Validation):
    def _execute(self):
        self._valid = len(self._value()) <= self._threshold
        return self._valid

    def message(self):
        return f"{self._attr_name()}は{self._threshold}以下で設定してください"
