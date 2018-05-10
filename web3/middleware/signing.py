from functools import (
    singledispatch,
)
import operator

from eth_account import (
    Account,
)
from eth_account.local import (
    LocalAccount,
)
from eth_keys.datatypes import (
    PrivateKey,
)
from eth_utils import (
    is_same_address,
)

from web3.utils.formatters import (
    apply_formatter_if,
)
from web3.utils.toolz import (
    compose,
)
from web3.utils.transactions import (
    fill_nonce,
    fill_transaction_defaults,
)

to_hexstr_from_eth_key = operator.methodcaller('to_hex')


def is_eth_key(value):
    if isinstance(value, PrivateKey):
        return True
    return False


def raw_key_formatter(private_key):
    formatter = compose(
        apply_formatter_if(is_eth_key, to_hexstr_from_eth_key),
    )
    return formatter(private_key)


@singledispatch
def to_account(val):
    raise TypeError(
        "key must be one of the types: "
        "eth_keys.datatype.PrivateKey, eth_account.local.LocalAccount, "
        "or raw private key as a string or bytestring. "
        "Was of type {0}".format(type(val)))


@to_account.register(LocalAccount)
def _(val):
    return val


def private_key_to_account(val):
    normalized_key = raw_key_formatter(val)
    return Account.privateKeyToAccount(normalized_key)


to_account.register(PrivateKey, private_key_to_account)
to_account.register(str, private_key_to_account)
to_account.register(bytes, private_key_to_account)


def construct_sign_and_send_raw_middleware(private_key_or_account):

    def sign_and_send_raw_middleware(make_request, w3):
        account = to_account(private_key_or_account)

        fill_tx = compose(
            fill_transaction_defaults(w3),
            fill_nonce(w3))

        def middleware(method, params):
            if not method == "eth_sendTransaction":
                return make_request(method, params)

            else:
                transaction = fill_tx(params[0])

                if 'from' in transaction:
                    if not is_same_address(account.address, transaction['from']):
                        raise ValueError(
                            "Sending account address mismatch."
                            "Transaction 'from' parameter does not match the"
                            "address to the private key used to construct signing"
                            "middleware.")
                else:
                    raise ValueError(
                        "Transaction signing middleware parameter"
                        "requirement not met: 'from' address was not included in"
                        "transaction parameters.")

                raw_tx = account.signTransaction(transaction).rawTransaction

                return make_request(
                    "eth_sendRawTransaction",
                    [raw_tx])

        return middleware

    return sign_and_send_raw_middleware
