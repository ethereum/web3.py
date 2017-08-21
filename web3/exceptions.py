class BadFunctionCallOutput(Exception):
    """
    We failed to decode ABI output.

    Most likely ABI mismatch.
    """
    pass


class CannotHandleRequest(Exception):
    """
    Raised by a provider to signal that it cannot handle an RPC request and
    that the manager should proceed to the next provider.
    """
    pass


class UnhandledRequest(Exception):
    """
    Raised by the manager when none of it's providers responds to a request.
    """
    pass
