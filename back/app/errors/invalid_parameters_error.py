class InvalidParametersError(Exception):
    def __init__(self, form):
        self.form = form

    def error_messages(self):
        return self.form.error_messages()
