from typing import (
    Any,
)

from eth_utils import (
    is_address,
    is_canonical_address,
)

from ethpm.exceptions import (
    ValidationError,
)
from web3 import Web3


def validate_address(address: Any) -> None:
    """
    Raise a ValidationError if an address is not canonicalized.
    """
    if not is_address(address):
        raise ValidationError(f"Expected an address, got: {address}")
    if not is_canonical_address(address):
        raise ValidationError(
            "Py-EthPM library only accepts canonicalized addresses. "
            f"{address} is not in the accepted format."
        )


def validate_w3_instance(w3: Web3) -> None:
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
        raise ValidationError(
            f"Bytecode segment: [{offset}:{slot_length}] is not comprised of empty bytes, "
            f"rather: {slot}."
        )
