import pytest

from eth_utils import (
    to_bytes,
    to_canonical_address,
)
from ethpm import (
    ASSETS_DIR,
)

from ens import ENS
from web3.exceptions import (
    InvalidAddress,
)
from web3.pm import (
    PM,
    VyperReferenceRegistry,
)


def bytes32(val):
    if isinstance(val, int):
        result = to_bytes(val)
    else:
        raise TypeError('val %r could not be converted to bytes')
    return result.rjust(32, b'\0')


pytest_plugins = ["pytest_ethereum.plugins"]


@pytest.fixture
def ens_setup(solc_deployer):
    # todo: move to module level once ethpm alpha stable
    ENS_MANIFEST = ASSETS_DIR / 'ens' / '1.0.1.json'
    ens_deployer = solc_deployer(ENS_MANIFEST)
    w3 = ens_deployer.package.w3

    # ** Set up ENS contracts **

    # remove account that creates ENS, so test transactions don't have write access
    accounts = w3.eth.accounts
    ens_key = accounts.pop()

    # create ENS contract
    # values borrowed from:
    # https://github.com/ethereum/web3.py/blob/master/tests/ens/conftest.py#L109
    eth_labelhash = w3.keccak(text='eth')
    eth_namehash = bytes32(0x93cdeb708b7545dc668eb9280176169d1c33cfd8ed6f04690a0bcc88a93fc4ae)
    resolver_namehash = bytes32(0xfdd5d5de6dd63db72bbc2d487944ba13bf775b50a80805fe6fcaba9b0fba88f5)
    ens_package = ens_deployer.deploy("ENSRegistry", transaction={"from": ens_key})
    ens_contract = ens_package.deployments.get_instance("ENSRegistry")

    # create public resolver
    public_resolver_package = ens_deployer.deploy(
        "PublicResolver",
        ens_contract.address,
        transaction={"from": ens_key}
    )
    public_resolver = public_resolver_package.deployments.get_instance("PublicResolver")

    # set 'resolver.eth' to resolve to public resolver
    ens_contract.functions.setSubnodeOwner(
        b'\0' * 32,
        eth_labelhash,
        ens_key
    ).transact({'from': ens_key})

    ens_contract.functions.setSubnodeOwner(
        eth_namehash,
        w3.keccak(text='resolver'),
        ens_key
    ).transact({'from': ens_key})

    ens_contract.functions.setResolver(
        resolver_namehash,
        public_resolver.address
    ).transact({'from': ens_key})

    public_resolver.functions.setAddr(
        resolver_namehash,
        public_resolver.address
    ).transact({'from': ens_key})

    # create .eth auction registrar
    eth_registrar_package = ens_deployer.deploy(
        "FIFSRegistrar",
        ens_contract.address,
        eth_namehash,
        transaction={"from": ens_key}
    )
    eth_registrar = eth_registrar_package.deployments.get_instance("FIFSRegistrar")

    # set '.eth' to resolve to the registrar
    ens_contract.functions.setResolver(
        eth_namehash,
        public_resolver.address
    ).transact({'from': ens_key})

    public_resolver.functions.setAddr(
        eth_namehash,
        eth_registrar.address
    ).transact({'from': ens_key})

    # set owner of tester.eth to an account controlled by tests
    ens_contract.functions.setSubnodeOwner(
        eth_namehash,
        w3.keccak(text='tester'),
        w3.eth.accounts[2]  # note that this does not have to be the default, only in the list
    ).transact({'from': ens_key})

    # make the registrar the owner of the 'eth' name
    ens_contract.functions.setSubnodeOwner(
        b'\0' * 32,
        eth_labelhash,
        eth_registrar.address
    ).transact({'from': ens_key})
    return ENS.fromWeb3(w3, ens_contract.address)


@pytest.fixture
def ens(ens_setup, mocker):
    mocker.patch('web3.middleware.stalecheck._isfresh', return_value=True)
    ens_setup.web3.eth.defaultAccount = ens_setup.web3.eth.coinbase
    return ens_setup


def test_ens_must_be_set_before_ens_methods_can_be_used(ens):
    w3 = ens.web3
    PM.attach(w3, 'pm')
    with pytest.raises(InvalidAddress):
        w3.pm.set_registry("tester.eth")


def test_web3_ens(ens):
    w3 = ens.web3
    PM.attach(w3, 'pm')
    ns = ENS.fromWeb3(w3, ens.ens.address)
    w3.ens = ns
    registry = VyperReferenceRegistry.deploy_new_instance(w3)
    w3.ens.setup_address('tester.eth', registry.address)
    actual_addr = ens.address('tester.eth')
    w3.pm.set_registry('tester.eth')
    assert w3.pm.registry.address == to_canonical_address(actual_addr)
    w3.pm.release_package('pkg', 'v1', 'website.com')
    pkg_name, version, manifest_uri = w3.pm.get_release_data('pkg', 'v1')
    assert pkg_name == 'pkg'
    assert version == 'v1'
    assert manifest_uri == 'website.com'
