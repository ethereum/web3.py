from typing import (
    Any,
    Callable,
    Dict,
    List,
    Tuple,
)

from eth_typing import (
    HexStr,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    DeprecatedMethod,
    Method,
    default_root_munger,
)
from web3.module import (
    Module,
)
from web3.types import (
    EnodeURI,
    ShhFilterID,
    ShhID,
    ShhMessage,
    ShhMessageFilter,
    ShhMessageParams,
    ShhStats,
    ShhSubscriptionID,
)

version: Method[Callable[[], str]] = Method(
    RPC.shh_version,
    mungers=None,
)


info: Method[Callable[[], ShhStats]] = Method(
    RPC.shh_info,
    mungers=None,
)


set_max_message_size: Method[Callable[[int], bool]] = Method(
    RPC.shh_setMaxMessageSize,
    mungers=[default_root_munger],
)


set_min_pow: Method[Callable[[float], bool]] = Method(
    RPC.shh_setMinPoW,
    mungers=[default_root_munger],
)


mark_trusted_peer: Method[Callable[[EnodeURI], bool]] = Method(
    RPC.shh_markTrustedPeer,
    mungers=[default_root_munger],
)


new_key_pair: Method[Callable[[], ShhID]] = Method(
    RPC.shh_newKeyPair,
    mungers=None,
)


add_private_key: Method[Callable[[HexStr], ShhID]] = Method(
    RPC.shh_addPrivateKey,
    mungers=[default_root_munger],
)


delete_key_pair: Method[Callable[[ShhID], bool]] = Method(
    RPC.shh_deleteKeyPair,
    mungers=[default_root_munger],
)


delete_key: Method[Callable[[ShhID], bool]] = Method(
    RPC.shh_deleteKey,
    mungers=[default_root_munger],
)


has_key_pair: Method[Callable[[ShhID], bool]] = Method(
    RPC.shh_hasKeyPair,
    mungers=[default_root_munger],
)


get_public_key: Method[Callable[[ShhID], HexStr]] = Method(
    RPC.shh_getPublicKey,
    mungers=[default_root_munger],
)


get_private_key: Method[Callable[[ShhID], HexStr]] = Method(
    RPC.shh_getPrivateKey,
    mungers=[default_root_munger],
)


new_sym_key: Method[Callable[[], ShhID]] = Method(
    RPC.shh_newSymKey,
    mungers=None,
)


add_sym_key: Method[Callable[[HexStr], ShhID]] = Method(
    RPC.shh_addSymKey,
    mungers=[default_root_munger],
)


generate_sym_key_from_password: Method[Callable[[str], ShhID]] = Method(
    RPC.shh_generateSymKeyFromPassword,
    mungers=[default_root_munger],
)


has_sym_key: Method[Callable[[ShhID], bool]] = Method(
    RPC.shh_hasSymKey,
    mungers=[default_root_munger],
)


get_sym_key: Method[Callable[[ShhID], HexStr]] = Method(
    RPC.shh_getSymKey,
    mungers=[default_root_munger],
)


delete_sym_key: Method[Callable[[ShhID], bool]] = Method(
    RPC.shh_deleteSymKey,
    mungers=[default_root_munger],
)


def post_munger(module: Module, message: Dict[str, Any]) -> Tuple[Dict[str, Any]]:
    if message and ("payload" in message):
        return (message,)
    else:
        raise ValueError("Message cannot be None or does not contain field 'payload'")


post: Method[Callable[[ShhMessageParams], bool]] = Method(
    RPC.shh_post,
    mungers=[post_munger],
)


new_message_filter: Method[Callable[[ShhMessageFilter], ShhFilterID]] = Method(
    RPC.shh_newMessageFilter,
    mungers=[default_root_munger],
)


delete_message_filter: Method[Callable[[ShhFilterID], bool]] = Method(
    RPC.shh_deleteMessageFilter,
    mungers=[default_root_munger],
)


get_filter_messages: Method[Callable[[ShhFilterID], List[ShhMessage]]] = Method(
    RPC.shh_getFilterMessages,
    mungers=[default_root_munger],
)


subscribe: Method[Callable[[ShhMessageFilter], ShhSubscriptionID]] = Method(
    RPC.shh_subscribe,
    mungers=[default_root_munger],
)


unsubscribe: Method[Callable[[ShhSubscriptionID], bool]] = Method(
    RPC.shh_unsubscribe,
    mungers=[default_root_munger],
)

# DeprecatedMethods
setMaxMessageSize = DeprecatedMethod(
    set_max_message_size,
    'setMaxMessageSize',
    'set_max_message_size')
setMinPoW = DeprecatedMethod(set_min_pow, 'setMinPoW', 'set_min_pow')
markTrustedPeer = DeprecatedMethod(mark_trusted_peer, 'markTrustedPeer', 'mark_trusted_peer')
newKeyPair = DeprecatedMethod(new_key_pair, 'newKeyPair', 'new_key_pair')
addPrivateKey = DeprecatedMethod(add_private_key, 'addPrivateKey', 'add_private_key')
deleteKeyPair = DeprecatedMethod(delete_key_pair, 'deleteKeyPair', 'delete_key_pair')
deleteKey = DeprecatedMethod(delete_key, 'deleteKey', 'delete_key')
hasKeyPair = DeprecatedMethod(has_key_pair, 'hasKeyPair', 'has_key_pair')
getPublicKey = DeprecatedMethod(get_public_key, 'getPublicKey', 'get_public_key')
getPrivateKey = DeprecatedMethod(get_private_key, 'getPrivateKey', 'get_private_key')
newSymKey = DeprecatedMethod(new_sym_key, 'newSymKey', 'new_sym_key')
addSymKey = DeprecatedMethod(add_sym_key, 'addSymKey', 'add_sym_key')
generateSymKeyFromPassword = DeprecatedMethod(
    generate_sym_key_from_password,
    'generateSymKeyFromPassword',
    'generate_sym_key_from_password')
hasSymKey = DeprecatedMethod(has_sym_key, 'hasSymKey', 'has_sym_key')
getSymKey = DeprecatedMethod(get_sym_key, 'getSymKey', 'get_sym_key')
deleteSymKey = DeprecatedMethod(delete_sym_key, 'deleteSymKey', 'delete_sym_key')
newMessageFilter = DeprecatedMethod(new_message_filter, 'newMessageFilter', 'new_message_filter')
deleteMessageFilter = DeprecatedMethod(
    delete_message_filter,
    'deleteMessageFilter',
    'delete_message_filter')
getFilterMessages = DeprecatedMethod(
    get_filter_messages,
    'getFilterMessages',
    'get_filter_messages')
