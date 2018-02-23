from web3.utils.transactions import (
    fill_transaction_defaults
)
import eth_account
from hexbytes import HexBytes

from cytoolz import (
    merge,
)


def key_to_account(web3, key):
    if isinstance(key, eth_account.local.LocalAccount):
        return key
    if isinstance(key, (HexBytes, str, bytes)):
        return web3.eth.account.privateKeyToAccount(key)
    try:
        # TODO Find a better way to check for and handle eth_keys objects
        return web3.eth.account.privateKeyToAccount(key.to_hex())
    except AttributeError:
        raise ValueError("key must be one of the types (...). Was of type {0}".format(type(key)))


def construct_in_flight_transaction_signing_middleware(private_key):

    def in_flight_transaction_signing_middleware(make_request, web3):
        account = key_to_account(web3, private_key)

        def middleware(method, params):
            if method == "eth_sendTransaction":

                transaction_filler = {
                    'from': account.address,
                    'nonce': web3.eth.getTransactionCount(account.address)
                }

                transaction = merge(transaction_filler, params[0])
                filled_transaction = fill_transaction_defaults(web3, transaction)
                signed_transaction = account.signTransaction(filled_transaction)
                return make_request("eth_sendRawTransaction", [signed_transaction.rawTransaction])
            else:
                return make_request(method, params)
        return middleware
    return in_flight_transaction_signing_middleware
