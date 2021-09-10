from eth_account import (
    Account,
)
from toolz import (
    assoc,
)

from web3._utils.transactions import (
    fill_transaction_defaults,
)
from web3.types import (
    TYPE_CHECKING,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class AccountWrapper(Account):
    """
    This is a wrapper for eth-account's Account class. It exists primarily as a bridge for
    web3.py to provide any translation / validation necessary to communicate more effectively
    with eth-account.
    """
    def __init__(self, web3: "Web3") -> None:
        self.web3 = web3

    # type ignored because Account.sign_transaction() does not have typing in place
    def sign_transaction(self, transaction_dict: TxParams, private_key):  # type: ignore
        transaction_dict = fill_transaction_defaults(self.web3, transaction_dict)

        if transaction_dict.get('accessList') is not None:
            access_list = transaction_dict.get('accessList')

            if len(access_list) > 0 and isinstance(access_list[0], dict):
                # If we have a non-empty accessList and it exists as an RPC-friendly structure
                # (contains dicts rather than tuples), convert to the appropriate rlp structure
                # for accessList by simplifying key -> value pairs into just tuples of the values.
                # This allows us to successfully sign with eth-account.
                # see: https://github.com/ethereum/web3.py/issues/2142
                rlp_structured_access_list = []
                for d in transaction_dict['accessList']:
                    rlp_structured_access_list.append(
                        (
                            d['address'],  # value of address
                            tuple(_ for _ in d['storageKeys'])  # tuple with storage key values
                        )
                    )

                transaction_dict = assoc(transaction_dict, 'accessList', rlp_structured_access_list)

        return Account.sign_transaction(transaction_dict, private_key)
