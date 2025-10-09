from typing import (
    Final,
)

from eth_typing import (
    ChecksumAddress,
    HexAddress,
    HexStr,
)
from faster_hexbytes import (
    HexBytes,
)

ACCEPTABLE_STALE_HOURS: Final = 48

AUCTION_START_GAS_CONSTANT: Final = 25000
AUCTION_START_GAS_MARGINAL: Final = 39000

EMPTY_SHA3_BYTES: Final = HexBytes(b"\0" * 32)
EMPTY_ADDR_HEX: Final = HexAddress(HexStr("0x" + "00" * 20))

REVERSE_REGISTRAR_DOMAIN: Final = "addr.reverse"

ENS_MAINNET_ADDR: Final = ChecksumAddress(
    HexAddress(HexStr("0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e"))
)


# --- interface ids --- #

ENS_ADDR_INTERFACE_ID: Final = HexStr("0x3b3b57de")
ENS_NAME_INTERFACE_ID: Final = HexStr("0x691f3431")
ENS_ABI_INTERFACE_ID: Final = HexStr("0x2203ab56")
ENS_PUBLIC_KEY_INTERFACE_ID: Final = HexStr("0xc8690233")
ENS_TEXT_INTERFACE_ID: Final = HexStr("0x59d1d43c")
ENS_CONTENT_HASH_INTERFACE_ID: Final = HexStr("0xbc1c58d1")
ENS_MULTICHAIN_ADDRESS_INTERFACE_ID: Final = HexStr("0xf1cb7e06")  # ENSIP-9
ENS_EXTENDED_RESOLVER_INTERFACE_ID: Final = HexStr("0x9061b923")  # ENSIP-10
