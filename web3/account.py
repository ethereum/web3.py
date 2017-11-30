from collections import (
    Mapping,
)
import json
import os

from cytoolz import (
    compose,
)

from eth_keyfile import (
    create_keyfile_json,
    decode_keyfile_json,
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
    is_dict,
)

from web3.utils.datastructures import (
    AttributeDict,
    HexBytes,
)
from web3.utils.decorators import (
    combomethod,
)
from web3.utils.encoding import (
    hexstr_if_str,
    text_if_str,
    to_bytes,
    to_int,
)
from web3.utils.signing import (
    LocalAccount,
    hash_of_signed_transaction,
    sign_message_hash,
    sign_transaction_dict,
    signature_wrapper,
    to_standard_signature_bytes,
    to_standard_v,
)
from web3.utils.transactions import (
    Transaction,
    vrs_from,
)


class Account(object):
    _keys = keys

    @combomethod
    def create(self, extra_entropy=''):
        extra_key_bytes = text_if_str(to_bytes, extra_entropy)
        key_bytes = keccak(os.urandom(32) + extra_key_bytes)
        return self.privateKeyToAccount(key_bytes)

    @staticmethod
    def decrypt(keyfile_json, password):
        if isinstance(keyfile_json, str):
            keyfile = json.loads(keyfile_json)
        elif is_dict(keyfile_json):
            keyfile = keyfile_json
        else:
            raise TypeError("The keyfile should be supplied as a JSON string, or a dictionary.")
        password_bytes = text_if_str(to_bytes, password)
        return decode_keyfile_json(keyfile, password_bytes)

    @staticmethod
    def encrypt(private_key, password):
        key_bytes = HexBytes(private_key)
        password_bytes = text_if_str(to_bytes, password)
        assert len(key_bytes) == 32
        return create_keyfile_json(key_bytes, password_bytes)

    @staticmethod
    def hashMessage(data=None, hexstr=None, text=None):
        message_bytes = to_bytes(data, hexstr=hexstr, text=text)
        recovery_hasher = compose(HexBytes, keccak, signature_wrapper)
        return recovery_hasher(message_bytes)

    @combomethod
    def privateKeyToAccount(self, private_key):
        key_bytes = HexBytes(private_key)
        try:
            key_obj = self._keys.PrivateKey(key_bytes)
            return LocalAccount(key_obj, self)
        except ValidationError as original_exception:
            raise ValueError(
                "The private key must be exactly 32 bytes long, instead of "
                "%d bytes." % len(key_bytes)
            ) from original_exception

    @combomethod
    def recover(self, msghash, vrs=None, signature=None):
        hash_bytes = HexBytes(msghash)
        if vrs is not None:
            v, r, s = map(hexstr_if_str(to_int), vrs)
            v_standard = to_standard_v(v)
            signature_obj = self._keys.Signature(vrs=(v_standard, r, s))
        elif signature is not None:
            signature_bytes = HexBytes(signature)
            signature_bytes_standard = to_standard_signature_bytes(signature_bytes)
            signature_obj = self._keys.Signature(signature_bytes=signature_bytes_standard)
        else:
            raise TypeError("You must supply the vrs tuple or the signature bytes")
        pubkey = signature_obj.recover_public_key_from_msg_hash(hash_bytes)
        return pubkey.to_checksum_address()

    @combomethod
    def recoverMessage(self, data=None, hexstr=None, text=None, vrs=None, signature=None):
        msg_hash = self.hashMessage(data, hexstr=hexstr, text=text)
        return self.recover(msg_hash, vrs=vrs, signature=signature)

    @combomethod
    def recoverTransaction(self, serialized_transaction):
        txn_bytes = HexBytes(serialized_transaction)
        txn = Transaction.from_bytes(txn_bytes)
        msg_hash = hash_of_signed_transaction(txn)
        return self.recover(msg_hash, vrs=vrs_from(txn))

    def setKeyBackend(self, backend):
        self._keys = KeyAPI(backend)

    @combomethod
    def sign(self, message=None, private_key=None, message_hexstr=None, message_text=None):
        '''
        @param private_key in bytes, str, or int.
        '''
        msg_bytes = to_bytes(message, hexstr=message_hexstr, text=message_text)
        msg_hash = self.hashMessage(msg_bytes)
        key_bytes = HexBytes(private_key)
        key = self._keys.PrivateKey(key_bytes)
        (v, r, s, eth_signature_bytes) = sign_message_hash(key, msg_hash)
        return AttributeDict({
            'message': HexBytes(msg_bytes),
            'messageHash': msg_hash,
            'r': r,
            's': s,
            'v': v,
            'signature': HexBytes(eth_signature_bytes),
        })

    @combomethod
    def signTransaction(self, transaction_dict, private_key):
        '''
        @param private_key in bytes, str, or int.
        '''
        assert isinstance(transaction_dict, Mapping)

        account = self.privateKeyToAccount(private_key)

        # sign transaction
        (
            v,
            r,
            s,
            rlp_encoded,
        ) = sign_transaction_dict(account._key_obj, transaction_dict)

        transaction_hash = keccak(rlp_encoded)

        return AttributeDict({
            'rawTransaction': HexBytes(rlp_encoded),
            'hash': HexBytes(transaction_hash),
            'r': r,
            's': s,
            'v': v,
        })
