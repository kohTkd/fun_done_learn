from app.errors.application_error import ApplicationError


class NotPersistedError(ApplicationError):
    def error_messages(self):
        return f"{self._translated_model()}は永続化されていません"
