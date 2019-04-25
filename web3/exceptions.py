import datetime
import time


class BadFunctionCallOutput(Exception):
    """
    We failed to decode ABI output.

    Most likely ABI mismatch.
    """
    pass


class BlockNumberOutofRange(Exception):
    """
    block_identifier passed does not match known block.
    """
    pass


class CannotHandleRequest(Exception):
    """
    Raised by a provider to signal that it cannot handle an RPC request and
    that the manager should proceed to the next provider.
    """
    pass


class InvalidAddress(ValueError):
    """
    The supplied address does not have a valid checksum, as defined in EIP-55
    """
    pass


class NameNotFound(ValueError):
    """
    Raised when a caller provides an Ethereum Name Service name that
    does not resolve to an address.
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


class MismatchedABI(Exception):
    """
    Raised when an ABI does not match with supplied parameters, or when an
    attempt is made to access a function/event that does not exist in the ABI.
    """
    pass


class FallbackNotFound(Exception):
    """
    Raised when fallback function doesn't exist in contract.
    """
    pass


class ValidationError(Exception):
    """
    Raised when a supplied value is invalid.
    """
    pass


class NoABIFunctionsFound(AttributeError):
    """
    Raised when an ABI is present, but doesn't contain any functions.
    """
    pass


class NoABIFound(AttributeError):
    """
    Raised when no ABI is present.
    """
    pass


class NoABIEventsFound(AttributeError):
    """
    Raised when an ABI doesn't contain any events.
    """
    pass


class InsufficientData(Exception):
    """
    Raised when there are insufficient data points to
    complete a calculation
    """
    pass


class TimeExhausted(Exception):
    """
    Raised when a method has not retrieved the desired result within a specified timeout.
    """
    pass


class PMError(Exception):
    """
    Raised when an error occurs in the PM module.
    """
    pass


class ManifestValidationError(PMError):
    """
    Raised when a provided manifest cannot be published, since it's invalid.
    """
    pass


class TransactionNotFound(Exception):
    """
    Raised when a tx hash used to lookup a tx in a jsonrpc call cannot be found.
    """
    pass


class BlockNotFound(Exception):
    """
    Raised when the block id used to lookup a block in a jsonrpc call cannot be found.
    """
    pass


class InfuraKeyNotFound(Exception):
    """
    Raised when there is no Infura Project Id set.
    """
    pass
