from web3.method import (
    Method,
    default_root_munger,
)

importRawKey = Method(
    "personal_importRawKey",
    mungers=[default_root_munger],
)


newAccount = Method(
    "personal_newAccount",
    mungers=[default_root_munger],
)


listAccounts = Method(
    "personal_listAccounts",
    mungers=None,
)


sendTransaction = Method(
    "personal_sendTransaction",
    mungers=[default_root_munger],
)


lockAccount = Method(
    "personal_lockAccount",
    mungers=[default_root_munger],
)


unlockAccount = Method(
    "personal_unlockAccount",
    mungers=[default_root_munger],
)


sign = Method(
    "personal_sign",
    mungers=[default_root_munger],
)


ecRecover = Method(
    "personal_ecRecover",
    mungers=[default_root_munger],
)
