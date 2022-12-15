from eth_utils import to_checksum_address, keccak
from eth_typing import ChecksumAddress, AnyAddress
from rlp import encode
from web3.types import Nonce


def get_create_address(sender: AnyAddress, nonce: Nonce) -> ChecksumAddress:
    """
    Determine the resulting `CREATE` opcode contract address for a sender and a nonce.

    NOTE: not for contracts deployed from `CREATE2` opcode.
    """
    contract_address = keccak(encode([bytes.fromhex(sender[2:]), nonce])).hex()[-40:]
    return to_checksum_address(contract_address)
