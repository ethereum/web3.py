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
        deployed_registry_address = deployed_registry_package.deployments.get_instance("registry").address
        return cls(deployed_registry_address, deployed_registry_package.w3)


    def release(self, name, version, uri):
        tx_receipt = self.registry.functions.release(name, version, uri).transact()
        self.w3.eth.waitForTransactionReceipt(tx_receipt)
        

    def get_release_data(self, name, version):
        release_id = self.registry.functions.getReleaseId(name, version).call()
        return self.registry.functions.getReleaseData(release_id).call()

    @property
    def owner(self):
        return self.registry.functions.owner().call()

    @to_tuple
    def get_all_package_ids(self):
        package_count = self.registry.functions.packageCount().call()
        for index in range(0, package_count, 4):
            package_ids = self.registry.functions.getAllPackageIds(index, 5).call()
            for pkg_id in package_ids:
                if pkg_id != b'\x00' * 32:
                    pkg_name = self.registry.functions.getPackageName(pkg_id).call()
                    pkg_data = self.registry.functions.getPackageData(pkg_name).call()
                    yield (pkg_name.rstrip(b'\x00'), pkg_data[2])
        

    @to_tuple
    def get_all_package_versions(self, name): # -> (version, uri):
        name, package_id, release_count = self.registry.functions.getPackageData(name).call()
        for index in range(0, release_count, 4):
            release_ids = self.registry.functions.getAllReleaseIds(b'package', index, 5).call()
            for r_id in release_ids:
                if r_id != b'\x00' * 32:
                    release_data = self.registry.functions.getReleaseData(r_id).call()
                    yield (release_data[1].rstrip(b'\x00'), release_data[2].rstrip(b'\x00'))
            


    def transfer_owner(self, new_address):
        tx_receipt = self.registry.functions.transferOwner(new_address).transact()
        self.w3.eth.waitForTransactionReceipt(tx_receipt)


