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
    TxParams,
)

importRawKey: Method[Callable[[str, str], ChecksumAddress]] = Method(
    RPC.personal_importRawKey,
    mungers=[default_root_munger],
)


newAccount: Method[Callable[[str], ChecksumAddress]] = Method(
    RPC.personal_newAccount,
    mungers=[default_root_munger],
)


listAccounts: Method[Callable[[], List[ChecksumAddress]]] = Method(
    RPC.personal_listAccounts,
    mungers=None,
)


sendTransaction: Method[Callable[[TxParams, str], HexBytes]] = Method(
    RPC.personal_sendTransaction,
    mungers=[default_root_munger],
)


lockAccount: Method[Callable[[ChecksumAddress], bool]] = Method(
    RPC.personal_lockAccount,
    mungers=[default_root_munger],
)


class UnlockAccountWrapper(Protocol):
    def __call__(self, account: ChecksumAddress, passphrase: str, duration: int=None) -> bool:
        pass


unlockAccount: Method[UnlockAccountWrapper] = Method(
    RPC.personal_unlockAccount,
    mungers=[default_root_munger],
)


sign: Method[Callable[[str, ChecksumAddress, Optional[str]], HexStr]] = Method(
    RPC.personal_sign,
    mungers=[default_root_munger],
)


signTypedData: Method[Callable[[Dict[str, Any], ChecksumAddress, str], HexStr]] = Method(
    RPC.personal_signTypedData,
    mungers=[default_root_munger],
)


ecRecover: Method[Callable[[str, HexStr], ChecksumAddress]] = Method(
    RPC.personal_ecRecover,
    mungers=[default_root_munger],
)
