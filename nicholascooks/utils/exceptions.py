from fastapi import HTTPException, status


class UnauthorizedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        """Returns HTTP 403"""
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)


class UnauthenticatedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
        )


class ExampleNotFoundException(HTTPException):
    def __init__(self, error_str: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_str,
        )
