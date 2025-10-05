from typing import (
    Final,
    Union,
)

import faster_eth_utils
from eth_typing import (
    HexStr,
)

from faster_web3.exceptions import (
    Web3ValueError,
)


to_bytes: Final = faster_eth_utils.to_bytes
to_hex: Final = faster_eth_utils.to_hex


def to_hex_if_bytes(val: Union[HexStr, str, bytes, bytearray]) -> HexStr:
    """
    Note: This method does not validate against all cases and is only
    meant to work with bytes and hex strings.
    """
    if isinstance(val, str):
        if not val.startswith("0x"):
            raise Web3ValueError(f"Expected a hex string. Got: {val!r}")
        return to_hex(hexstr=val)

    return to_hex(val) if isinstance(val, (bytes, bytearray)) else to_hex(hexstr=val)


def to_bytes_if_hex(val: Union[HexStr, str, bytes, bytearray]) -> bytes:
    """
    Note: This method does not validate against all cases and is only
    meant to work with bytes and hex strings.
    """
    return to_bytes(hexstr=val) if isinstance(val, str) else val
