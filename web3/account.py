
import functools
import os

from cytoolz import (
    compose,
)

from eth_keys import KeyAPI
from eth_utils import (
    keccak,
)

from web3.module import Module

from web3.utils.encoding import (
    to_bytes,
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

    def setKeyBackend(self, backend):
        self._keys = KeyAPI(backend)
