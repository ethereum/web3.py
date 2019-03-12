from eth_utils import (
    add_0x_prefix,
    apply_to_return_value,
    from_wei,
    is_address,
    is_checksum_address,
    keccak as eth_utils_keccak,
    remove_0x_prefix,
    to_checksum_address,
    to_wei,
)
from hexbytes import (
    HexBytes,
)

from ens import ENS
from web3._utils.abi import (
    map_abi_data,
)
from web3._utils.decorators import (
    combomethod,
    deprecated_for,
)
from web3._utils.empty import (
    empty,
)
from web3._utils.encoding import (
    hex_encode_abi_type,
    to_bytes,
    to_hex,
    to_int,
    to_text,
    to_json,
)
from web3._utils.module import (
    attach_modules,
)
from web3._utils.normalizers import (
    abi_ens_resolver,
)
from web3.eth import (
    Eth,
)
from web3.geth import (
    Geth,
    GethAdmin,
    GethMiner,
    GethPersonal,
    GethShh,
    GethTxPool,
)
from web3.iban import (
    Iban,
)
from web3.manager import (
    RequestManager as DefaultRequestManager,
)
from web3.net import (
    Net,
)
from web3.parity import (
    Parity,
    ParityPersonal,
    ParityShh,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.providers.ipc import (
    IPCProvider,
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
from web3.version import (
    Version,
)


def get_default_modules():
    return {
        "eth": (Eth,),
        "net": (Net,),
        "version": (Version,),
        "parity": (Parity, {
            "personal": (ParityPersonal,),
            "shh": (ParityShh,),
        }),
        "geth": (Geth, {
            "admin": (GethAdmin,),
            "miner": (GethMiner,),
            "personal": (GethPersonal,),
            "shh": (GethShh,),
            "txpool": (GethTxPool,),
        }),
        "testing": (Testing,),
    }


class Web3:
    # Providers
    HTTPProvider = HTTPProvider
    IPCProvider = IPCProvider
    EthereumTesterProvider = EthereumTesterProvider
    WebsocketProvider = WebsocketProvider

    # Managers
    RequestManager = DefaultRequestManager

    # Iban
    Iban = Iban

    # Encoding and Decoding
    toBytes = staticmethod(to_bytes)
    toInt = staticmethod(to_int)
    toHex = staticmethod(to_hex)
    toText = staticmethod(to_text)
    toJSON = staticmethod(to_json)

    # Currency Utility
    toWei = staticmethod(to_wei)
    fromWei = staticmethod(from_wei)

    # Address Utility
    isAddress = staticmethod(is_address)
    isChecksumAddress = staticmethod(is_checksum_address)
    toChecksumAddress = staticmethod(to_checksum_address)

    def __init__(self, provider=None, middlewares=None, modules=None, ens=empty):
        self.manager = self.RequestManager(self, provider, middlewares)

        if modules is None:
            modules = get_default_modules()

        attach_modules(self, modules)

        self.ens = ens

    @property
    def middleware_onion(self):
        return self.manager.middleware_onion

    @property
    def provider(self):
        return self.manager.provider

    @provider.setter
    def provider(self, provider):
        self.manager.provider = provider

    @property
    def clientVersion(self):
        return self.manager.request_blocking("web3_clientVersion", [])

    @property
    def api(self):
        from web3 import __version__
        return __version__

    @deprecated_for("keccak")
    @apply_to_return_value(HexBytes)
    def sha3(primitive=None, text=None, hexstr=None):
        return Web3.keccak(primitive, text, hexstr)

    @staticmethod
    @apply_to_return_value(HexBytes)
    def keccak(primitive=None, text=None, hexstr=None):
        if isinstance(primitive, (bytes, int, type(None))):
            input_bytes = to_bytes(primitive, hexstr=hexstr, text=text)
            return eth_utils_keccak(input_bytes)

        raise TypeError(
            "You called keccak with first arg %r and keywords %r. You must call it with one of "
            "these approaches: keccak(text='txt'), keccak(hexstr='0x747874'), "
            "keccak(b'\\x74\\x78\\x74'), or keccak(0x747874)." % (
                primitive,
                {'text': text, 'hexstr': hexstr}
            )
        )

    @combomethod
    @deprecated_for("solidityKeccak")
    def soliditySha3(cls, abi_types, values):
        return cls.solidityKeccak(abi_types, values)

    @combomethod
    def solidityKeccak(cls, abi_types, values):
        """
        Executes keccak256 exactly as Solidity does.
        Takes list of abi_types as inputs -- `[uint24, int8[], bool]`
        and list of corresponding values  -- `[20, [-1, 5, 0], True]`
        """
        if len(abi_types) != len(values):
            raise ValueError(
                "Length mismatch between provided abi types and values.  Got "
                "{0} types and {1} values.".format(len(abi_types), len(values))
            )

        if isinstance(cls, type):
            w3 = None
        else:
            w3 = cls
        normalized_values = map_abi_data([abi_ens_resolver(w3)], abi_types, values)

        hex_string = add_0x_prefix(''.join(
            remove_0x_prefix(hex_encode_abi_type(abi_type, value))
            for abi_type, value
            in zip(abi_types, normalized_values)
        ))
        return cls.keccak(hexstr=hex_string)

    def isConnected(self):
        return self.provider.isConnected()

    @property
    def ens(self):
        if self._ens is empty:
            return ENS.fromWeb3(self)
        else:
            return self._ens

    @ens.setter
    def ens(self, new_ens):
        self._ens = new_ens

    @property
    def pm(self):
        if hasattr(self, '_pm'):
            return self._pm
        else:
            raise AttributeError(
                "The Package Management feature is disabled by default until "
                "its API stabilizes. To use these features, please enable them by running "
                "`w3.enable_unstable_package_management_api()` and try again."
            )

    def enable_unstable_package_management_api(self):
        from web3.pm import PM
        PM.attach(self, '_pm')
