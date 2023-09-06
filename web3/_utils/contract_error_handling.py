import warnings

from eth_abi import (
    abi,
)
from eth_utils import (
    to_bytes,
)

from web3.exceptions import (
    ContractCustomError,
    ContractLogicError,
    ContractPanicError,
    OffchainLookup,
)
from web3.types import (
    RPCResponse,
)

# func selector for "Error(string)"
SOLIDITY_ERROR_FUNC_SELECTOR = "0x08c379a0"

# --- CCIP Read - EIP-3668 --- #
# the first 4 bytes of keccak hash (func selector) for:
# "OffchainLookup(address,string[],bytes,bytes4,bytes)"
OFFCHAIN_LOOKUP_FUNC_SELECTOR = "0x556f1830"
OFFCHAIN_LOOKUP_FIELDS = {
    "sender": "address",
    "urls": "string[]",
    "callData": "bytes",
    "callbackFunction": "bytes4",
    "extraData": "bytes",
}


# --- Solidity Panic Error, as of Solidity 0.8.0 --- #
PANIC_ERROR_FUNC_SELECTOR = "0x4e487b71"
PANIC_ERROR_CODES = {
    "00": "Panic error 0x00: Generic compiler inserted panics.",
    "01": "Panic error 0x01: Assert evaluates to false.",
    "11": "Panic error 0x11: Arithmetic operation results in underflow or overflow.",
    "12": "Panic error 0x12: Division by zero.",
    "21": "Panic error 0x21: Cannot convert value into an enum type.",
    "22": "Panic error 0x12: Storage byte array is incorrectly encoded.",
    "31": "Panic error 0x31: Call to 'pop()' on an empty array.",
    "32": "Panic error 0x32: Array index is out of bounds.",
    "41": "Panic error 0x41: Allocation of too much memory or array too large.",
    "51": "Panic error 0x51: Call to a zero-initialized variable of internal "
    "function type.",
}

MISSING_DATA = "no data"


def _parse_openethereum_hex_error(data: str) -> str:
    """
    Parse Parity/OpenEthereum error from the data.
    "Reverted", function selector and offset are always the same for revert errors
    """
    prefix = f"Reverted {SOLIDITY_ERROR_FUNC_SELECTOR}"
    data_offset = ("00" * 31) + "20"  # 0x0000...0020 (32 bytes)
    revert_pattern = prefix + data_offset
    error = data

    if data.startswith(revert_pattern):
        # if common revert pattern
        string_length = int(data[len(revert_pattern) : len(revert_pattern) + 64], 16)
        error = data[
            len(revert_pattern) + 64 : len(revert_pattern) + 64 + string_length * 2
        ]
    elif data.startswith("Reverted 0x"):
        # Special case for this form: 'Reverted 0x...'
        error = data.split(" ")[1][2:]

    return error


def _raise_error_from_decoded_revert_data(data: str) -> None:
    """
    Decode response error data and raise appropriate exception.
    """
    if data.startswith("Reverted "):
        try:
            reason_string = bytes.fromhex(_parse_openethereum_hex_error(data)).decode(
                "utf8"
            )
        except UnicodeDecodeError:
            warnings.warn("Could not decode revert reason as UTF-8", RuntimeWarning)
            raise ContractLogicError("execution reverted", data=data)

        raise ContractLogicError(f"execution reverted: {reason_string}", data=data)

    if data[:10] == OFFCHAIN_LOOKUP_FUNC_SELECTOR:
        parsed_data_as_bytes = to_bytes(hexstr=data[10:])
        abi_decoded_data = abi.decode(
            list(OFFCHAIN_LOOKUP_FIELDS.values()), parsed_data_as_bytes
        )
        offchain_lookup_payload = dict(
            zip(OFFCHAIN_LOOKUP_FIELDS.keys(), abi_decoded_data)
        )
        raise OffchainLookup(offchain_lookup_payload, data=data)

    if data[:10] == PANIC_ERROR_FUNC_SELECTOR:
        panic_error_code = data[-2:]
        raise ContractPanicError(PANIC_ERROR_CODES[panic_error_code], data=data)

    # Solidity 0.8.4 introduced custom error messages that allow args to
    # be passed in (or not). See:
    # https://blog.soliditylang.org/2021/04/21/custom-errors/
    if len(data) >= 10 and not data[:10] == SOLIDITY_ERROR_FUNC_SELECTOR:
        # Raise with data as both the message and the data for backwards
        # compatibility and so that data can be accessed via 'data' attribute
        # on the ContractCustomError exception
        raise ContractCustomError(data, data=data)


def raise_contract_logic_error_on_revert(response: RPCResponse) -> RPCResponse:
    """
    Reverts contain a `data` attribute with the following layout:
        "Reverted "
        Function selector for Error(string): 08c379a (4 bytes)
        Data offset: 32 (32 bytes)
        String length (32 bytes)
        Reason string (padded, use string length from above to get meaningful part)

    See also https://solidity.readthedocs.io/en/v0.6.3/control-structures.html#revert
    """
    error = response.get("error")
    if error is None or isinstance(error, str):
        raise ValueError(error)

    code = error.get("code")
    message = error.get("message")
    message_present = message is not None and message != ""
    data = error.get("data", MISSING_DATA)

    if message_present:
        if data is None:
            raise ContractLogicError(message, data=data)
        elif isinstance(data, dict):
            raise ContractLogicError(f"execution reverted: {message}", data=data)
        elif code == 3:
            # Geth Revert with error message and code 3 case:
            raise ContractLogicError(message, data=data)
        elif "execution reverted" in message:
            raise ContractLogicError("execution reverted", data=data)

    if data is None and not message_present:
        raise ContractLogicError("execution reverted", data=data)

    _raise_error_from_decoded_revert_data(data)

    return response
