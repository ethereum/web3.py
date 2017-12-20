from eth_keys.datatypes import PrivateKey
from eth_utils import is_same_address

from web3.utils.datastructures import HexBytes
# from web3.utils.signing import LocalAccount

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def construct_transaction_signing_middleware(private_key):
    """Intercept a transaction in flight and sign it.

    Args:
        private_key (TYPE): Private key used to sign the transaction.
                            Accepts the following formats:
                            - `PrivateKey` object from `eth-keys`
                            - `LocalAccount` object from `web3.eth.account`
                            - raw bytes
                            - TODO: hex encoded string


    Returns:
        TYPE: Description
    """

    # Check if the private_key is either
    # - eth_keys.keys.PrivateKey
    # - web3.eth.account.create().privateKey -- can just check that its HexBytes
    # - bytes
    # TODO: - hexbytes
    valid_key_types = (PrivateKey, HexBytes, bytes)

    _private_key = private_key if valid_key_types else None

    if isinstance(private_key, valid_key_types):
        # Might also want to check that bytes length == 32
        # eth_utils.is_32byte_address
        _private_key = private_key

    def transaction_signing_middleware(make_request, web3):
        def middleware(method, params):
            # Only operate on the `eth.sendTransaction` method
            # Only operate on if the private key matches the public key in the transaction
            # Note: params == transaction in this case.
            if method != 'eth_sendTransaction':
                return make_request(method, params)

            transaction = params
            transaction_from_address = transaction.get('from')
            private_key_address = web3.eth.account.privateKeyToAccount(_private_key).address

            if is_same_address(transaction_from_address, private_key_address):
                return make_request(method, params)

            if 'gas' not in transaction:
                # import pdb; pdb.set_trace()
                transaction['gas'] = web3.eth.estimateGas(transaction)
            if 'gas_price' not in transaction:
                transaction['gasPrice'] = web3.eth.gasPrice
            if 'nonce' not in transaction:
                transaction['nonce'] = web3.eth.getTransactionCount(transaction_from_address)

            signed = web3.eth.account.signTransaction(transaction, _private_key)
            raw_transaction = signed.rawTransaction

            return make_request(method='eth_sendRawTransaction', params=[raw_transaction])
        return middleware
    return transaction_signing_middleware
