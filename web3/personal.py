from web3.method import (
    Method,
    default_root_munger,
)


def importRawKey():
    return Method(
        "personal_importRawKey",
        mungers=[default_root_munger],
    )


def newAccount():
    return Method(
        "personal_newAccount",
        mungers=[default_root_munger],
    )


def listAccounts():
    return Method(
        "personal_listAccounts",
        mungers=None,
    )


def sendTransaction():
    return Method(
        "personal_sendTransaction",
        mungers=[default_root_munger],
    )


def lockAccount():
    return Method(
        "personal_lockAccount",
        mungers=[default_root_munger],
    )


def unlockAccount():
    return Method(
        "personal_unlockAccount",
        mungers=[default_root_munger],
    )


def sign():
    return Method(
        "personal_sign",
        mungers=[default_root_munger],
    )


def ecRecover():
    return Method(
        "personal_ecRecover",
        mungers=[default_root_munger],
    )
