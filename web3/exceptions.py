import datetime
import time
from typing import (
    Any,
    Dict,
)

from web3.types import (
    BlockData,
)


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


class TooManyRequests(Exception):
    """
    Raised by a provider to signal that too many requests have been made consecutively.
    """

    pass


class MultipleFailedRequests(Exception):
    """
    Raised by a provider to signal that multiple requests to retrieve the same
    (or similar) data have failed.
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

    def __init__(self, block: BlockData, allowable_delay: int) -> None:
        last_block_date = datetime.datetime.fromtimestamp(block["timestamp"]).strftime(
            "%c"
        )
        message = (
            f"The latest block, #{block['number']}, is "
            f"{time.time() - block['timestamp']} seconds old, but is only "
            f"allowed to be {allowable_delay} s old. "
            f"The date of the most recent block is {last_block_date}. Continue "
            "syncing and try again..."
        )
        super().__init__(message, block, allowable_delay)

    def __str__(self) -> str:
        return self.args[0]


class MismatchedABI(Exception):
    """
    Raised when an ABI does not match with supplied parameters, or when an
    attempt is made to access a function/event that does not exist in the ABI.
    """

    pass


class ABIEventFunctionNotFound(AttributeError, MismatchedABI):
    """
    Raised when an attempt is made to access an event
    that does not exist in the ABI.
    """

    pass


class ABIFunctionNotFound(AttributeError, MismatchedABI):
    """
    Raised when an attempt is made to access a function
    that does not exist in the ABI.
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


class ExtraDataLengthError(ValidationError):
    """
    Raised when an RPC call returns >32 bytes of extraData.
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
    Raised when a method has not retrieved the desired
    result within a specified timeout.
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


class InfuraProjectIdNotFound(Exception):
    """
    Raised when there is no Infura Project Id set.
    """

    pass


class LogTopicError(ValueError):
    # Inherits from ValueError for backwards compatibility
    """
    Raised when the number of log topics is mismatched.
    """
    pass


class InvalidEventABI(ValueError):
    # Inherits from ValueError for backwards compatibility
    """
    Raised when the event ABI is invalid.
    """
    pass


class ContractLogicError(ValueError):
    # Inherits from ValueError for backwards compatibility
    """
    Raised on a contract revert error
    """


class OffchainLookup(ContractLogicError):
    """
    Raised when a contract reverts with OffchainLookup as described in EIP-3668
    """

    def __init__(self, payload: Dict[str, Any]) -> None:
        self.payload = payload
        super().__init__()


class InvalidTransaction(Exception):
    """
    Raised when a transaction includes an invalid combination of arguments.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class TransactionTypeMismatch(InvalidTransaction):
    """
    Raised when legacy transaction values are used alongside dynamic
    fee (EIP-1559) transaction values.
    """

    def __init__(self) -> None:
        message = "Found legacy and EIP 1559 transaction values."
        super().__init__(message)


class BadResponseFormat(ValueError, KeyError):
    # Inherits from KeyError and ValueError for backwards compatibility
    """
    Raised when a JSON-RPC response comes back in an unexpected format
    """
    pass
