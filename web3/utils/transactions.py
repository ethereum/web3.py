import random

import gevent

import rlp
from rlp.sedes import big_endian_int, binary, Binary
from rlp.utils import int_to_big_endian

from .encoding import (
    to_decimal,
    decode_hex,
    decode_big_endian_int,
)
from .string import (
    force_bytes,
    coerce_args_to_bytes,
)
from .types import (
    is_string,
)
from .crypto import (
    sha3,
)
from .address import (
    to_address,
)
from .formatting import (
    pad_left,
)


def wait_for_transaction_receipt(web3, txn_hash, timeout=120):
    with gevent.Timeout(timeout):
        while True:
            txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
            if txn_receipt is not None:
                break
            gevent.sleep(random.random())
    return txn_receipt


def get_block_gas_limit(web3, block_identifier=None):
    if block_identifier is None:
        block_identifier = web3.eth.blockNumber
    block = web3.eth.getBlock(block_identifier)
    return block['gasLimit']


def get_buffered_gas_estimate(web3, transaction, gas_buffer=100000):
    gas_estimate_transaction = dict(**transaction)

    gas_estimate = web3.eth.estimateGas(gas_estimate_transaction)

    gas_limit = get_block_gas_limit(web3)

    if gas_estimate > gas_limit:
        raise ValueError(
            "Contract does not appear to be delpoyable within the "
            "current network gas limits.  Estimated: {0}. Current gas "
            "limit: {1}".format(gas_estimate, gas_limit)
        )

    return min(gas_limit, gas_estimate + gas_buffer)


def is_secp256k1_available():
    try:
        import secp256k1  # noqa
    except ImportError:
        return False
    else:
        return True


def is_bitcoin_available():
    try:
        import bitcoin  # noqa
    except ImportError:
        return False
    else:
        return True


# in the yellow paper it is specified that s should be smaller than secpk1n (eq.205)
secpk1n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
TT256 = 2 ** 256


address_sedes = Binary.fixed_length(20, allow_empty=True)


class Transaction(rlp.Serializable):
    """
    # Derived from `pyethereum.transaction.Transaction`

    A transaction is stored as:
    [nonce, gasprice, startgas, to, value, data, v, r, s]

    nonce is the number of transactions already sent by that account, encoded
    in binary form (eg.  0 -> '', 7 -> '\x07', 1000 -> '\x03\xd8').

    (v,r,s) is the raw Electrum-style signature of the transaction without the
    signature made with the private key corresponding to the sending account,
    with 0 <= v <= 3. From an Electrum-style signature (65 bytes) it is
    possible to extract the public key, and thereby the address, directly.

    A valid transaction is one where:
    (i) the signature is well-formed (ie. 0 <= v <= 3, 0 <= r < P, 0 <= s < N,
        0 <= r < P - N if v >= 2), and
    (ii) the sending account has enough funds to pay the fee and the value.
    """

    fields = [
        ('nonce', big_endian_int),
        ('gasprice', big_endian_int),
        ('startgas', big_endian_int),
        ('to', address_sedes),
        ('value', big_endian_int),
        ('data', binary),
        ('v', big_endian_int),
        ('r', big_endian_int),
        ('s', big_endian_int),
    ]

    _sender = None

    def __init__(self, nonce, gasprice, startgas, to, value, data, v=0, r=0, s=0):
        self.data = None

        to = decode_hex(to_address(to))
        assert len(to) == 20 or len(to) == 0
        super(Transaction, self).__init__(nonce, gasprice, startgas, to, value, data, v, r, s)

        if self.gasprice >= TT256 or self.startgas >= TT256 or \
                self.value >= TT256 or self.nonce >= TT256:
            raise ValueError("Values way too high!")

    @property
    def sender(self):
        if not self._sender:
            if not is_bitcoin_available() or not is_secp256k1_available():
                raise ImportError(
                    "In order to derive the sender for transactions the "
                    "`bitcoin` and `secp256k1` packages must be installed."
                )
            from bitcoin import N
            from secp256k1 import PublicKey, ALL_FLAGS

            # Determine sender
            if self.v:
                has_invalid_signature_values = (
                    self.r >= N or
                    self.s >= N or
                    self.v < 27 or
                    self.v > 28 or
                    self.r == 0 or
                    self.s == 0
                )
                if has_invalid_signature_values:
                    raise ValueError("Invalid signature values!")
                rlpdata = rlp.encode(self, UnsignedTransaction)
                rawhash = decode_hex(sha3(rlpdata))

                pk = PublicKey(flags=ALL_FLAGS)
                try:
                    pk.public_key = pk.ecdsa_recover(
                        rawhash,
                        pk.ecdsa_recoverable_deserialize(
                            pad_left(
                                int_to_big_endian(self.r),
                                32,
                                b'\x00',
                            ) + pad_left(
                                int_to_big_endian(self.s),
                                32,
                                b'\x00',
                            ),
                            self.v - 27
                        ),
                        raw=True
                    )
                    pub = pk.serialize(compressed=False)
                except Exception:
                    raise ValueError("Invalid signature values (x^3+7 is non-residue)")

                if pub[1:] == b"\x00" * (len(pub) - 1):
                    raise ValueError("Invalid signature (zero privkey cannot sign)")

                self._sender = to_address(sha3(pub[1:])[-40:])
                assert self.sender == self._sender
            else:
                self._sender = 0
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value

    @coerce_args_to_bytes
    def sign(self, key):
        """Sign this transaction with a private key.

        A potentially already existing signature would be overridden.
        """
        if not is_bitcoin_available() or not is_secp256k1_available():
            raise ImportError(
                "In order to sign transactions the "
                "`bitcoin` and `secp256k1` packages must be installed."
            )
        from bitcoin import privtopub
        from secp256k1 import PrivateKey

        if key in (0, b'', b'\x00' * 32, b'0' * 64):
            raise ValueError("Zero privkey cannot sign")

        rawhash = decode_hex(sha3(rlp.encode(self, UnsignedTransaction)))

        if len(key) in {64, 66}:
            # we need a binary key
            key = decode_hex(key)

        pk = PrivateKey(key, raw=True)
        sig_bytes, rec_id = pk.ecdsa_recoverable_serialize(
            pk.ecdsa_sign_recoverable(rawhash, raw=True)
        )
        signature = sig_bytes + force_bytes(chr(rec_id))
        self.v = (ord(signature[64]) if is_string(signature[64]) else signature[64]) + 27
        self.r = decode_big_endian_int(signature[0:32])
        self.s = decode_big_endian_int(signature[32:64])

        self.sender = to_address(sha3(privtopub(key)[1:])[-40:])
        return self


UnsignedTransaction = Transaction.exclude(['v', 'r', 's'])


def serialize_transaction(transaction):
    unsigned_transaction = UnsignedTransaction(
        nonce=to_decimal(transaction['nonce']),
        gasprice=to_decimal(transaction['gasPrice']),
        startgas=to_decimal(transaction['gas']),
        to=transaction['to'],
        value=to_decimal(transaction['value']),
        data=decode_hex(transaction['data']),
    )
    return rlp.encode(unsigned_transaction, UnsignedTransaction)


def add_signature_to_transaction(serialize_transaction, signature):
    unsigned_transaction = rlp.decode(serialize_transaction, UnsignedTransaction)

    v = (ord(signature[64]) if is_string(signature[64]) else signature[64]) + 27
    r = decode_big_endian_int(signature[0:32])
    s = decode_big_endian_int(signature[32:64])

    signed_transaction = Transaction(
        nonce=unsigned_transaction.nonce,
        gasprice=unsigned_transaction.gasprice,
        startgas=unsigned_transaction.startgas,
        to=unsigned_transaction.to,
        value=unsigned_transaction.value,
        data=unsigned_transaction.data,
        v=v,
        r=r,
        s=s,
    )
    return signed_transaction
