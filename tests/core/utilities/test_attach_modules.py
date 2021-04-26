import pytest

from web3 import Web3
from web3._utils.module import (
    attach_modules,
)
from web3.exceptions import (
    ValidationError,
)
from web3.module import (
    ModuleV2,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


class MockEth(ModuleV2):
    def block_number(self):
        return 42


class MockGeth(ModuleV2):
    pass


class MockGethAdmin(ModuleV2):
    def start_ws(self):
        return True


class MockGethPersonal(ModuleV2):
    def unlock_account(self):
        return True


def test_attach_modules():
    mods = {
        "geth": (MockGeth, {
            "personal": (MockGethPersonal,),
            "admin": (MockGethAdmin,),
        }),
        "eth": (MockEth,),
    }
    w3 = Web3(EthereumTesterProvider(), modules={})
    attach_modules(w3, mods)
    assert w3.eth.block_number() == 42
    assert w3.geth.personal.unlock_account() is True
    assert w3.geth.admin.start_ws() is True


def test_attach_modules_multiple_levels_deep():
    mods = {
        "eth": (MockEth,),
        "geth": (MockGeth, {
            "personal": (MockGethPersonal, {
                "admin": (MockGethAdmin,),
            }),
        }),
    }
    w3 = Web3(EthereumTesterProvider(), modules={})
    attach_modules(w3, mods)
    assert w3.eth.block_number() == 42
    assert w3.geth.personal.unlock_account() is True
    assert w3.geth.personal.admin.start_ws() is True


def test_attach_modules_with_wrong_module_format():
    mods = {
        "eth": (MockEth, MockGeth, MockGethPersonal)
    }
    w3 = Web3(EthereumTesterProvider, modules={})
    with pytest.raises(ValidationError, match="Module definitions can only have 1 or 2 elements"):
        attach_modules(w3, mods)


def test_attach_modules_with_existing_modules():
    mods = {
        "eth": (MockEth,),
    }
    w3 = Web3(EthereumTesterProvider, modules=mods)
    with pytest.raises(AttributeError,
                       match="The web3 object already has an attribute with that name"):
        attach_modules(w3, mods)
