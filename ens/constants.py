from typing import (
    cast,
)

from eth_typing import (
    Address,
)
from hexbytes import (
    HexBytes,
)

ACCEPTABLE_STALE_HOURS = 48

AUCTION_START_GAS_CONSTANT = 25000
AUCTION_START_GAS_MARGINAL = 39000

EMPTY_SHA3_BYTES = cast(HexBytes, b'\0' * 32)
EMPTY_ADDR_HEX = cast(Address, '0x' + '00' * 20)

REVERSE_REGISTRAR_DOMAIN = 'addr.reverse'
