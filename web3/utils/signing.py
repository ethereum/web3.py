from cytoolz import (
    compose,
)

from web3.utils.encoding import (
    to_bytes,
    to_int,
    zpad_bytes,
)

from web3.utils.transactions import (
    ChainAwareUnsignedTransaction,
    UnsignedTransaction,
    encode_transaction,
    serializable_unsigned_transaction_from_dict,
    strip_signature,
)

CHAIN_ID_OFFSET = 35
V_OFFSET = 27


def sign_transaction_dict(eth_key, transaction_dict):
    # indicate that no functions should try to make calls to the client
    web3 = None

    # generate RLP-serializable transaction, with defaults filled
    unsigned_transaction = serializable_unsigned_transaction_from_dict(web3, transaction_dict)

    transaction_hash = unsigned_transaction.hash()

    # detect chain
    if isinstance(unsigned_transaction, UnsignedTransaction):
        chain_id = None
    else:
        chain_id = unsigned_transaction.v

    # sign with private key
    (v, r, s) = sign_transaction_hash(eth_key, transaction_hash, chain_id)

    # serialize transaction with rlp
    encoded_transaction = encode_transaction(unsigned_transaction, vrs=(v, r, s))

    return (v, r, s, encoded_transaction)


# watch here for updates to signature format: https://github.com/ethereum/EIPs/issues/191
def signature_wrapper(message, version=b'E'):
    assert isinstance(message, bytes)
    if version == b'E':
        preamble = b'\x19Ethereum Signed Message:\n'
        size = str(len(message)).encode('utf-8')
        return preamble + size + message
    else:
        raise NotImplementedError("Only the 'Ethereum Signed Message' preamble is supported")


def hash_of_signed_transaction(txn_obj):
    '''
    Regenerate the hash of the signed transaction object.

    1. Infer the chain ID from the signature
    2. Strip out signature from transaction
    3. Annotate the transaction with that ID, if available
    4. Take the hash of the serialized, unsigned, chain-aware transaction

    Chain ID inference and annotation is according to EIP-155
    See details at https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md

    :return: chain-aware transaction, ready for hashing/signing
    :rtype: `~web3.utils.encoding.ExtendedRLP`
    '''
    (chain_id, _v) = extract_chain_id(txn_obj.v)
    unsigned_parts = strip_signature(txn_obj)
    if chain_id is None:
        signable_transaction = UnsignedTransaction(*unsigned_parts)
    else:
        extended_transaction = unsigned_parts + [chain_id, 0, 0]
        signable_transaction = ChainAwareUnsignedTransaction(*extended_transaction)
    return signable_transaction.hash()


def extract_chain_id(raw_v):
    '''
    Extracts chain ID, according to EIP-155
    @return (chain_id, v)
    '''
    above_id_offset = raw_v - CHAIN_ID_OFFSET
    if above_id_offset < 0:
        if raw_v in {0, 1}:
            return (None, raw_v + V_OFFSET)
        elif raw_v in {27, 28}:
            return (None, raw_v)
        else:
            raise ValueError("v %r is invalid, must be one of: 0, 1, 27, 28, 35+")
    else:
        (chain_id, v_bit) = divmod(above_id_offset, 2)
        return (chain_id, v_bit + V_OFFSET)


def to_standard_signature_bytes(ethereum_signature_bytes):
    rs = ethereum_signature_bytes[:-1]
    v = to_int(ethereum_signature_bytes[-1])
    standard_v = to_standard_v(v)
    return rs + to_bytes(standard_v)


def to_standard_v(enhanced_v):
    (_chain, chain_naive_v) = extract_chain_id(enhanced_v)
    v_standard = chain_naive_v - V_OFFSET
    assert v_standard in {0, 1}
    return v_standard


def to_eth_v(v_raw, chain_id=None):
    if chain_id is None:
        v = v_raw + V_OFFSET
    else:
        v = v_raw + CHAIN_ID_OFFSET + 2 * chain_id
    return v


def sign_transaction_hash(account, transaction_hash, chain_id):
    signature = account.sign_msg_hash(transaction_hash)
    (v_raw, r, s) = signature.vrs
    v = to_eth_v(v_raw, chain_id)
    return (v, r, s)


to_bytes32 = compose(zpad_bytes(32), to_bytes)


def sign_message_hash(key, msg_hash):
    signature = key.sign_msg_hash(msg_hash)
    (v_raw, r, s) = signature.vrs
    v = to_eth_v(v_raw)
    eth_signature_bytes = to_bytes32(r) + to_bytes32(s) + to_bytes(v)
    return (v, r, s, eth_signature_bytes)


class LocalAccount(object):
    '''
    Collection of convenience methods on private key, roughly using the
    same API as web3.js: https://web3js.readthedocs.io/en/1.0/web3-eth-accounts.html#create
    '''
    def __init__(self, key, account):
        '''
        :param eth_keys.PrivateKey key: to prefill in private key execution
        :param web3.account.Account account: the key-unaware management API
        '''
        self._publicapi = account

        self.address = key.public_key.to_checksum_address()

        key_raw = key.to_bytes()
        self.privateKey = key_raw

        self._key_obj = key

    def encrypt(self, password):
        return self._publicapi.encrypt(self.privateKey, password)

    def sign(self, *args, **kwargs):
        if len(args) > 1 or 'private_key' in kwargs:
            raise TypeError(
                "This account object already has a private key,"
                "you cannot specify a different one."
            )
        kwargs['private_key'] = self.privateKey
        return self._publicapi.sign(*args, **kwargs)

    def signTransaction(self, transaction_dict):
        return self._publicapi.signTransaction(transaction_dict, self.privateKey)

    def __bytes__(self):
        return self.privateKey
