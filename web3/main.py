from __future__ import absolute_import
import codecs
import re

from eth_utils import (
    to_wei,
    from_wei,
    is_0x_prefixed,
    is_address,
    is_checksum_address,
    to_checksum_address,
    decode_hex,
    encode_hex,
    force_text,
    coerce_return_to_text,
    add_0x_prefix,
    remove_0x_prefix,
)

from toolz.functoolz import (
    compose,
)

from web3.admin import Admin
from web3.db import Db
from web3.eth import Eth
from web3.miner import Miner
from web3.net import Net
from web3.personal import Personal
from web3.shh import Shh
from web3.txpool import TxPool
from web3.version import Version
from web3.testing import Testing

from web3.iban import Iban

from web3.providers.rpc import (
    HTTPProvider,
    RPCProvider,
    KeepAliveRPCProvider,
)
from web3.providers.tester import (
    TestRPCProvider,
    EthereumTesterProvider,
)
from web3.providers.ipc import (
    IPCProvider,
)
from web3.providers.manager import (
    RequestManager,
)
from web3.utils.abi import (
    is_address_type,
    is_array_type,
    is_bool_type,
    is_bytes_type,
    is_int_type,
    is_uint_type,
    is_string_type,
    size_of_type,
)
from web3.utils.encoding import (
    to_hex,
    to_decimal,
    from_decimal,
)


class Web3(object):
    # Providers
    HTTPProvider = HTTPProvider
    RPCProvider = RPCProvider
    KeepAliveRPCProvider = KeepAliveRPCProvider
    IPCProvider = IPCProvider
    TestRPCProvider = TestRPCProvider
    EthereumTesterProvider = EthereumTesterProvider

    # Managers
    RequestManager = RequestManager

    # Iban
    Iban = Iban

    # Encoding and Decoding
    toHex = staticmethod(to_hex)
    toAscii = staticmethod(decode_hex)
    toUtf8 = staticmethod(compose(force_text, decode_hex))
    fromAscii = staticmethod(encode_hex)
    fromUtf8 = staticmethod(encode_hex)
    toDecimal = staticmethod(to_decimal)
    fromDecimal = staticmethod(from_decimal)

    # Currency Utility
    toWei = staticmethod(to_wei)
    fromWei = staticmethod(from_wei)

    # Address Utility
    isAddress = staticmethod(is_address)
    isChecksumAddress = staticmethod(is_checksum_address)
    toChecksumAddress = staticmethod(to_checksum_address)

    def __init__(self, provider):
        self._requestManager = RequestManager(provider)

        self.eth = Eth(self)
        self.db = Db(self)
        self.shh = Shh(self)
        self.net = Net(self)
        self.personal = Personal(self)
        self.version = Version(self)
        self.txpool = TxPool(self)
        self.miner = Miner(self)
        self.admin = Admin(self)
        self.testing = Testing(self)

    def setProvider(self, provider):
        self._requestManager.setProvider(provider)

    def setManager(self, manager):
        self._requestManager = manager

    @property
    def currentProvider(self):
        return self._requestManager.provider

    @coerce_return_to_text
    def sha3(self, value, encoding="hex"):
        if encoding == 'hex':
            hex_string = value
        else:
            hex_string = encode_hex(value)
        return self._requestManager.request_blocking('web3_sha3', [hex_string])

    def soliditySha3(self, types, values):
        hex_string = ''
        for abi_type, value in zip(types, values):
            hex_string += hex_encode_abi_type(abi_type, value)

        hex_string = add_0x_prefix(hex_string)
        return self.sha3(hex_string)

    def isConnected(self):
        return self.currentProvider is not None and self.currentProvider.isConnected()

    def createBatch(self):
        raise NotImplementedError("Not Implemented")

    def receive(self, requestid, timeout=0, keep=False):
        return self._requestManager.receive(requestid, timeout, keep)


def hex_encode_abi_type(abi_type, value):
    if is_array_type(abi_type):
        sub_type = re.sub(r"\[[^]]*\]$", "", abi_type, 1)
        return "".join([hex_encode_abi_type(sub_type, v) for v in value])
    elif is_bool_type(abi_type):
        return remove_0x_prefix(hex(value)).zfill(2)
    elif is_uint_type(abi_type):
        return positive_int_to_hex(value, size_of_type(abi_type))
    elif is_int_type(abi_type):
        bit_size = size_of_type(abi_type)
        if value < 0:
            return twos_compliment_of_negative(value, bit_size)
        else:
            return positive_int_to_hex(value, bit_size)
    elif is_address_type(abi_type):
        return remove_0x_prefix(value)
    elif is_bytes_type(abi_type):
        if is_0x_prefixed(value):
            return remove_0x_prefix(value)
        else:
            return bytes_to_hex(value)
    elif is_string_type(abi_type):
        return bytes_to_hex(value)


def positive_int_to_hex(value, bit_size=None):
    hex_value = remove_0x_prefix(hex(value))
    if bit_size:
        return hex_value.zfill(int(bit_size / 4))
    return ('0' * (len(hex_value) % 2)) + hex_value


def twos_compliment_of_negative(value, bit_size):
    value = (1 << bit_size) + value
    hex_value = hex(value)
    hex_value = hex_value[:-1] if hex_value[-1] == "L" else hex_value
    return remove_0x_prefix(hex_value)


def bytes_to_hex(byte_string):
    if type(byte_string) == str:
        byte_string = str.encode(byte_string)
    return codecs.getencoder('hex')(byte_string)[0].decode("utf-8")
