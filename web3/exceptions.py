import datetime
import time


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


class StaleBlockchain(Exception):
    """
    Raised by the stalecheck_middleware when the latest block is too old.
    """
    def __init__(self, block, allowable_delay):
        last_block_date = datetime.datetime.fromtimestamp(block.timestamp).strftime('%c')
        message = (
            "The latest block, #%d, is %d seconds old, but is only allowed to be %d s old. "
            "The date of the most recent block is %s. Continue syncing and try again..." %
            (block.number, time.time() - block.timestamp, allowable_delay, last_block_date)
        )
        super().__init__(message, block, allowable_delay)

    def __str__(self):
        return self.args[0]
