from coupon_management_flask.exceptions.api_exception import ApiException
from coupon_management_flask.utils.http_status_codes import HTTP_404_NOT_FOUND


class EntityNotFoundException(ApiException):
    def __init__(self, message: str):
        super().__init__(message, HTTP_404_NOT_FOUND, "NOT_FOUND")
