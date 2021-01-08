import re
from typing import (
    TYPE_CHECKING,
    Any,
    Tuple,
)
from urllib import (
    parse,
)

from eth_typing import (
    URI,
    BlockNumber,
    HexStr,
)
from eth_utils import (
    add_0x_prefix,
    is_integer,
    remove_0x_prefix,
)
from hexbytes import (
    HexBytes,
)

from ethpm.constants import (
    SUPPORTED_CHAIN_IDS,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def get_genesis_block_hash(web3: "Web3") -> HexBytes:
    return web3.eth.get_block(BlockNumber(0))["hash"]


BLOCK = "block"

BIP122_URL_REGEX = (
    "^"
    "blockchain://"
    "(?P<chain_id>[a-zA-Z0-9]{64})"
    "/"
    "(?P<resource_type>block|transaction)"
    "/"
    "(?P<resource_hash>[a-zA-Z0-9]{64})"
    "$"
)


def is_BIP122_uri(value: URI) -> bool:
    return bool(re.match(BIP122_URL_REGEX, value))


def parse_BIP122_uri(blockchain_uri: URI) -> Tuple[HexStr, str, HexStr]:
    match = re.match(BIP122_URL_REGEX, blockchain_uri)
    if match is None:
        raise ValueError(f"Invalid URI format: '{blockchain_uri}'")
    chain_id, resource_type, resource_hash = match.groups()
    return (add_0x_prefix(HexStr(chain_id)), resource_type, add_0x_prefix(HexStr(resource_hash)))


def is_BIP122_block_uri(value: URI) -> bool:
    if not is_BIP122_uri(value):
        return False
    _, resource_type, _ = parse_BIP122_uri(value)
    return resource_type == BLOCK


BLOCK_OR_TRANSACTION_HASH_REGEX = "^(?:0x)?[a-zA-Z0-9]{64}$"


def is_block_or_transaction_hash(value: str) -> bool:
    return bool(re.match(BLOCK_OR_TRANSACTION_HASH_REGEX, value))


def create_BIP122_uri(
    chain_id: HexStr, resource_type: str, resource_identifier: HexStr
) -> URI:
    """
    See: https://github.com/bitcoin/bips/blob/master/bip-0122.mediawiki
    """
    if resource_type != BLOCK:
        raise ValueError("Invalid resource_type.  Must be one of 'block'")
    elif not is_block_or_transaction_hash(resource_identifier):
        raise ValueError(
            "Invalid resource_identifier.  Must be a hex encoded 32 byte value"
        )
    elif not is_block_or_transaction_hash(chain_id):
        raise ValueError("Invalid chain_id.  Must be a hex encoded 32 byte value")

    return URI(
        parse.urlunsplit(
            [
                "blockchain",
                remove_0x_prefix(chain_id),
                f"{resource_type}/{remove_0x_prefix(resource_identifier)}",
                "",
                "",
            ]
        )
    )


def create_block_uri(chain_id: HexStr, block_identifier: HexStr) -> URI:
    return create_BIP122_uri(chain_id, "block", remove_0x_prefix(block_identifier))


def is_supported_chain_id(chain_id: Any) -> bool:
    if not is_integer(chain_id):
        return False

    if chain_id not in SUPPORTED_CHAIN_IDS.keys():
        return False
    return True
