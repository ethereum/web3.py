from eth_keys import (
    datatypes,
)
import eth_utils

from web3.exceptions import (
    InvalidAddress,
)
from web3.utils import (
    datastructures,
)


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

    valid_key_types = (datatypes.PrivateKey, datastructures.HexBytes, bytes)

    if not isinstance(private_key, valid_key_types):
        raise ValueError('Private Key is invalid.')

    def transaction_signing_middleware(make_request, web3):
        def middleware(method, params):
            # Only operate on the `eth.sendTransaction` method
            # Only operate on if the private key matches the public key in the transaction
            # Note: params[0] == transaction in this case.
            if method != 'eth_sendTransaction':
                return make_request(method, params)
            if not isinstance(params, list):
                raise TypeError('Params should be of type `list`')
            if not len(params) == 1:
                raise ValueError('Params list should be of length 1')
            if not isinstance(params[0], dict):
                raise TypeError('Transaction should be of type `dict`')

            transaction = params[0]
            transaction_from_address = transaction.get('from')
            private_key_address = web3.eth.account.privateKeyToAccount(private_key).address

            if not eth_utils.is_same_address(transaction_from_address, private_key_address):
                return make_request(method, params)

            if 'gas' not in transaction:
                try:
                    transaction['gas'] = web3.eth.estimateGas(transaction)
                except ValueError:
                    # raise
                    transaction['gas'] = 21000
            if 'gas_price' not in transaction:
                transaction['gasPrice'] = web3.eth.gasPrice
            if 'chainId' not in transaction:
                transaction['chainId'] = int(web3.net.version)
            if 'nonce' not in transaction:
                try:
                    transaction['nonce'] = web3.eth.getTransactionCount(transaction_from_address)
                except InvalidAddress:
                    raise

            signed = web3.eth.account.signTransaction(transaction, private_key)
            raw_transaction = signed.get('rawTransaction')

            return make_request(method='eth_sendRawTransaction', params=[raw_transaction])
        return middleware
    return transaction_signing_middleware
