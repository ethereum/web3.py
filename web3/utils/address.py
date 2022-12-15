from eth_typing import (
    ChecksumAddress,
    HexAddress,
)
from eth_utils import (
    keccak,
    to_checksum_address,
)
from rlp import (
    encode,
)

from web3.types import (
    HexStr,
    Nonce,
)


def get_create_address(sender: HexAddress, nonce: Nonce) -> ChecksumAddress:
    """
    Determine the resulting `CREATE` opcode contract address for a sender and a nonce.
    """
    bytes_sender = bytes.fromhex(sender[2:])

    contract_address = keccak(encode([bytes_sender, nonce])).hex()[-40:]
    return to_checksum_address(contract_address)


def get_create2_address(
    sender: HexAddress, salt: HexStr, init_code: HexStr
) -> ChecksumAddress:
    """
    Determine the resulting `CREATE2` opcode contract address for a sender, salt and
    bytecode.
    """
    bytes_prefix = bytes.fromhex("0xFF"[2:])
    bytes_sender = bytes.fromhex(sender[2:])
    bytes_salt = bytes.fromhex(salt[2:])
    bytes_init_code = bytes.fromhex(init_code[2:])

    contract_address = keccak(
        bytes_prefix + bytes_sender + bytes_salt + keccak(bytes_init_code)
    ).hex()[-40:]
    return to_checksum_address(contract_address)
