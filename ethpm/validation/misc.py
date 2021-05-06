from urllib import (
    parse,
)

from ethpm.exceptions import (
    EthPMValidationError,
)
from web3 import Web3


def validate_w3_instance(w3: "Web3") -> None:
    if w3 is None or not isinstance(w3, Web3):
        raise ValueError("Package does not have valid web3 instance.")


def validate_empty_bytes(offset: int, length: int, bytecode: bytes) -> None:
    """
    Validates that segment [`offset`:`offset`+`length`] of
    `bytecode` is comprised of empty bytes (b'\00').
    """
    slot_length = offset + length
    slot = bytecode[offset:slot_length]
    if slot != bytearray(length):
        raise EthPMValidationError(
            f"Bytecode segment: [{offset}:{slot_length}] "
            f"is not comprised of empty bytes, rather: {slot!r}."
        )


def validate_escaped_string(string: str) -> None:
    unsafe = parse.unquote(string)
    safe = parse.quote(unsafe)
    if string != safe:
        raise EthPMValidationError(
            f"String: {string} is not properly escaped, and contains url unsafe characters."
        )
