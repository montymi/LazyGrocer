"""Custom error classes for the application."""


class BaseAPIError(Exception):
    """Base exception class for API errors."""

    status_code = 500
    message = "Internal server error"

    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__()
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """Convert error to dictionary for JSON response."""
        rv = dict(self.payload or ())
        rv['error'] = {
            'message': self.message,
            'status_code': self.status_code
        }
        return rv


class ValidationError(BaseAPIError):
    """Raised when input validation fails."""

    status_code = 400
    message = "Validation error"


class NotFoundError(BaseAPIError):
    """Raised when a resource is not found."""

    status_code = 404
    message = "Resource not found"


class ConflictError(BaseAPIError):
    """Raised when there's a conflict with existing data."""

    status_code = 409
    message = "Conflict with existing resource"


class UnauthorizedError(BaseAPIError):
    """Raised when authentication is required."""

    status_code = 401
    message = "Unauthorized access"


class ForbiddenError(BaseAPIError):
    """Raised when access is forbidden."""

    status_code = 403
    message = "Access forbidden"


class DatabaseError(BaseAPIError):
    """Raised when database operation fails."""

    status_code = 500
    message = "Database operation failed"


class BadRequestError(BaseAPIError):
    """Raised for bad requests."""

    status_code = 400
    message = "Bad request"