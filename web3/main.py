from eth_utils import (
    apply_to_return_value,
    add_0x_prefix,
    from_wei,
    is_address,
    is_checksum_address,
    keccak,
    remove_0x_prefix,
    to_checksum_address,
    to_wei,
)

from ens import ENS

from web3.admin import Admin
from web3.eth import Eth
from web3.iban import Iban
from web3.miner import Miner
from web3.net import Net
from web3.parity import Parity
from web3.personal import Personal
from web3.testing import Testing
from web3.txpool import TxPool
from web3.version import Version

from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.providers.ipc import (
    IPCProvider,
)
from web3.providers.rpc import (
    HTTPProvider,
)
from web3.providers.tester import (
    TestRPCProvider,
)
from web3.providers.websocket import (
    WebsocketProvider
)

from web3.manager import (
    RequestManager,
)

from web3.utils.abi import (
    map_abi_data,
)
from hexbytes import (
    HexBytes,
)
from web3.utils.decorators import (
    combomethod,
)
from web3.utils.empty import empty
from web3.utils.encoding import (
    hex_encode_abi_type,
    to_bytes,
    to_int,
    to_hex,
    to_text,
)
from web3.utils.normalizers import (
    abi_ens_resolver,
)


def get_default_modules():
    return {
        "eth": Eth,
        "net": Net,
        "personal": Personal,
        "version": Version,
        "txpool": TxPool,
        "miner": Miner,
        "admin": Admin,
        "parity": Parity,
        "testing": Testing,
    }


class Web3:
    # Providers
    HTTPProvider = HTTPProvider
    IPCProvider = IPCProvider
    TestRPCProvider = TestRPCProvider
    EthereumTesterProvider = EthereumTesterProvider
    WebsocketProvider = WebsocketProvider

    # Managers
    RequestManager = RequestManager

    # Iban
    Iban = Iban

    # Encoding and Decoding
    toBytes = staticmethod(to_bytes)
    toInt = staticmethod(to_int)
    toHex = staticmethod(to_hex)
    toText = staticmethod(to_text)

    # Currency Utility
    toWei = staticmethod(to_wei)
    fromWei = staticmethod(from_wei)

    # Address Utility
    isAddress = staticmethod(is_address)
    isChecksumAddress = staticmethod(is_checksum_address)
    toChecksumAddress = staticmethod(to_checksum_address)

    def __init__(self, providers=empty, middlewares=None, modules=None, ens=empty):
        self.manager = RequestManager(self, providers, middlewares)

        if modules is None:
            modules = get_default_modules()

        for module_name, module_class in modules.items():
            module_class.attach(self, module_name)

        self.ens = ens

    @property
    def middleware_stack(self):
        return self.manager.middleware_stack

    @property
    def providers(self):
        return self.manager.providers

    @providers.setter
    def providers(self, providers):
        self.manager.providers = providers

    @staticmethod
    @apply_to_return_value(HexBytes)
    def sha3(primitive=None, text=None, hexstr=None):
        if isinstance(primitive, (bytes, int, type(None))):
            input_bytes = to_bytes(primitive, hexstr=hexstr, text=text)
            return keccak(input_bytes)

        raise TypeError(
            "You called sha3 with first arg %r and keywords %r. You must call it with one of "
            "these approaches: sha3(text='txt'), sha3(hexstr='0x747874'), "
            "sha3(b'\\x74\\x78\\x74'), or sha3(0x747874)." % (
                primitive,
                {'text': text, 'hexstr': hexstr}
            )
        )

    @combomethod
    def soliditySha3(cls, abi_types, values):
        """
        Executes sha3 (keccak256) exactly as Solidity does.
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
        return cls.sha3(hexstr=hex_string)

    def isConnected(self):
        for provider in self.providers:
            if provider.isConnected():
                return True
        else:
            return False

    @property
    def ens(self):
        if self._ens is empty:
            return ENS.fromWeb3(self)
        else:
            return self._ens

    @ens.setter
    def ens(self, new_ens):
        self._ens = new_ens
