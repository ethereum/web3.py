import json
from eth_utils import to_canonical_address, to_tuple, combomethod

from pytest_ethereum.deployer import Deployer
from web3.contract import Contract
from web3.module import (
    Module,
)

try:
    from ethpm.utils.chains import get_genesis_block_hash
    from ethpm import (
        ASSETS_DIR,
        Package,
    )
except ImportError as exc:
    raise ImportError(
        "To use web3's alpha package management features, you must install the "
        "`ethpm` dependency manually: pip install --upgrade ethpm"
    ) from exc


# Package Management is currently still in alpha
# It is not automatically available on a web3 object.
# To use the `PM` module, attach it to your web3 object
# i.e. PM.attach(web3, 'pm')


class PM(Module):

    def set_registry(self, address=None):
        if not address:
            self.registry = Registry.deploy_new_instance(self.web3)
        else:
            self.registry = Registry(address, self.web3)

    def get_package_from_manifest(self, manifest):
        pkg = Package(manifest, self.web3)
        return pkg

    def get_package_from_uri(self, uri):
        pkg = Package.from_uri(uri, self.web3)
        return pkg

    def release_package(self, name, version, uri):
        if not self.registry:
            raise AttributeError("Registry has not been set for web3.pm")
        if self.web3.eth.defaultAccount != self.registry.owner:
            # change error
            raise AttributeError("Owner doesn't have right permissions to release pkg.")
        self.registry.release(name, version, uri)

    def get_release_data_from_registry(self, name, version):
        if not self.registry:
            raise AttributeError("Registry has not been set for web3.pm")
        return self.registry.get_release_data(name, version) 

    def get_package_from_registry(self, name, version):
        if not self.registry:
            raise AttributeError("Registry has not been set for web3.pm")
        release_uri = self.registry.get_release_data(name, version)
        return self.get_package_from_uri(release_uri)


class Registry(Contract):
    def __init__(self, address, w3):
        # only works with v.py registry in ethpm/assets
        # abi verification for compatibility?
        # todo ens linking
        manifest = json.loads((ASSETS_DIR / 'vyper_registry' / '1.0.0.json').read_text())
        registry_package = Package(manifest, w3)
        self.registry = registry_package.get_contract_instance("registry", to_canonical_address(address))
        self.w3 = w3
        self.address = address

    @classmethod
    def deploy_new_instance(cls, w3):
        manifest = json.loads((ASSETS_DIR / 'vyper_registry' / '1.0.0.json').read_text())
        registry_package = Package(manifest, w3)
        registry_deployer = Deployer(registry_package)
        deployed_registry_package = registry_deployer.deploy("registry")
        deployed_registry_address = deployed_registry_package.deployments.get_contract_instance("registry").address
        return cls(deployed_registry_address, deployed_registry_package.w3)


    def release(self, name, version, uri):
        tx_receipt = self.registry.functions.release(name, version, uri).transact()
        self.w3.eth.waitForTransactionReceipt(tx_receipt)
        

    def get_release_data(self, name, version):
        return self.registry.functions.get_release_data(name, version).call()

    @property
    def owner(self):
        return self.registry.functions.owner().call()

    @to_tuple
    def get_all_packages(self):
        package_count = self.registry.functions.package_count().call()
        for index in range(package_count):
            package_id = self.registry.functions.get_package_id(index).call()
            package_data = self.registry.functions.get_package_data_by_id(package_id).call()
            yield (package_data[0].rstrip(b'\x00'), package_data[1])
        

    @to_tuple
    def get_all_package_versions(self, name): # -> (version, uri):
        package_data = self.registry.functions.get_package_data(name).call()
        release_count = package_data[1]
        for index in range(release_count):
            release_id = self.registry.functions.get_release_id_by_package_and_count(name, (index + 1)).call()
            release_data = self.registry.functions.get_release_data_by_id(release_id).call()
            yield (release_data[1].rstrip(b'\x00'), release_data[2].rstrip(b'\x00'))


    def transfer_owner(self, new_address):
        tx_receipt = self.registry.functions.transfer_owner(new_address).transact()
        self.w3.eth.waitForTransactionReceipt(tx_receipt)


