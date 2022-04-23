from typing import (
    Union,
)

from eth_typing import (
    HexStr,
)
from eth_utils import (
    to_bytes,
    to_hex,
)


def to_hex_if_bytes(val: Union[str, bytes]) -> HexStr:
    return to_hex(val) if isinstance(val, (bytes, bytearray)) else to_hex(hexstr=val)


def to_bytes_if_hex(val: Union[HexStr, str, bytes]) -> bytes:
    return to_bytes(hexstr=val) if isinstance(val, str) else val
