import decimal

from ens import (
    AsyncENS,
    ENS,
)
from eth_abi.codec import (
    ABICodec,
)
from eth_utils import (
    add_0x_prefix,
    apply_to_return_value,
    from_wei,
    is_address,
    is_checksum_address,
    keccak as eth_utils_keccak,
    remove_0x_prefix,
    to_bytes,
    to_checksum_address,
    to_int,
    to_text,
    to_wei,
)
from functools import (
    wraps,
)
from hexbytes import (
    HexBytes,
)
from typing import (
    Any,
    Coroutine,
    Dict,
    List,
    Optional,
    Sequence,
    Type,
    TYPE_CHECKING,
    Union,
    cast,
)

from eth_typing import (
    AnyAddress,
    ChecksumAddress,
    HexStr,
    Primitives,
)
from eth_typing.abi import TypeStr
from eth_utils import (
    combomethod,
)

from web3._utils.abi import (
    build_default_registry,
    build_strict_registry,
    map_abi_data,
)
from web3._utils.empty import (
    empty,
)
from web3._utils.encoding import (
    hex_encode_abi_type,
    to_hex,
    to_json,
)
from web3._utils.rpc_abi import (
    RPC,
)
from web3._utils.module import (
    attach_modules as _attach_modules,
)
from web3._utils.normalizers import (
    abi_ens_resolver,
)
from web3.eth import (
    AsyncEth,
    Eth,
)
from web3.geth import (
    AsyncGethAdmin,
    AsyncGethPersonal,
    AsyncGethTxPool,
    Geth,
    GethAdmin,
    GethMiner,
    GethPersonal,
    GethTxPool,
)
from web3.manager import (
    RequestManager as DefaultRequestManager,
)
from web3.module import (
    Module,
)
from web3.net import (
    AsyncNet,
    Net,
)
from web3.providers import (
    AsyncBaseProvider,
    BaseProvider,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.providers.ipc import (
    IPCProvider,
)
from web3.providers.async_rpc import (
    AsyncHTTPProvider,
)
from web3.providers.rpc import (
    HTTPProvider,
)
from web3.providers.websocket import (
    WebsocketProvider,
)
from web3.testing import (
    Testing,
)
from web3.types import (  # noqa: F401
    Middleware,
    MiddlewareOnion,
    Wei,
)

if TYPE_CHECKING:
    from web3.pm import PM  # noqa: F401
    from web3._utils.empty import Empty  # noqa: F401


def get_async_default_modules() -> Dict[str, Union[Type[Module], Sequence[Any]]]:
    return {
        "eth": AsyncEth,
        "net": AsyncNet,
        "geth": (
            Geth,
            {
                "admin": AsyncGethAdmin,
                "personal": AsyncGethPersonal,
                "txpool": AsyncGethTxPool,
            },
        ),
    }


def get_default_modules() -> Dict[str, Union[Type[Module], Sequence[Any]]]:
    return {
        "eth": Eth,
        "net": Net,
        "geth": (
            Geth,
            {
                "admin": GethAdmin,
                "miner": GethMiner,
                "personal": GethPersonal,
                "txpool": GethTxPool,
            },
        ),
        "testing": Testing,
    }


class Web3:
    # Providers
    HTTPProvider = HTTPProvider
    IPCProvider = IPCProvider
    EthereumTesterProvider = EthereumTesterProvider
    WebsocketProvider = WebsocketProvider
    AsyncHTTPProvider = AsyncHTTPProvider

    # Managers
    RequestManager = DefaultRequestManager

    # Encoding and Decoding
    @staticmethod
    @wraps(to_bytes)
    def to_bytes(
        primitive: Primitives = None, hexstr: HexStr = None, text: str = None
    ) -> bytes:
        return to_bytes(primitive, hexstr, text)

    @staticmethod
    @wraps(to_int)
    def to_int(
        primitive: Primitives = None, hexstr: HexStr = None, text: str = None
    ) -> int:
        return to_int(primitive, hexstr, text)

    @staticmethod
    @wraps(to_hex)
    def to_hex(
        primitive: Primitives = None, hexstr: HexStr = None, text: str = None
    ) -> HexStr:
        return to_hex(primitive, hexstr, text)

    @staticmethod
    @wraps(to_text)
    def to_text(
        primitive: Primitives = None, hexstr: HexStr = None, text: str = None
    ) -> str:
        return to_text(primitive, hexstr, text)

    @staticmethod
    @wraps(to_json)
    def to_json(obj: Dict[Any, Any]) -> str:
        return to_json(obj)

    # Currency Utility
    @staticmethod
    @wraps(to_wei)
    def to_wei(number: Union[int, float, str, decimal.Decimal], unit: str) -> Wei:
        return cast(Wei, to_wei(number, unit))

    @staticmethod
    @wraps(from_wei)
    def from_wei(number: int, unit: str) -> Union[int, decimal.Decimal]:
        return from_wei(number, unit)

    # Address Utility
    @staticmethod
    @wraps(is_address)
    def is_address(value: Any) -> bool:
        return is_address(value)

    @staticmethod
    @wraps(is_checksum_address)
    def is_checksum_address(value: Any) -> bool:
        return is_checksum_address(value)

    @staticmethod
    @wraps(to_checksum_address)
    def to_checksum_address(value: Union[AnyAddress, str, bytes]) -> ChecksumAddress:
        return to_checksum_address(value)

    # mypy Types
    eth: Eth
    geth: Geth
    net: Net

    def __init__(
        self,
        provider: Optional[Union[BaseProvider, AsyncBaseProvider]] = None,
        middlewares: Optional[Sequence[Any]] = None,
        modules: Optional[Dict[str, Union[Type[Module], Sequence[Any]]]] = None,
        external_modules: Optional[
            Dict[str, Union[Type[Module], Sequence[Any]]]
        ] = None,
        ens: Union[ENS, AsyncENS, "Empty"] = empty,
    ) -> None:
        self.manager = self.RequestManager(self, provider, middlewares)
        # this codec gets used in the module initialization,
        # so it needs to come before attach_modules
        self.codec = ABICodec(build_default_registry())

        if modules is None:
            modules = (
                get_async_default_modules()
                if provider and provider.is_async
                else get_default_modules()
            )

        self.attach_modules(modules)

        if external_modules is not None:
            self.attach_modules(external_modules)

        self.ens = ens

    @property
    def middleware_onion(self) -> MiddlewareOnion:
        return self.manager.middleware_onion

    @property
    def provider(self) -> Union[BaseProvider, AsyncBaseProvider]:
        return self.manager.provider

    @provider.setter
    def provider(self, provider: Union[BaseProvider, AsyncBaseProvider]) -> None:
        self.manager.provider = provider

    @property
    def client_version(self) -> str:
        return self.manager.request_blocking(RPC.web3_clientVersion, [])

    @property
    def api(self) -> str:
        from web3 import __version__

        return __version__

    @staticmethod
    @apply_to_return_value(HexBytes)
    def keccak(
        primitive: Optional[Primitives] = None,
        text: Optional[str] = None,
        hexstr: Optional[HexStr] = None,
    ) -> bytes:
        if isinstance(primitive, (bytes, int, type(None))):
            input_bytes = to_bytes(primitive, hexstr=hexstr, text=text)
            return eth_utils_keccak(input_bytes)

        raise TypeError(
            f"You called keccak with first arg {primitive!r} and keywords "
            f"{{'text': {text!r}, 'hexstr': {hexstr!r}}}. You must call it with "
            "one of these approaches: keccak(text='txt'), keccak(hexstr='0x747874'), "
            "keccak(b'\\x74\\x78\\x74'), or keccak(0x747874)."
        )

    @combomethod
    def solidity_keccak(cls, abi_types: List[TypeStr], values: List[Any]) -> bytes:
        """
        Executes keccak256 exactly as Solidity does.
        Takes list of abi_types as inputs -- `[uint24, int8[], bool]`
        and list of corresponding values  -- `[20, [-1, 5, 0], True]`
        """
        if len(abi_types) != len(values):
            raise ValueError(
                "Length mismatch between provided abi types and values.  Got "
                f"{len(abi_types)} types and {len(values)} values."
            )

        if isinstance(cls, type):
            w3 = None
        else:
            w3 = cls
        normalized_values = map_abi_data([abi_ens_resolver(w3)], abi_types, values)

        hex_string = add_0x_prefix(
            HexStr(
                "".join(
                    remove_0x_prefix(hex_encode_abi_type(abi_type, value))
                    for abi_type, value in zip(abi_types, normalized_values)
                )
            )
        )
        return cls.keccak(hexstr=hex_string)

    def attach_modules(
        self, modules: Optional[Dict[str, Union[Type[Module], Sequence[Any]]]]
    ) -> None:
        """
        Attach modules to the `Web3` instance.
        """
        _attach_modules(self, modules)

    def is_connected(self) -> Union[bool, Coroutine[Any, Any, bool]]:
        return self.provider.is_connected()

    def is_encodable(self, _type: TypeStr, value: Any) -> bool:
        return self.codec.is_encodable(_type, value)

    @property
    def ens(self) -> Union[ENS, AsyncENS, "Empty"]:
        if self._ens is empty:
            return (
                AsyncENS.from_web3(self) if self.eth.is_async else ENS.from_web3(self)
            )

        return self._ens

    @ens.setter
    def ens(self, new_ens: Union[ENS, AsyncENS, "Empty"]) -> None:
        self._ens = new_ens

    @property
    def pm(self) -> "PM":
        if hasattr(self, "_pm"):
            # ignored b/c property is dynamically set
            # via enable_unstable_package_management_api
            return self._pm  # type: ignore
        else:
            raise AttributeError(
                "The Package Management feature is disabled by default until "
                "its API stabilizes. To use these features, please enable them by "
                "running `w3.enable_unstable_package_management_api()` and try again."
            )

    def enable_unstable_package_management_api(self) -> None:
        from web3.pm import PM  # noqa: F811

        if not hasattr(self, "_pm"):
            self.attach_modules({"_pm": PM})

    def enable_strict_bytes_type_checking(self) -> None:
        self.codec = ABICodec(build_strict_registry())
