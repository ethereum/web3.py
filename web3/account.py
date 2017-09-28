
from collections import (
    Mapping,
)
import functools
import os
import sys

from cytoolz import (
    compose,
    pipe,
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

from web3.utils.datastructures import (
    AttributeDict,
)
from web3.utils.encoding import (
    to_bytes,
    to_decimal,
    to_hex,
    to_hex_with_size,
)
from web3.utils.exception import (
    raise_from,
)
from web3.utils.signing import (
    annotate_transaction_with_chain_id,
    signature_wrapper,
    sign_transaction_hash,
)
from web3.utils.transactions import (
    encode_transaction,
    serializable_unsigned_transaction,
)


def return_key_api(to_wrap):
    @functools.wraps(to_wrap)
    def wrapper(*args, **kwargs):
        key = to_wrap(*args, **kwargs)
        sign = key.sign_msg
        key.address = key.public_key.to_checksum_address()
        key.privateKey = key.to_bytes()
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

    @staticmethod
    def hashMessage(data=None, hexstr=None, text=None):
        message_bytes = to_bytes(data, hexstr=hexstr, text=text)
        recovery_hasher = compose(to_hex, keccak, signature_wrapper)
        return recovery_hasher(message_bytes)

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

    def recover(self, msghash=None, msghash_hexstr=None, vrs=None, signature_bytes=None):
        hash_bytes = to_bytes(msghash, hexstr=msghash_hexstr)
        if vrs:
            vrs_raw = (vrs[0] - 27, ) + vrs[1:]
            signature = self._keys.Signature(vrs=vrs_raw)
        else:
            signature = self._keys.Signature(signature_bytes=signature_bytes)
        pubkey = signature.recover_public_key_from_msg_hash(hash_bytes)
        return pubkey.to_checksum_address()

    def recoverTransaction(self, primitive=None, hexstr=None):
        raw_tx = to_bytes(primitive, hexstr=hexstr)
        # TODO move to a new transaction handler
        tx_parts = rlp.decode(raw_tx)
        unsigned_parts = tx_parts[:-3]
        raw_v, r, s = map(to_decimal, tx_parts[-3:])
        (chain_aware_tx, _chain_id, v) = annotate_transaction_with_chain_id(unsigned_parts, raw_v)
        message_hash = keccak(rlp.encode(chain_aware_tx))
        return self.recover(message_hash, vrs=(v, r, s))

    def setKeyBackend(self, backend):
        self._keys = KeyAPI(backend)

    def sign(self, message=None, private_key=None, message_hexstr=None, message_text=None):
        '''
        @param private_key in bytes, str, or int.
            In Python 2, a bytes, unicode or str object will be interpreted as hexstr
            In Python 3, only a str object will be interpreted as hexstr
        '''
        msg_bytes = to_bytes(message, hexstr=message_hexstr, text=message_text)
        msg_hash = self.hashMessage(msg_bytes)
        if isinstance(private_key, str) or (
                sys.version_info.major < 3 and isinstance(private_key, unicode)  # noqa: F821
            ):
            key_bytes = to_bytes(hexstr=private_key)
        else:
            key_bytes = to_bytes(private_key)
        key = self._keys.PrivateKey(key_bytes)
        # TODO move to a new signature handler
        signature = key.sign_msg_hash(to_bytes(hexstr=msg_hash))
        (r, s, v_raw) = (getattr(signature, part) for part in 'rsv')
        v = v_raw + 27
        eth_signature_bytes = b''.join(map(to_bytes, (r, s, v)))
        (r_hex, s_hex, eth_signature_hex) = map(to_hex, (r, s, eth_signature_bytes))
        return AttributeDict({
            'message': msg_bytes,
            'messageHash': msg_hash,
            'r': r_hex,
            's': s_hex,
            'v': v,
            'signature': eth_signature_hex,
        })

    def signTransaction(self, transaction_dict, private_key):
        '''
        @param private_key in bytes, str, or int.
            In Python 2, a bytes, unicode or str object will be interpreted as hexstr
            In Python 3, only a str object will be interpreted as hexstr
        '''
        assert isinstance(transaction_dict, Mapping)

        # build private key
        if isinstance(private_key, str) or (
                sys.version_info.major < 3 and isinstance(private_key, unicode)  # noqa: F821
            ):
            key_bytes = to_bytes(hexstr=private_key)
        else:
            key_bytes = to_bytes(private_key)
        account = self.privateKeyToAccount(key_bytes)

        # detect nonce for this account
        if 'nonce' not in transaction_dict:
            transaction_dict['nonce'] = self.web3.eth.getTransactionCount(account.address)

        unsigned_transaction = serializable_unsigned_transaction(self.web3, transaction_dict)

        transaction_hash = pipe(unsigned_transaction, rlp.encode, keccak)

        chain_id = unsigned_transaction.v
        (v, r, s) = sign_transaction_hash(account, transaction_hash, chain_id)

        encoded_transaction = encode_transaction(unsigned_transaction, vrs=(v, r, s))

        # format most returned elements as hex
        signature_info = {
            key: to_hex_with_size(val, 256)
            for key, val
            in (
                ('rawTransaction', encoded_transaction),
                ('hash', transaction_hash),
                ('r', r),
                ('s', s),
            )
        }
        signature_info['v'] = v
        return AttributeDict(signature_info)
