from io import (
    UnsupportedOperation,
)
import pytest

from eth_utils import (
    is_integer,
)

from web3 import (
    Web3,
)
from web3._utils.module import (
    attach_modules,
)
from web3.exceptions import (
    Web3AttributeError,
    Web3ValidationError,
)
from web3.module import (
    Module,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


class MockEth(Module):
    def block_number(self):
        return 42


class MockGeth(Module):
    pass


class MockGethAdmin(Module):
    def start_ws(self):
        return True


def test_attach_modules():
    mods = {
        "geth": (
            MockGeth,
            {
                "admin": MockGethAdmin,
            },
        ),
        "eth": MockEth,
    }
    w3 = Web3(EthereumTesterProvider(), modules={})
    attach_modules(w3, mods)
    assert w3.eth.block_number() == 42
    assert w3.geth.admin.start_ws() is True


def test_attach_single_module_as_tuple():
    w3 = Web3(EthereumTesterProvider(), modules={"eth": (MockEth,)})
    assert w3.eth.block_number() == 42


def test_attach_modules_multiple_levels_deep(module1):
    mods = {
        "eth": MockEth,
        "geth": (
            MockGeth,
            {
                "module1": (
                    module1,
                    {
                        "admin": MockGethAdmin,
                    },
                ),
            },
        ),
    }
    w3 = Web3(EthereumTesterProvider(), modules={})
    attach_modules(w3, mods)
    assert w3.eth.block_number() == 42
    assert w3.geth.module1.admin.start_ws() is True


def test_attach_modules_with_wrong_module_format():
    mods = {"eth": (MockEth, MockEth, MockEth)}
    w3 = Web3(EthereumTesterProvider, modules={})
    with pytest.raises(
        Web3ValidationError, match="Module definitions can only have 1 or 2 elements"
    ):
        attach_modules(w3, mods)


def test_attach_modules_with_existing_modules():
    mods = {
        "eth": MockEth,
    }
    w3 = Web3(EthereumTesterProvider, modules=mods)
    with pytest.raises(
        Web3AttributeError,
        match=("The web3 object already has an attribute with that name"),
    ):
        attach_modules(w3, mods)


def test_attach_external_modules_multiple_levels_deep(
    module1, module2, module3, module4
):
    w3 = Web3(
        EthereumTesterProvider(),
        external_modules={
            "module1": module1,
            "module2": (
                module2,
                {
                    "submodule1": (
                        module3,
                        {
                            "submodule2": module4,
                        },
                    ),
                },
            ),
        },
    )

    assert w3.is_connected()

    # assert instantiated with default modules
    assert hasattr(w3, "geth")
    assert hasattr(w3, "eth")
    assert is_integer(w3.eth.chain_id)

    # assert instantiated with module1
    assert hasattr(w3, "module1")
    assert w3.module1.a == "a"
    assert w3.module1.b == "b"

    # assert instantiated with module2 + submodules
    assert hasattr(w3, "module2")
    assert w3.module2.c == "c"
    assert w3.module2.d() == "d"

    assert hasattr(w3.module2, "submodule1")
    assert w3.module2.submodule1.e == "e"
    assert hasattr(w3.module2.submodule1, "submodule2")
    assert w3.module2.submodule1.submodule2.f == "f"


def test_attach_external_modules_that_do_not_inherit_from_module_class(
    module1_unique,
    module2_unique,
    module3_unique,
    module4_unique,
):
    w3 = Web3(
        EthereumTesterProvider(),
        external_modules={
            "module1": module1_unique,
            "module2": (
                module2_unique,
                {
                    "submodule1": (
                        module3_unique,
                        {
                            "submodule2": module4_unique,
                        },
                    ),
                },
            ),
        },
    )

    # assert module1 attached
    assert hasattr(w3, "module1")
    assert w3.module1.a == "a"
    assert w3.module1.b() == "b"
    assert w3.module1.return_eth_chain_id == w3.eth.chain_id

    # assert module2 + submodules attached
    assert hasattr(w3, "module2")
    assert w3.module2.c == "c"
    assert w3.module2.d() == "d"

    assert hasattr(w3.module2, "submodule1")
    assert w3.module2.submodule1.e == "e"
    assert hasattr(w3.module2.submodule1, "submodule2")
    assert w3.module2.submodule1.submodule2.f == "f"

    # assert default modules intact
    assert hasattr(w3, "geth")
    assert hasattr(w3, "eth")
    assert is_integer(w3.eth.chain_id)


def test_attach_modules_for_module_with_more_than_one_init_argument(
    module_many_init_args,
):
    with pytest.raises(
        UnsupportedOperation,
        match=(
            "A module class may accept a single `Web3` instance as "
            "the first argument of its __init__\\(\\) method. More "
            "than one argument found for ModuleManyArgs: \\['a', 'b']"
        ),
    ):
        Web3(
            EthereumTesterProvider(),
            external_modules={"module_should_fail": module_many_init_args},
        )
