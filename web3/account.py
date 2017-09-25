
import functools
import os

from cytoolz import (
    compose,
)

from eth_keys import (
    KeyAPI,
    keys,
)
from eth_keys.exceptions import (
    ValidationError,
)

from eth_utils import (
    keccak,
)

import rlp

from web3.module import Module

from web3.utils.encoding import (
    to_bytes,
    to_decimal,
)
from web3.utils.exception import (
    raise_from,
)
from web3.utils.signing import (
    annotate_transaction_with_chain_id,
    signature_wrapper,
)


def return_key_api(to_wrap):
    @functools.wraps(to_wrap)
    def wrapper(*args, **kwargs):
        key = to_wrap(*args, **kwargs)
        sign = key.sign_msg
        key.address = key.public_key.to_checksum_address()
        key.privateKey = key
        key.sign = compose(sign, signature_wrapper, to_bytes)
        key.signTransaction = compose(sign, to_bytes)
        return key
    return wrapper


class Account(Module):
    _keys = keys

    def create(self, extra_entropy=''):
        extra_key_bytes = to_bytes(text=extra_entropy)
        key_bytes = keccak(os.urandom(32) + extra_key_bytes)
        return self.privateKeyToAccount(key_bytes)

    @return_key_api
    def privateKeyToAccount(self, primitive=None, hexstr=None):
        key_bytes = to_bytes(primitive, hexstr=hexstr)
        try:
            return self._keys.PrivateKey(key_bytes)
        except ValidationError as original_exception:
            raise_from(
                ValueError(
                    "The private key must be exactly 32 bytes long, instead of "
                    "%d bytes." % len(key_bytes)
                ),
                original_exception
            )

    def recoverTransaction(self, primitive=None, hexstr=None):
        raw_tx = to_bytes(primitive, hexstr=hexstr)
        tx_parts = rlp.decode(raw_tx)
        unsigned_parts = tx_parts[:-3]
        raw_v, r, s = map(to_decimal, tx_parts[-3:])
        (chain_aware_tx, _chain_id, v) = annotate_transaction_with_chain_id(unsigned_parts, raw_v)
        signature = self._keys.Signature(vrs=(v, r, s))
        pubkey = signature.recover_public_key_from_msg(rlp.encode(chain_aware_tx))
        return pubkey.to_checksum_address()

    def setKeyBackend(self, backend):
        self._keys = KeyAPI(backend)
