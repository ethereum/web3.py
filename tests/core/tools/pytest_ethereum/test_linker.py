import pytest

from ethpm import (
    ASSETS_DIR,
    Package,
)
from web3.tools.pytest_ethereum.deployer import (
    Deployer,
)
from web3.tools.pytest_ethereum.exceptions import (
    DeployerError,
)
from web3.tools.pytest_ethereum.linker import (
    deploy,
    link,
    linker,
    run_python,
)


@pytest.fixture
def escrow_deployer(deployer):
    escrow_manifest_path = ASSETS_DIR / "escrow" / "with_bytecode_v3.json"
    return deployer(escrow_manifest_path)


def test_linker(escrow_deployer, w3):
    # todo test multiple links in one type
    assert isinstance(escrow_deployer, Deployer)
    with pytest.raises(DeployerError):
        escrow_deployer.deploy("Escrow")

    escrow_strategy = linker(
        deploy("SafeSendLib"),
        link("Escrow", "SafeSendLib"),
        deploy("Escrow", w3.eth.accounts[0]),
    )
    assert hasattr(escrow_strategy, "__call__")
    escrow_deployer.register_strategy("Escrow", escrow_strategy)
    linked_escrow_package = escrow_deployer.deploy("Escrow")
    assert isinstance(linked_escrow_package, Package)
    linked_escrow_factory = linked_escrow_package.get_contract_factory("Escrow")
    assert linked_escrow_factory.needs_bytecode_linking is False


def test_linker_with_from(escrow_deployer, w3):
    escrow_strategy = linker(
        deploy("SafeSendLib"),
        link("Escrow", "SafeSendLib"),
        deploy("Escrow", w3.eth.accounts[0], transaction={"from": w3.eth.accounts[5]}),
    )
    escrow_deployer.register_strategy("Escrow", escrow_strategy)
    linked_escrow_package = escrow_deployer.deploy("Escrow")
    escrow_instance = linked_escrow_package.deployments.get_instance("Escrow")
    assert escrow_instance.functions.sender().call() == w3.eth.accounts[5]


def test_linker_with_callback(escrow_deployer, w3):
    sender = w3.eth.accounts[0]
    recipient = w3.eth.accounts[5]

    def callback_fn(package):
        escrow_instance = package.deployments.get_instance("Escrow")
        tx_hash = escrow_instance.functions.releaseFunds().transact({"from": sender})
        w3.eth.waitForTransactionReceipt(tx_hash)

    escrow_strategy = linker(
        deploy("SafeSendLib", transaction={"from": sender}),
        link("Escrow", "SafeSendLib"),
        deploy(
            "Escrow",
            recipient,
            transaction={"from": sender, "value": w3.toWei("1", "ether")},
        ),
        run_python(callback_fn),
    )
    escrow_deployer.register_strategy("Escrow", escrow_strategy)
    assert w3.eth.get_balance(recipient) == w3.toWei("1000000", "ether")
    linked_escrow_package = escrow_deployer.deploy("Escrow")
    escrow_instance = linked_escrow_package.deployments.get_instance("Escrow")
    assert escrow_instance.functions.sender().call() == sender
    assert w3.eth.get_balance(recipient) == w3.toWei("1000001", "ether")
