from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
)

from eth_typing import (
    ChecksumAddress,
    HexStr,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.compat import (
    Protocol,
)
from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    Method,
    default_root_munger,
)
from web3.types import (
    GethWallet,
    TxParams,
)

import_raw_key: Method[Callable[[str, str], ChecksumAddress]] = Method(
    RPC.personal_importRawKey,
    mungers=[default_root_munger],
)


new_account: Method[Callable[[str], ChecksumAddress]] = Method(
    RPC.personal_newAccount,
    mungers=[default_root_munger],
)


list_accounts: Method[Callable[[], List[ChecksumAddress]]] = Method(
    RPC.personal_listAccounts,
    is_property=True,
)


list_wallets: Method[Callable[[], List[GethWallet]]] = Method(
    RPC.personal_listWallets,
    is_property=True,
)


send_transaction: Method[Callable[[TxParams, str], HexBytes]] = Method(
    RPC.personal_sendTransaction,
    mungers=[default_root_munger],
)


lock_account: Method[Callable[[ChecksumAddress], bool]] = Method(
    RPC.personal_lockAccount,
    mungers=[default_root_munger],
)


class UnlockAccountWrapper(Protocol):
    def __call__(
        self, account: ChecksumAddress, passphrase: str, duration: Optional[int] = None
    ) -> bool:
        pass


unlock_account: Method[UnlockAccountWrapper] = Method(
    RPC.personal_unlockAccount,
    mungers=[default_root_munger],
)


sign: Method[Callable[[str, ChecksumAddress, Optional[str]], HexStr]] = Method(
    RPC.personal_sign,
    mungers=[default_root_munger],
)


sign_typed_data: Method[
    Callable[[Dict[str, Any], ChecksumAddress, str], HexStr]
] = Method(
    RPC.personal_signTypedData,
    mungers=[default_root_munger],
)


ec_recover: Method[Callable[[str, HexStr], ChecksumAddress]] = Method(
    RPC.personal_ecRecover,
    mungers=[default_root_munger],
)
