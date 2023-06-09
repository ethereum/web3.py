import pytest

from eth_utils import (
    to_bytes,
)

from ens import (
    ENS,
)
from ethpm import (
    ASSETS_DIR,
)
from web3.exceptions import (
    InvalidAddress,
)
from web3.pm import (
    SimpleRegistry,
)


def bytes32(val):
    if isinstance(val, int):
        result = to_bytes(val)
    else:
        raise TypeError(f"{val!r} could not be converted to bytes")
    return result.rjust(32, b"\0")


@pytest.fixture
def ens_setup(deployer):
    # todo: move to module level once ethpm alpha stable
    ENS_MANIFEST = ASSETS_DIR / "ens" / "v3.json"
    ens_deployer = deployer(ENS_MANIFEST)
    w3 = ens_deployer.package.w3

    # ** Set up ENS contracts **

    # remove account that creates ENS, so test transactions don't have write access
    accounts = w3.eth.accounts
    ens_key = accounts.pop()

    # create ENS contract
    # values borrowed from:
    # https://github.com/ethereum/web3.py/blob/main/tests/ens/conftest.py#L109
    eth_labelhash = w3.keccak(text="eth")
    eth_namehash = bytes32(
        0x93CDEB708B7545DC668EB9280176169D1C33CFD8ED6F04690A0BCC88A93FC4AE
    )
    resolver_namehash = bytes32(
        0xFDD5D5DE6DD63DB72BBC2D487944BA13BF775B50A80805FE6FCABA9B0FBA88F5
    )
    ens_package = ens_deployer.deploy("ENSRegistry", transaction={"from": ens_key})
    ens_contract = ens_package.deployments.get_instance("ENSRegistry")

    # create public resolver
    public_resolver_package = ens_deployer.deploy(
        "PublicResolver", ens_contract.address, transaction={"from": ens_key}
    )
    public_resolver = public_resolver_package.deployments.get_instance("PublicResolver")

    # set 'resolver.eth' to resolve to public resolver
    ens_contract.functions.setSubnodeOwner(b"\0" * 32, eth_labelhash, ens_key).transact(
        {"from": ens_key}
    )

    ens_contract.functions.setSubnodeOwner(
        eth_namehash, w3.keccak(text="resolver"), ens_key
    ).transact({"from": ens_key})

    ens_contract.functions.setResolver(
        resolver_namehash, public_resolver.address
    ).transact({"from": ens_key})

    public_resolver.functions.setAddr(
        resolver_namehash, public_resolver.address
    ).transact({"from": ens_key})

    # create .eth auction registrar
    eth_registrar_package = ens_deployer.deploy(
        "FIFSRegistrar",
        ens_contract.address,
        eth_namehash,
        transaction={"from": ens_key},
    )
    eth_registrar = eth_registrar_package.deployments.get_instance("FIFSRegistrar")

    # set '.eth' to resolve to the registrar
    ens_contract.functions.setResolver(eth_namehash, public_resolver.address).transact(
        {"from": ens_key}
    )

    public_resolver.functions.setAddr(eth_namehash, eth_registrar.address).transact(
        {"from": ens_key}
    )

    # set owner of tester.eth to an account controlled by tests
    ens_contract.functions.setSubnodeOwner(
        eth_namehash,
        w3.keccak(text="tester"),
        w3.eth.accounts[
            2
        ],  # note that this does not have to be the default, only in the list
    ).transact({"from": ens_key})

    # make the registrar the owner of the 'eth' name
    ens_contract.functions.setSubnodeOwner(
        b"\0" * 32, eth_labelhash, eth_registrar.address
    ).transact({"from": ens_key})
    return ENS.from_web3(w3, ens_contract.address)


@pytest.fixture
def ens(ens_setup, mocker):
    mocker.patch("web3.middleware.stalecheck._is_fresh", return_value=True)
    ens_setup.w3.eth.default_account = ens_setup.w3.eth.coinbase
    with pytest.warns(
        UserWarning, match="The ``ethPM`` module is no longer being maintained"
    ):
        ens_setup.w3.enable_unstable_package_management_api()
    return ens_setup


def test_ens_must_be_set_before_ens_methods_can_be_used(ens):
    w3 = ens.w3
    with pytest.raises(InvalidAddress):
        w3.pm.set_registry("tester.eth")


@pytest.mark.xfail(reason="Need to properly add authorization as of 8/10/2022")
def test_web3_ens(ens):
    w3 = ens.w3
    ns = ENS.from_web3(w3, ens.ens.address)
    w3.ens = ns
    registry = SimpleRegistry.deploy_new_instance(w3)
    w3.ens.setup_address("tester.eth", registry.address)
    actual_addr = ens.address("tester.eth")
    w3.pm.set_registry("tester.eth")
    assert w3.pm.registry.address == actual_addr
    w3.pm.release_package(
        "owned", "1.0.0", "ipfs://QmcxvhkJJVpbxEAa6cgW3B6XwPJb79w9GpNUv2P2THUzZR"
    )
    pkg_name, version, manifest_uri = w3.pm.get_release_data("owned", "1.0.0")
    assert pkg_name == "owned"
    assert version == "1.0.0"
    assert manifest_uri == "ipfs://QmcxvhkJJVpbxEAa6cgW3B6XwPJb79w9GpNUv2P2THUzZR"
