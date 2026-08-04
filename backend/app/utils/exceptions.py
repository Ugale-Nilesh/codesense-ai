"""Custom application exceptions.

Each exception carries a machine-readable code and an HTTP-appropriate
status_code, matching the error response shape defined in
docs/06_API_Contracts.md: status, code, message, details.
"""


class AppError(Exception):
    """Base class for all application-specific exceptions."""

    status_code: int = 500
    code: str = "INTERNAL_ERROR"

    def __init__(self, message: str, details: list | None = None) -> None:
        self.message = message
        self.details = details or []
        super().__init__(message)


class ValidationError(AppError):
    status_code = 400
    code = "VALIDATION_ERROR"


class AuthenticationError(AppError):
    status_code = 401
    code = "AUTHENTICATION_ERROR"


class AuthorizationError(AppError):
    status_code = 403
    code = "AUTHORIZATION_ERROR"


class AIServiceError(AppError):
    status_code = 502
    code = "AI_SERVICE_ERROR"


class GitHubIntegrationError(AppError):
    status_code = 502
    code = "GITHUB_INTEGRATION_ERROR"


class FileProcessingError(AppError):
    status_code = 422
    code = "FILE_PROCESSING_ERROR"
