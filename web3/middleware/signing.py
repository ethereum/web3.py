from eth_account.local import (
    LocalAccount,
)
from eth_keys.datatypes import (
    PrivateKey,
)
from eth_utils import (
    is_same_address,
)
from toolz import (
    compose,
)

from web3.utils.formatters import (
    apply_formatter_if,
)
from web3.utils.transactions import (
    fill_nonce,
    fill_transaction_defaults,
)

to_hexstr_from_eth_key = lambda x: x.to_hex()  # noqa: E731


def is_eth_key(value):
    if isinstance(value, PrivateKey):
        return True
    return False


def raw_key_formatter(private_key):
    formatter = compose(
        apply_formatter_if(is_eth_key, to_hexstr_from_eth_key),
    )
    return formatter(private_key)


def to_account(web3, private_key):

    if isinstance(private_key, LocalAccount):
        return private_key

    elif isinstance(private_key, (PrivateKey, str, bytes,)):
        normalized_key = raw_key_formatter(private_key)
        return web3.eth.account.privateKeyToAccount(normalized_key)

    raise TypeError(
        "key must be one of the types: "
        "eth_keys.datatype.PrivateKey, eth_account.local.LocalAccount, "
        "or raw private key as a string or bytestring. "
        "Was of type {0}".format(type(private_key)))


def construct_sign_and_send_raw_middleware(private_key):

    def sign_and_send_raw_middleware(make_request, web3):
        account = to_account(web3, private_key)

        def middleware(method, params):
            if method == "eth_sendTransaction":

                fill_tx = compose(
                    fill_transaction_defaults(web3),
                    fill_nonce(web3))

                transaction = fill_tx(params[0])

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

                raw_tx = account.signTransaction(transaction).rawTransaction

                return make_request(
                    "eth_sendRawTransaction",
                    [raw_tx])

            else:
                return make_request(method, params)

        return middleware

    return sign_and_send_raw_middleware
