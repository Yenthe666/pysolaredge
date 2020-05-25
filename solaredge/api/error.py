class Error(Exception):
    """
        Base exception wrapper.
    """
    pass


class RequestError(Error):
    """Errors while preparing or performing an API request."""

    pass


class IdentifierError(RequestError):
    """
        Errors while preparing an API request (such as an invalid key).
    """

    pass
