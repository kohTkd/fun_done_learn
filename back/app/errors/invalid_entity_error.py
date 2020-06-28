class InvalidEntityError(Exception):
    def __init__(self, model):
        self.model = model
