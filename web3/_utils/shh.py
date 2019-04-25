from web3.method import (
    Method,
    default_root_munger,
)

version = Method(
    "shh_version",
    mungers=None,
)


info = Method(
    "shh_info",
    mungers=None,
)


setMaxMessageSize = Method(
    "shh_setMaxMessageSize",
    mungers=[default_root_munger],
)


setMinPoW = Method(
    "shh_setMinPoW",
    mungers=[default_root_munger],
)


markTrustedPeer = Method(
    "shh_markTrustedPeer",
    mungers=[default_root_munger],
)


newKeyPair = Method(
    "shh_newKeyPair",
    mungers=None,
)


addPrivateKey = Method(
    "shh_addPrivateKey",
    mungers=[default_root_munger],
)


deleteKeyPair = Method(
    "shh_deleteKeyPair",
    mungers=[default_root_munger],
)


deleteKey = Method(
    "shh_deleteKey",
    mungers=[default_root_munger],
)


hasKeyPair = Method(
    "shh_hasKeyPair",
    mungers=[default_root_munger],
)


getPublicKey = Method(
    "shh_getPublicKey",
    mungers=[default_root_munger],
)


getPrivateKey = Method(
    "shh_getPrivateKey",
    mungers=[default_root_munger],
)


newSymKey = Method(
    "shh_newSymKey",
    mungers=None,
)


addSymKey = Method(
    "shh_addSymKey",
    mungers=[default_root_munger],
)


generateSymKeyFromPassword = Method(
    "shh_generateSymKeyFromPassword",
    mungers=[default_root_munger],
)


hasSymKey = Method(
    "shh_hasSymKey",
    mungers=[default_root_munger],
)


getSymKey = Method(
    "shh_getSymKey",
    mungers=[default_root_munger],
)


deleteSymKey = Method(
    "shh_deleteSymKey",
    mungers=[default_root_munger],
)


def post_munger(module, message):
    if message and ("payload" in message):
        return (message,)
    else:
        raise ValueError("Message cannot be None or does not contain field 'payload'")


post = Method(
    "shh_post",
    mungers=[post_munger],
)


newMessageFilter = Method(
    "shh_newMessageFilter",
    mungers=[default_root_munger],
)


deleteMessageFilter = Method(
    "shh_deleteMessageFilter",
    mungers=[default_root_munger],
)


getFilterMessages = Method(
    "shh_getFilterMessages",
    mungers=[default_root_munger],
)


subscribe = Method(
    "shh_subscribe",
    mungers=[default_root_munger],
)


unsubscribe = Method(
    "shh_unsubscribe",
    mungers=[default_root_munger],
)
