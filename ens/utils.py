from datetime import (
    datetime,
    timezone,
)
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
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
    to_bytes,
    to_normalized_address,
)
from eth_utils.abi import (
    collapse_if_tuple,
)
from hexbytes import (
    HexBytes,
)

from ._normalization import (
    normalize_name_ensip15,
)
from .constants import (
    ACCEPTABLE_STALE_HOURS,
    AUCTION_START_GAS_CONSTANT,
    AUCTION_START_GAS_MARGINAL,
    EMPTY_ADDR_HEX,
    EMPTY_SHA3_BYTES,
    REVERSE_REGISTRAR_DOMAIN,
)
from .exceptions import (
    ENSValidationError,
    InvalidName,
)

default = object()


if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3 as _Web3,
    )
    from web3.providers import (  # noqa: F401
        AsyncBaseProvider,
        BaseProvider,
    )
    from web3.types import (  # noqa: F401
        ABIFunction,
        AsyncMiddleware,
        Middleware,
        RPCEndpoint,
    )


def Web3() -> Type["_Web3"]:
    from web3 import (
        Web3 as Web3Main,
    )

    return Web3Main


def init_web3(
    provider: "BaseProvider" = cast("BaseProvider", default),
    middlewares: Optional[Sequence[Tuple["Middleware", str]]] = None,
) -> "_Web3":
    from web3 import (
        Web3 as Web3Main,
    )
    from web3.eth import (
        Eth as EthMain,
    )

    if provider is default:
        w3 = Web3Main(ens=None, modules={"eth": (EthMain)})
    else:
        w3 = Web3Main(provider, middlewares, ens=None, modules={"eth": (EthMain)})

    return customize_web3(w3)


def customize_web3(w3: "_Web3") -> "_Web3":
    from web3.middleware import (
        make_stalecheck_middleware,
    )

    if w3.middleware_onion.get("name_to_address"):
        w3.middleware_onion.remove("name_to_address")

    if not w3.middleware_onion.get("stalecheck"):
        w3.middleware_onion.add(
            make_stalecheck_middleware(ACCEPTABLE_STALE_HOURS * 3600), name="stalecheck"
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
    if is_empty_name(name):
        return ""
    elif isinstance(name, (bytes, bytearray)):
        name = name.decode("utf-8")

    return normalize_name_ensip15(name).as_text


def ens_encode_name(name: str) -> bytes:
    """
    Encode a name according to DNS standards specified in section 3.1
    of RFC1035 with the following validations:

        - There is no limit on the total length of the encoded name
        and the limit on labels is the ENS standard of 255.

        - Return a single 0-octet, b'\x00', if empty name.

    :param str name: the dot-separated ENS name
    """
    if is_empty_name(name):
        return b"\x00"

    normalized_name = normalize_name(name)

    labels = normalized_name.split(".")
    labels_as_bytes = [to_bytes(text=label) for label in labels]

    # raises if len(label) > 255:
    for index, label in enumerate(labels):
        if len(label) > 255:
            raise ENSValidationError(
                f"Label at position {index} too long after encoding."
            )

    # concat label size in bytes to each label:
    dns_prepped_labels = [to_bytes(len(label)) + label for label in labels_as_bytes]

    # return the joined prepped labels in order and append the zero byte at the end:
    return b"".join(dns_prepped_labels) + b"\x00"


def is_valid_name(name: str) -> bool:
    """
    Validate whether the fully qualified name is valid, as defined in ENS `EIP-137
    <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#name-syntax>`_

    :param str name: the dot-separated ENS name
    :returns: True if ``name`` is set, and :meth:`~ens.ENS.nameprep` will not
              raise InvalidName
    """
    if is_empty_name(name):
        return False
    try:
        normalize_name(name)
        return True
    except InvalidName:
        return False


def to_utc_datetime(timestamp: float) -> Optional[datetime]:
    return datetime.fromtimestamp(timestamp, timezone.utc) if timestamp else None


def sha3_text(val: Union[str, bytes]) -> HexBytes:
    if isinstance(val, str):
        val = val.encode("utf-8")
    return Web3().keccak(val)


def label_to_hash(label: str) -> HexBytes:
    label = normalize_name(label)
    if "." in label:
        raise ValueError(f"Cannot generate hash for label {label!r} with a '.'")
    return Web3().keccak(text=label)


def normal_name_to_hash(name: str) -> HexBytes:
    """
    This method will not normalize the name. 'normal' name here means the name
    should already be normalized before calling this method.

    :param name:            the name to hash - should already be normalized
    :return: namehash       the hash of the name
    :rtype: HexBytes
    """
    node = EMPTY_SHA3_BYTES
    if not is_empty_name(name):
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


def address_in(
    address: ChecksumAddress, addresses: Collection[ChecksumAddress]
) -> bool:
    return any(is_same_address(address, item) for item in addresses)


def address_to_reverse_domain(address: ChecksumAddress) -> str:
    lower_unprefixed_address = remove_0x_prefix(HexStr(to_normalized_address(address)))
    return lower_unprefixed_address + "." + REVERSE_REGISTRAR_DOMAIN


def estimate_auction_start_gas(labels: Collection[str]) -> int:
    return AUCTION_START_GAS_CONSTANT + AUCTION_START_GAS_MARGINAL * len(labels)


def assert_signer_in_modifier_kwargs(modifier_kwargs: Any) -> ChecksumAddress:
    ERR_MSG = "You must specify the sending account"
    assert len(modifier_kwargs) == 1, ERR_MSG

    _modifier_type, modifier_dict = dict(modifier_kwargs).popitem()
    if "from" not in modifier_dict:
        raise TypeError(ERR_MSG)

    return modifier_dict["from"]


def is_none_or_zero_address(addr: Union[Address, ChecksumAddress, HexAddress]) -> bool:
    return not addr or addr == EMPTY_ADDR_HEX


def is_empty_name(name: str) -> bool:
    return name is None or name.strip() in {"", "."}


def is_valid_ens_name(ens_name: str) -> bool:
    split_domain = ens_name.split(".")
    if len(split_domain) == 1:
        return False
    for name in split_domain:
        if not is_valid_name(name):
            return False
    return True


# borrowed from similar method at `web3._utils.abi` due to circular dependency
def get_abi_output_types(abi: "ABIFunction") -> List[str]:
    return (
        []
        if abi["type"] == "fallback"
        else [collapse_if_tuple(cast(Dict[str, Any], arg)) for arg in abi["outputs"]]
    )


# -- async -- #


def init_async_web3(
    provider: "AsyncBaseProvider" = cast("AsyncBaseProvider", default),
    middlewares: Optional[Sequence[Tuple["AsyncMiddleware", str]]] = (),
) -> "AsyncWeb3":
    from web3 import (
        AsyncWeb3 as AsyncWeb3Main,
    )
    from web3.eth import (
        AsyncEth as AsyncEthMain,
    )

    middlewares = list(middlewares)
    for i, (middleware, name) in enumerate(middlewares):
        if name == "name_to_address":
            middlewares.pop(i)

    if "stalecheck" not in (name for mw, name in middlewares):
        middlewares.append((_async_ens_stalecheck_middleware, "stalecheck"))

    if provider is default:
        async_w3 = AsyncWeb3Main(
            middlewares=middlewares, ens=None, modules={"eth": (AsyncEthMain)}
        )
    else:
        async_w3 = AsyncWeb3Main(
            provider,
            middlewares=middlewares,
            ens=None,
            modules={"eth": (AsyncEthMain)},
        )

    return async_w3


async def _async_ens_stalecheck_middleware(
    make_request: Callable[["RPCEndpoint", Any], Any], w3: "AsyncWeb3"
) -> "Middleware":
    from web3.middleware import (
        async_make_stalecheck_middleware,
    )

    middleware = await async_make_stalecheck_middleware(ACCEPTABLE_STALE_HOURS * 3600)
    return await middleware(make_request, w3)
