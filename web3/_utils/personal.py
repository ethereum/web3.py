from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    Method,
    default_root_munger,
)

importRawKey = Method(
    RPC.personal_importRawKey,
    mungers=[default_root_munger],
)


newAccount = Method(
    RPC.personal_newAccount,
    mungers=[default_root_munger],
)


listAccounts = Method(
    RPC.personal_listAccounts,
    mungers=None,
)


sendTransaction = Method(
    RPC.personal_sendTransaction,
    mungers=[default_root_munger],
)


lockAccount = Method(
    RPC.personal_lockAccount,
    mungers=[default_root_munger],
)


unlockAccount = Method(
    RPC.personal_unlockAccount,
    mungers=[default_root_munger],
)


sign = Method(
    RPC.personal_sign,
    mungers=[default_root_munger],
)


signTypedData = Method(
    RPC.personal_signTypedData,
    mungers=[default_root_munger],
)


ecRecover = Method(
    RPC.personal_ecRecover,
    mungers=[default_root_munger],
)
