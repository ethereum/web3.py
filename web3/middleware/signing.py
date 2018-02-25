import eth_account
from eth_utils import (
    is_same_address,
)

from web3.utils.transactions import (
    fill_transaction_defaults,
)


def key_to_account(web3, key):
    if isinstance(key, eth_account.local.LocalAccount):
        return key
    if isinstance(key, (str, bytes)):
        return web3.eth.account.privateKeyToAccount(key)
    try:
        sk_hex = key.to_hex()
        return web3.eth.account.privateKeyToAccount(sk_hex)
    except AttributeError:
        raise TypeError("key must be one of the types (...). Was of type {0}".format(type(key)))


def construct_sign_and_send_raw_middleware(private_key):

    def sign_and_send_raw_middleware(make_request, web3):
        account = key_to_account(web3, private_key)

        def middleware(method, params):
            if method == "eth_sendTransaction":
                transaction = fill_transaction_defaults(web3, params[0])

                if 'from' in transaction:
                    try:
                        assert is_same_address(account.address, transaction['from'])
                    except AssertionError:
                        raise ValueError("Sending account address mismatch. \
                            Transaction 'from' parameter does not match the \
                            address to the private key used to construct signing \
                            middleware.")
                else:
                    raise ValueError("Transaction signing middleware parameter \
                        requirement not met: 'from' address was not included in\
                        transaction parameters.")

                # TODO: Can this be added to fill_transaction_defaults()?
                transaction['nonce'] = web3.eth.getTransactionCount(account.address)

                signed_transaction = account.signTransaction(transaction)

                return make_request(
                    "eth_sendRawTransaction",
                    [signed_transaction.rawTransaction])

            else:
                return make_request(method, params)

        return middleware

    return sign_and_send_raw_middleware
