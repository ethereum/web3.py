from web3.method import (
    Method,
)


def default_root_munger(module, *args):
    return [*args]


def importRawKey():
    return Method(
        "personal_importRawKey",
        mungers=[default_root_munger],
        formatter_lookup_fn=None,
    )


def newAccount():
    return Method(
        "personal_newAccount",
        mungers=[default_root_munger],
        formatter_lookup_fn=None,
    )


def listAccounts():
    return Method(
        "personal_listAccounts",
        mungers=None,
        formatter_lookup_fn=None,
    )


def sendTransaction():
    return Method(
        "personal_sendTransaction",
        mungers=[default_root_munger],
        formatter_lookup_fn=None,
    )


def lockAccount():
    return Method(
        "personal_lockAccount",
        mungers=[default_root_munger],
        formatter_lookup_fn=None,
    )


def unlockAccount():
    return Method(
        "personal_unlockAccount",
        mungers=[default_root_munger],
        formatter_lookup_fn=None,
    )


def sign():
    return Method(
        "personal_sign",
        mungers=[default_root_munger],
        formatter_lookup_fn=None,
    )


def ecRecover():
    return Method(
        "personal_ecRecover",
        mungers=[default_root_munger],
        formatter_lookup_fn=None,
    )
