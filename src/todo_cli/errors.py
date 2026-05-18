class TodoCliError(Exception):
    """Base error for user-facing CLI failures."""


class ValidationError(TodoCliError):
    pass


class NotFoundError(TodoCliError):
    pass
