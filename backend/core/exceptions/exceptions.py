from http import HTTPStatus
from fastapi import status


class CustomException(Exception):
    """
    Custom exception class to handle all exceptions.
    Args:
        message: The error message.
        error_code: The error code.
        message: The error message.
    """

    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = HTTPStatus.BAD_GATEWAY.description

    def __init__(self, message: str = None) -> None:
        if message:
            self.message = message


class AuthenticationRequiredException(CustomException):
    """
    Authentication required exception.
    """

    code = status.HTTP_401_UNAUTHORIZED
    error_code = status.HTTP_401_UNAUTHORIZED
    message = "Authentication required"


class InsufficientPermissionsException(CustomException):
    """
    Insufficient permissions exception.
    """

    code = HTTPStatus.FORBIDDEN
    error_code = HTTPStatus.FORBIDDEN
    message = "Insufficient permissions"

class AuthenticationRequiredException(CustomException):
    """
    Authentication required exception.
    """

    code = status.HTTP_401_UNAUTHORIZED
    error_code = status.HTTP_401_UNAUTHORIZED
    message = "Authentication required"

class TimeoutException(CustomException):
    """
    Timeout exception.
    """

    code = HTTPStatus.REQUEST_TIMEOUT
    error_code = HTTPStatus.REQUEST_TIMEOUT
    message = HTTPStatus.REQUEST_TIMEOUT.description


class InternalServerException(CustomException):
    """
    Internal server exception.
    """

    code = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = HTTPStatus.INTERNAL_SERVER_ERROR.description


class BadRequestException(CustomException):
    """
    Bad request exception.
    """

    code = HTTPStatus.BAD_REQUEST
    error_code = HTTPStatus.BAD_REQUEST
    message = HTTPStatus.BAD_REQUEST.description


class NotFoundException(CustomException):
    """
    Resource not found exception.
    """

    code = HTTPStatus.NOT_FOUND
    error_code = HTTPStatus.NOT_FOUND
    message = HTTPStatus.NOT_FOUND.description



class UnauthorizedException(CustomException):
    """
    Unauthorized exception.
    """

    code = HTTPStatus.UNAUTHORIZED
    error_code = HTTPStatus.UNAUTHORIZED
    message = HTTPStatus.UNAUTHORIZED.description
