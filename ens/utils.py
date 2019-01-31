import copy
import datetime
import functools

from eth_utils import (
    is_same_address,
    remove_0x_prefix,
    to_normalized_address,
)
import idna

from ens.constants import (
    ACCEPTABLE_STALE_HOURS,
    AUCTION_START_GAS_CONSTANT,
    AUCTION_START_GAS_MARGINAL,
    EMPTY_SHA3_BYTES,
    MIN_ETH_LABEL_LENGTH,
    REVERSE_REGISTRAR_DOMAIN,
)
from ens.exceptions import (
    InvalidLabel,
    InvalidName,
)

default = object()


def Web3():
    from web3 import Web3
    return Web3


def dict_copy(func):
    "copy dict keyword args, to avoid modifying caller's copy"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        copied_kwargs = copy.deepcopy(kwargs)
        return func(*args, **copied_kwargs)
    return wrapper


def ensure_hex(data):
    if not isinstance(data, str):
        return Web3().toHex(data)
    return data


def init_web3(providers=default):
    from web3 import Web3

    if providers is default:
        w3 = Web3(ens=None)
    else:
        w3 = Web3(providers, ens=None)

    return customize_web3(w3)


def customize_web3(w3):
    from web3.middleware import make_stalecheck_middleware

    w3.middleware_onion.remove('name_to_address')
    w3.middleware_onion.add(
        make_stalecheck_middleware(ACCEPTABLE_STALE_HOURS * 3600),
        name='stalecheck',
    )
    return w3


def normalize_name(name):
    """
    Clean the fully qualified name, as defined in ENS `EIP-137
    <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#name-syntax>`_

    This does *not* enforce whether ``name`` is a label or fully qualified domain.

    :param str name: the dot-separated ENS name
    :raises InvalidName: if ``name`` has invalid syntax
    """
    if not name:
        return name
    elif isinstance(name, (bytes, bytearray)):
        name = name.decode('utf-8')
    try:
        return idna.decode(name, uts46=True, std3_rules=True)
    except idna.IDNAError as exc:
        raise InvalidName("%s is an invalid name, because %s" % (name, exc)) from exc


def is_valid_name(name):
    """
    Validate whether the fully qualified name is valid, as defined in ENS `EIP-137
    <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#name-syntax>`_

    :param str name: the dot-separated ENS name
    :returns: True if ``name`` is set, and :meth:`~ens.main.ENS.nameprep` will not raise InvalidName
    """
    if not name:
        return False
    try:
        normalize_name(name)
        return True
    except InvalidName:
        return False


def name_to_label(name, registrar):
    name = normalize_name(name)
    if '.' not in name:
        label = name
    else:
        name_pieces = name.split('.')
        registrar_pieces = registrar.split('.')
        if len(name_pieces) != len(registrar_pieces) + 1:
            raise ValueError(
                "You must specify a label, like 'tickets' "
                "or a fully-qualified name, like 'tickets.%s'" % registrar
            )
        label, *label_registrar = name_pieces
        if label_registrar != registrar_pieces:
            raise ValueError("This interface only manages names under .%s " % registrar)
    return label


def dot_eth_label(name):
    """
    Convert from a name, like 'ethfinex.eth', to a label, like 'ethfinex'
    If name is already a label, this should be a noop, except for converting to a string
    and validating the name syntax.
    """
    label = name_to_label(name, registrar='eth')
    if len(label) < MIN_ETH_LABEL_LENGTH:
        raise InvalidLabel('name %r is too short' % label)
    else:
        return label


def to_utc_datetime(timestamp):
    if timestamp:
        return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
    else:
        return None


def sha3_text(val):
    if isinstance(val, str):
        val = val.encode('utf-8')
    return Web3().keccak(val)


def label_to_hash(label):
    label = normalize_name(label)
    if '.' in label:
        raise ValueError("Cannot generate hash for label %r with a '.'" % label)
    return Web3().keccak(text=label)


def normal_name_to_hash(name):
    node = EMPTY_SHA3_BYTES
    if name:
        labels = name.split(".")
        for label in reversed(labels):
            labelhash = label_to_hash(label)
            assert isinstance(labelhash, bytes)
            assert isinstance(node, bytes)
            node = Web3().keccak(node + labelhash)
    return node


def raw_name_to_hash(name):
    """
    Generate the namehash. This is also known as the ``node`` in ENS contracts.

    In normal operation, generating the namehash is handled
    behind the scenes. For advanced usage, it is a helpful utility.

    This normalizes the name with `nameprep
    <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#name-syntax>`_
    before hashing.

    :param str name: ENS name to hash
    :return: the namehash
    :rtype: bytes
    :raises InvalidName: if ``name`` has invalid syntax
    """
    normalized_name = normalize_name(name)
    return normal_name_to_hash(normalized_name)


def address_in(address, addresses):
    return any(is_same_address(address, item) for item in addresses)


def address_to_reverse_domain(address):
    lower_unprefixed_address = remove_0x_prefix(to_normalized_address(address))
    return lower_unprefixed_address + '.' + REVERSE_REGISTRAR_DOMAIN


def estimate_auction_start_gas(labels):
    return AUCTION_START_GAS_CONSTANT + AUCTION_START_GAS_MARGINAL * len(labels)


def assert_signer_in_modifier_kwargs(modifier_kwargs):
    ERR_MSG = "You must specify the sending account"
    assert len(modifier_kwargs) == 1, ERR_MSG

    _modifier_type, modifier_dict = dict(modifier_kwargs).popitem()
    if 'from' not in modifier_dict:
        raise TypeError(ERR_MSG)

    return modifier_dict['from']


def is_none_or_zero_address(addr):
    return not addr or addr == '0x' + '00' * 20
