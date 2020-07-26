OK = 200
CREATED = 201
NOT_FOUND = 404
UNPROCESSABLE_ENTITY = 422

SUCCEEDED_STATUSES = range(200, 300)

class ApiResponse():
    def __init__(self, body, status):
        self.body = body
        self.status = status

    @classmethod
    def ok(cls, body):
        return ApiResponse(body, OK)

    @classmethod
    def created(cls, body):
        return ApiResponse(body, CREATED)

    @classmethod
    def unprocessable_entity(cls, errors):
        return ApiResponse({'errors': errors}, UNPROCESSABLE_ENTITY)

    @classmethod
    def not_found(cls, errors):
        return ApiResponse({'errors': errors}, NOT_FOUND)

    def succeeded(self) -> bool:
        return self.status in SUCCEEDED_STATUSES
