from app.validations.validation import Validation


class BlankValidation(Validation):
    def _execute(self):
        self._valid = not (not self._value())
        return self._valid

    def message(self):
        return f"{self._attr_name()}は必須です"
