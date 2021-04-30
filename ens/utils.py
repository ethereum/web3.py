import copy
import datetime
import functools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Optional,
    Type,
    TypeVar,
    Union,
    cast,
)

from eth_typing import (
    Address,
    ChecksumAddress,
    HexAddress,
    HexStr,
)
from eth_utils import (
    is_same_address,
    remove_0x_prefix,
    to_normalized_address,
)
from hexbytes import (
    HexBytes,
)
import idna

from ens.constants import (
    ACCEPTABLE_STALE_HOURS,
    AUCTION_START_GAS_CONSTANT,
    AUCTION_START_GAS_MARGINAL,
    EMPTY_ADDR_HEX,
    EMPTY_SHA3_BYTES,
    REVERSE_REGISTRAR_DOMAIN,
)
from ens.exceptions import (
    InvalidName,
)

default = object()


if TYPE_CHECKING:
    from web3 import Web3 as _Web3  # noqa: F401
    from web3.providers import (  # noqa: F401
        BaseProvider,
    )


def Web3() -> Type['_Web3']:
    from web3 import Web3 as Web3Main
    return Web3Main


TFunc = TypeVar("TFunc", bound=Callable[..., Any])


def dict_copy(func: TFunc) -> TFunc:
    "copy dict keyword args, to avoid modifying caller's copy"
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> TFunc:
        copied_kwargs = copy.deepcopy(kwargs)
        return func(*args, **copied_kwargs)
    return cast(TFunc, wrapper)


def ensure_hex(data: HexBytes) -> HexBytes:
    if not isinstance(data, str):
        return Web3().toHex(data)
    return data


def init_web3(provider: 'BaseProvider' = cast('BaseProvider', default)) -> '_Web3':
    from web3 import Web3 as Web3Main

    if provider is default:
        w3 = Web3Main(ens=None)
    else:
        w3 = Web3Main(provider, ens=None)

    return customize_web3(w3)


def customize_web3(w3: '_Web3') -> '_Web3':
    from web3.middleware import make_stalecheck_middleware

    w3.middleware_onion.remove('name_to_address')
    w3.middleware_onion.add(
        make_stalecheck_middleware(ACCEPTABLE_STALE_HOURS * 3600),
        name='stalecheck',
    )
    return w3


def normalize_name(name: str) -> str:
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
        return idna.uts46_remap(name, std3_rules=True)
    except idna.IDNAError as exc:
        raise InvalidName(f"{name} is an invalid name, because {exc}") from exc


def is_valid_name(name: str) -> bool:
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


def to_utc_datetime(timestamp: float) -> Optional[datetime.datetime]:
    if timestamp:
        return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
    else:
        return None


def sha3_text(val: Union[str, bytes]) -> HexBytes:
    if isinstance(val, str):
        val = val.encode('utf-8')
    return Web3().keccak(val)


def label_to_hash(label: str) -> HexBytes:
    label = normalize_name(label)
    if '.' in label:
        raise ValueError("Cannot generate hash for label %r with a '.'" % label)
    return Web3().keccak(text=label)


def normal_name_to_hash(name: str) -> HexBytes:
    node = EMPTY_SHA3_BYTES
    if name:
        labels = name.split(".")
        for label in reversed(labels):
            labelhash = label_to_hash(label)
            assert isinstance(labelhash, bytes)
            assert isinstance(node, bytes)
            node = Web3().keccak(node + labelhash)
    return node


def raw_name_to_hash(name: str) -> HexBytes:
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


def address_in(address: ChecksumAddress, addresses: Collection[ChecksumAddress]) -> bool:
    return any(is_same_address(address, item) for item in addresses)


def address_to_reverse_domain(address: ChecksumAddress) -> str:
    lower_unprefixed_address = remove_0x_prefix(HexStr(to_normalized_address(address)))
    return lower_unprefixed_address + '.' + REVERSE_REGISTRAR_DOMAIN


def estimate_auction_start_gas(labels: Collection[str]) -> int:
    return AUCTION_START_GAS_CONSTANT + AUCTION_START_GAS_MARGINAL * len(labels)


def assert_signer_in_modifier_kwargs(modifier_kwargs: Any) -> ChecksumAddress:
    ERR_MSG = "You must specify the sending account"
    assert len(modifier_kwargs) == 1, ERR_MSG

    _modifier_type, modifier_dict = dict(modifier_kwargs).popitem()
    if 'from' not in modifier_dict:
        raise TypeError(ERR_MSG)

    return modifier_dict['from']


def is_none_or_zero_address(addr: Union[Address, ChecksumAddress, HexAddress]) -> bool:
    return not addr or addr == EMPTY_ADDR_HEX


def is_valid_ens_name(ens_name: str) -> bool:
    split_domain = ens_name.split('.')
    if len(split_domain) == 1:
        return False
    for name in split_domain:
        if not is_valid_name(name):
            return False
    return True
