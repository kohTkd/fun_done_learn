from app.errors.application_error import ApplicationError


class NotFoundError(ApplicationError):
    def error_messages(self):
        return f"{self._translated_model()}が見つかりません"
