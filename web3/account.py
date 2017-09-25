
import functools
import os

from cytoolz import (
    compose,
)

from eth_keys import KeyAPI

from eth_utils import (
    keccak,
)

import rlp

from web3.module import Module

from web3.utils.encoding import (
    to_bytes,
    to_decimal,
)
from web3.utils.signing import (
    signature_wrapper,
)


def return_key_api(to_wrap):
    @functools.wraps(to_wrap)
    def wrapper(*args, **kwargs):
        key = to_wrap(*args, **kwargs)
        sign = key.sign
        key.address = key.public_key.to_checksum_address()
        key.privateKey = key
        key.sign = compose(sign, signature_wrapper, to_bytes)
        key.signTransaction = compose(sign, to_bytes)
        return key
    return wrapper


class Account(Module):
    _keys = KeyAPI()

    def create(self, extra_entropy=''):
        extra_key_bytes = to_bytes(text=extra_entropy)
        key_bytes = keccak(os.urandom(32) + extra_key_bytes)
        return self.privateKeyToAccount(key_bytes)

    @return_key_api
    def privateKeyToAccount(self, primitive=None, hexstr=None):
        key_bytes = to_bytes(primitive, hexstr=hexstr)
        if len(key_bytes) != 32:
            raise ValueError(
                "The private key must be exactly 32 bytes long, instead of "
                "%d bytes." % len(key_bytes)
            )
        return self._keys.PrivateKey(key_bytes)

    def recoverTransaction(self, primitive=None, hexstr=None):
        raw_tx = to_bytes(primitive, hexstr=hexstr)
        tx_parts = rlp.decode(raw_tx)
        unsigned_parts = tx_parts[:-3]
        raw_v, r, s = map(to_decimal, tx_parts[-3:])
        if raw_v < 2:
            v = raw_v
        else:
            v = to_decimal(raw_v % 2 == 0)  # dark magic from https://github.com/MaiaVictor/eth-lib/blob/862bf8c504bd001d482564bea3921486a04798eb/src/account.js#L58
            if raw_v >= 35:
                # dark magic from https://github.com/MaiaVictor/eth-lib/blob/862bf8c504bd001d482564bea3921486a04798eb/src/account.js#L88
                unsigned_parts += [to_bytes((raw_v - 35) >> 1), b'', b'']
        pubkey = self._keys.Signature(vrs=(v, r, s)).recover_msg(rlp.encode(unsigned_parts))
        return pubkey.to_checksum_address()

    def setKeyBackend(self, backend):
        self._keys = KeyAPI(backend)
