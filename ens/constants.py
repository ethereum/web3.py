from eth_typing import (
    ChecksumAddress,
    HexAddress,
    HexStr,
)
from hexbytes import (
    HexBytes,
)

ACCEPTABLE_STALE_HOURS = 48

AUCTION_START_GAS_CONSTANT = 25000
AUCTION_START_GAS_MARGINAL = 39000

EMPTY_SHA3_BYTES = HexBytes(b'\0' * 32)
EMPTY_ADDR_HEX = HexAddress(HexStr('0x' + '00' * 20))

REVERSE_REGISTRAR_DOMAIN = 'addr.reverse'

MAINNET_NET_VERSION = 1
ROPSTEN_NET_VERSION = 3
RINKEBY_NET_VERSION = 4
GOERLI_NET_VERSION = 5

NET_VERSION_TO_ENS_ADDR = {
    MAINNET_NET_VERSION:
        ChecksumAddress(HexAddress(HexStr('0x314159265dD8dbb310642f98f50C066173C1259b'))),
    ROPSTEN_NET_VERSION:
        ChecksumAddress(HexAddress(HexStr('0x112234455C3a32FD11230C42E7Bccd4A84e02010'))),
    RINKEBY_NET_VERSION:
        ChecksumAddress(HexAddress(HexStr('0xe7410170f87102DF0055eB195163A03B7F2Bff4A'))),
    GOERLI_NET_VERSION:
        ChecksumAddress(HexAddress(HexStr('0x112234455C3a32FD11230C42E7Bccd4A84e02010'))),
}
