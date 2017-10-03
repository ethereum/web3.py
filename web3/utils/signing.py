
import sys

from web3.utils.encoding import (
    to_bytes,
    to_hex,
)

CHAIN_ID_OFFSET = 35
V_OFFSET = 27


# watch here for updates to signature format: https://github.com/ethereum/EIPs/issues/191
def signature_wrapper(message, version=b'E'):
    assert isinstance(message, bytes)
    if version == b'E':
        preamble = b'\x19Ethereum Signed Message:\n'
        size = str(len(message)).encode('utf-8')
        return preamble + size + message
    else:
        raise NotImplementedError("Only the 'Ethereum Signed Message' preamble is supported")


def annotate_transaction_with_chain_id(transaction_parts, raw_v):
    '''
    Extends transaction with chain ID, according to EIP-155
    See details at https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md
    @return (transaction_parts, chain_id, v)
    '''
    assert len(transaction_parts) == 6
    (chain_id, v) = extract_chain_id(raw_v)
    if chain_id is None:
        chain_id_extension = []
    else:
        chain_id_extension = [to_bytes(chain_id), b'', b'']
    return (transaction_parts + chain_id_extension, chain_id, v)


def extract_chain_id(raw_v):
    '''
    Extracts chain ID, according to EIP-155
    @return (chain_id, v)
    '''
    above_id_offset = raw_v - CHAIN_ID_OFFSET
    if above_id_offset < 0:
        return (None, raw_v)
    else:
        (chain_id, v_bit) = divmod(above_id_offset, 2)
        return (chain_id, v_bit + V_OFFSET)


def sign_transaction_hash(account, transaction_hash, chain_id):
    signature = account.sign_msg_hash(transaction_hash)
    (v_raw, r, s) = signature.vrs
    v = 2 * chain_id + CHAIN_ID_OFFSET + v_raw
    return (v, r, s)


class LocalAccount(object):
    '''
    Collection of convenience methods on private key, roughly using the
    same API as web3.js: https://web3js.readthedocs.io/en/1.0/web3-eth-accounts.html#create
    '''
    def __init__(self, key, web3):
        '''
        @param key instance of eth_keys.PrivateKey
        '''
        self._publicapi = web3.eth.account

        self.address = key.public_key.to_checksum_address()

        key_raw = key.to_bytes()
        if sys.version_info.major < 3:
            key_raw = to_hex(key_raw)
        self.privateKey = key_raw

        self._key_obj = key

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

    # Python 2 support
    def __str__(self):
        return self.privateKey
