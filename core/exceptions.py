#  Copyright (c) 2024.
#  Julio Cezar Riffel
#  https://www.linkedin.com/in/julio-cezar-riffel/
#  https://github.com/julioriffel

from enum import Enum

from fastapi import HTTPException, status


class ErrorsEnum(str, Enum):
    NOT_FOUND = "NOT_FOUND"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"


class BaseException(HTTPException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Error"

    def __init__(self, **kwargs):
        super().__init__(status_code=self.STATUS_CODE, detail=self.DETAIL, **kwargs)


class NotFoundException(BaseException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = ErrorsEnum.NOT_FOUND


class LimitExceededException(BaseException):
    STATUS_CODE = status.HTTP_422_UNPROCESSABLE_ENTITY
    DETAIL = ErrorsEnum.LIMIT_EXCEEDED
