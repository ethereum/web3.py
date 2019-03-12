from web3.method import (
    Method,
    default_root_munger,
)


def version():
    return Method(
        "shh_version",
        mungers=None,
    )


def info():
    return Method(
        "shh_info",
        mungers=None,
    )


def setMaxMessageSize():
    return Method(
        "shh_setMaxMessageSize",
        mungers=[default_root_munger],
    )


def setMinPoW():
    return Method(
        "shh_setMinPoW",
        mungers=[default_root_munger],
    )


def markTrustedPeer():
    return Method(
        "shh_markTrustedPeer",
        mungers=[default_root_munger],
    )


def newKeyPair():
    return Method(
        "shh_newKeyPair",
        mungers=None,
    )


def addPrivateKey():
    return Method(
        "shh_addPrivateKey",
        mungers=[default_root_munger],
    )


def deleteKeyPair():
    return Method(
        "shh_deleteKeyPair",
        mungers=[default_root_munger],
    )


def deleteKey():
    return Method(
        "shh_deleteKey",
        mungers=[default_root_munger],
    )


def hasKeyPair():
    return Method(
        "shh_hasKeyPair",
        mungers=[default_root_munger],
    )


def getPublicKey():
    return Method(
        "shh_getPublicKey",
        mungers=[default_root_munger],
    )


def getPrivateKey():
    return Method(
        "shh_getPrivateKey",
        mungers=[default_root_munger],
    )


def newSymKey():
    return Method(
        "shh_newSymKey",
        mungers=None,
    )


def addSymKey():
    return Method(
        "shh_addSymKey",
        mungers=[default_root_munger],
    )


def generateSymKeyFromPassword():
    return Method(
        "shh_generateSymKeyFromPassword",
        mungers=[default_root_munger],
    )


def hasSymKey():
    return Method(
        "shh_hasSymKey",
        mungers=[default_root_munger],
    )


def getSymKey():
    return Method(
        "shh_getSymKey",
        mungers=[default_root_munger],
    )


def deleteSymKey():
    return Method(
        "shh_deleteSymKey",
        mungers=[default_root_munger],
    )


def post_munger(module, message):
    if message and ("payload" in message):
        return (message,)
    else:
        raise ValueError("Message cannot be None or does not contain field 'payload'")


def post():
    return Method(
        "shh_post",
        mungers=[post_munger],
    )


def newMessageFilter():
    return Method(
        "shh_newMessageFilter",
        mungers=[default_root_munger],
    )


def deleteMessageFilter():
    return Method(
        "shh_deleteMessageFilter",
        mungers=[default_root_munger],
    )


def getFilterMessages():
    return Method(
        "shh_getFilterMessages",
        mungers=[default_root_munger],
    )


def subscribe():
    return Method(
        "shh_subscribe",
        mungers=[default_root_munger],
    )


def unsubscribe():
    return Method(
        "shh_unsubscribe",
        mungers=[default_root_munger],
    )
