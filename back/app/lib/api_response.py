OK = 200
CREATED = 201
UNPROCESSABLE_ENTITY = 422


class ApiResponse():
    def __init__(self, body, status):
        self.body = body
        self.status = status

    @classmethod
    def created(cls, body):
        return ApiResponse(body, CREATED)

    @classmethod
    def unprocessable_entity(cls, body):
        return ApiResponse(body, UNPROCESSABLE_ENTITY)
