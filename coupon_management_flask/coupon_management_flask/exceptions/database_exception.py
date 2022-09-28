from coupon_management_flask.exceptions.api_exception import ApiException
from coupon_management_flask.utils.http_status_codes import HTTP_500_INTERNAL_SERVER_ERROR


class DatabaseException(ApiException):
    def __init__(self, message: str):
        super().__init__(message, HTTP_500_INTERNAL_SERVER_ERROR, "INTERNAL_SERVER_ERROR")