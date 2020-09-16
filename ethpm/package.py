import json
from pathlib import (
    Path,
)
from typing import (
    Any,
    Dict,
    Generator,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    Union,
    cast,
)

from eth_typing import (
    URI,
    Address,
    ContractName,
    Manifest,
)
from eth_utils import (
    to_canonical_address,
    to_dict,
    to_text,
    to_tuple,
)

from ethpm._utils.cache import (
    cached_property,
)
from ethpm._utils.contract import (
    generate_contract_factory_kwargs,
)
from ethpm._utils.deployments import (
    get_linked_deployments,
    normalize_linked_references,
    validate_deployments_tx_receipt,
    validate_linked_references,
)
from ethpm.contract import (
    LinkableContract,
)
from ethpm.dependencies import (
    Dependencies,
)
from ethpm.deployments import (
    DeploymentData,
    Deployments,
)
from ethpm.exceptions import (
    BytecodeLinkingError,
    EthPMValidationError,
    FailureToFetchIPFSAssetsError,
    InsufficientAssetsError,
    PyEthPMError,
)
from ethpm.uri import (
    resolve_uri_contents,
)
from ethpm.validation.manifest import (
    check_for_deployments,
    validate_build_dependencies_are_present,
    validate_manifest_against_schema,
    validate_manifest_deployments,
    validate_raw_manifest_format,
)
from ethpm.validation.misc import (
    validate_w3_instance,
)
from ethpm.validation.package import (
    validate_build_dependency,
    validate_contract_name,
    validate_minimal_contract_factory_data,
)
from ethpm.validation.uri import (
    validate_single_matching_uri,
)
from web3 import Web3
from web3._utils.validation import (
    validate_address,
)
from web3.eth import (
    Contract,
)


class Package(object):
    def __init__(
        self, manifest: Dict[str, Any], w3: Web3, uri: Optional[str] = None
    ) -> None:
        """
        A package should be created using one of the available
        classmethods and a valid w3 instance.
        """
        if not isinstance(manifest, dict):
            raise TypeError(
                "Package object must be initialized with a dictionary. "
                f"Got {type(manifest)}"
            )

        if "manifest" not in manifest or manifest["manifest"] != "ethpm/3":
            raise EthPMValidationError(
                "Py-Ethpm currently only supports v3 ethpm manifests. "
                "Please use the CLI to update or re-generate a v3 manifest. "
            )

        validate_manifest_against_schema(manifest)
        validate_manifest_deployments(manifest)
        validate_w3_instance(w3)

        self.w3 = w3
        self.w3.eth.defaultContractFactory = cast(Type[Contract], LinkableContract)
        self.manifest = manifest
        self._uri = uri

    def update_w3(self, w3: Web3) -> "Package":
        """
        Returns a new instance of `Package` containing the same manifest,
        but connected to a different web3 instance.

        .. doctest::

           >>> new_w3 = Web3(Web3.EthereumTesterProvider())
           >>> NewPackage = OwnedPackage.update_w3(new_w3)
           >>> assert NewPackage.w3 == new_w3
           >>> assert OwnedPackage.manifest == NewPackage.manifest
        """
        validate_w3_instance(w3)
        return Package(self.manifest, w3, self.uri)

    def __repr__(self) -> str:
        """
        String readable representation of the Package.

        .. doctest::

           >>> OwnedPackage.__repr__()
           '<Package owned==1.0.0>'
        """
        name = self.name
        version = self.version
        return f"<Package {name}=={version}>"

    @property
    def name(self) -> str:
        """
        The name of this ``Package``.

        .. doctest::

           >>> OwnedPackage.name
           'owned'
        """
        return self.manifest["name"]

    @property
    def version(self) -> str:
        """
        The package version of a ``Package``.

        .. doctest::

           >>> OwnedPackage.version
           '1.0.0'
        """
        return self.manifest["version"]

    @property
    def manifest_version(self) -> str:
        """
        The manifest version of a ``Package``.

        .. doctest::

           >>> OwnedPackage.manifest_version
           'ethpm/3'
        """
        return self.manifest["manifest"]

    @property
    def uri(self) -> Optional[str]:
        """
        The uri (local file_path / content-addressed URI) of a ``Package``'s manifest.
        """
        return self._uri

    @property
    def contract_types(self) -> List[str]:
        """
        All contract types included in this package.
        """
        if 'contractTypes' in self.manifest:
            return sorted(self.manifest['contractTypes'].keys())
        else:
            raise ValueError("No contract types found in manifest; {self.__repr__()}.")

    @classmethod
    def from_file(cls, file_path: Path, w3: Web3) -> "Package":
        """
        Returns a ``Package`` instantiated by a manifest located at the provided Path.
        ``file_path`` arg must be a ``pathlib.Path`` instance.
        A valid ``Web3`` instance is required to instantiate a ``Package``.
        """
        if isinstance(file_path, Path):
            raw_manifest = file_path.read_text()
            validate_raw_manifest_format(raw_manifest)
            manifest = json.loads(raw_manifest)
        else:
            raise TypeError(
                "The Package.from_file method expects a pathlib.Path instance."
                f"Got {type(file_path)} instead."
            )
        return cls(manifest, w3, file_path.as_uri())

    @classmethod
    def from_uri(cls, uri: URI, w3: Web3) -> "Package":
        """
        Returns a Package object instantiated by a manifest located at a content-addressed URI.
        A valid ``Web3`` instance is also required.
        URI schemes supported:

        - IPFS: `ipfs://Qm...`

        - HTTP: `https://api.github.com/repos/:owner/:repo/git/blobs/:file_sha`

        - Registry: `erc1319://registry.eth:1/greeter?version=1.0.0`

        .. code:: python

           OwnedPackage = Package.from_uri('ipfs://QmbeVyFLSuEUxiXKwSsEjef7icpdTdA4kGG9BcrJXKNKUW', w3)  # noqa: E501
        """
        contents = to_text(resolve_uri_contents(uri))
        validate_raw_manifest_format(contents)
        manifest = json.loads(contents)
        return cls(manifest, w3, uri)

    #
    # Contracts
    #

    def get_contract_factory(self, name: ContractName) -> LinkableContract:
        """
        Return the contract factory for a given contract type, generated from the data vailable
        in ``Package.manifest``. Contract factories are accessible from the package class.

        .. code:: python

           Owned = OwnedPackage.get_contract_factory('owned')

        In cases where a contract uses a library, the contract factory will have
        unlinked bytecode. The ``ethpm`` package ships with its own subclass of
        ``web3.contract.Contract``, ``ethpm.contract.LinkableContract`` with a few extra
        methods and properties related to bytecode linking.

        .. code:: python

           >>> math = owned_package.contract_factories.math
           >>> math.needs_bytecode_linking
           True
           >>> linked_math = math.link_bytecode({'MathLib': '0x1234...'})
           >>> linked_math.needs_bytecode_linking
           False
        """
        validate_contract_name(name)

        if "contractTypes" not in self.manifest:
            raise InsufficientAssetsError(
                "This package does not contain any contract type data."
            )

        try:
            contract_data = self.manifest["contractTypes"][name]
        except KeyError:
            raise InsufficientAssetsError(
                "This package does not contain any package data to generate "
                f"a contract factory for contract type: {name}. Available contract types include: "
                f"{self.contract_types}."
            )

        validate_minimal_contract_factory_data(contract_data)
        contract_kwargs = generate_contract_factory_kwargs(contract_data)
        contract_factory = self.w3.eth.contract(**contract_kwargs)
        return contract_factory

    def get_contract_instance(self, name: ContractName, address: Address) -> Contract:
        """
        Will return a ``Web3.contract`` instance generated from the contract type data available
        in ``Package.manifest`` and the provided ``address``. The provided ``address`` must be
        valid on the connected chain available through ``Package.w3``.
        """
        validate_address(address)
        validate_contract_name(name)
        try:
            self.manifest["contractTypes"][name]["abi"]
        except KeyError:
            raise InsufficientAssetsError(
                "Package does not have the ABI required to generate a contract instance "
                f"for contract: {name} at address: {address}."
            )
        contract_kwargs = generate_contract_factory_kwargs(
            self.manifest["contractTypes"][name]
        )
        contract_instance = self.w3.eth.contract(
            address=address, **contract_kwargs
        )
        return contract_instance

    #
    # Build Dependencies
    #

    @cached_property
    def build_dependencies(self) -> "Dependencies":
        """
        Return `Dependencies` instance containing the build dependencies available on this Package.
        The ``Package`` class should provide access to the full dependency tree.

        .. code:: python

           >>> owned_package.build_dependencies['zeppelin']
           <ZeppelinPackage>
        """
        validate_build_dependencies_are_present(self.manifest)

        dependencies = self.manifest["buildDependencies"]
        dependency_packages = {}
        for name, uri in dependencies.items():
            try:
                validate_build_dependency(name, uri)
                dependency_package = Package.from_uri(uri, self.w3)
            except PyEthPMError as e:
                raise FailureToFetchIPFSAssetsError(
                    f"Failed to retrieve build dependency: {name} from URI: {uri}.\n"
                    f"Got error: {e}."
                )
            else:
                dependency_packages[name] = dependency_package

        return Dependencies(dependency_packages)

    #
    # Deployments
    #

    @cached_property
    def deployments(self) -> Union["Deployments", Dict[None, None]]:
        """
        Returns a ``Deployments`` object containing all the deployment data and contract
        instances of a ``Package``'s `contract_types`. Automatically filters deployments
        to only expose those available on the current ``Package.w3`` instance.

        .. code:: python

           package.deployments.get_instance("ContractType")
        """
        if not check_for_deployments(self.manifest):
            return {}

        all_blockchain_uris = self.manifest["deployments"].keys()
        matching_uri = validate_single_matching_uri(all_blockchain_uris, self.w3)

        deployments = self.manifest["deployments"][matching_uri]
        all_contract_instances = self._get_all_contract_instances(deployments)
        validate_deployments_tx_receipt(deployments, self.w3, allow_missing_data=True)
        linked_deployments = get_linked_deployments(deployments)
        if linked_deployments:
            for deployment_data in linked_deployments.values():
                on_chain_bytecode = self.w3.eth.getCode(
                    deployment_data["address"]
                )
                unresolved_linked_refs = normalize_linked_references(
                    deployment_data["runtimeBytecode"]["linkDependencies"]
                )
                resolved_linked_refs = tuple(
                    self._resolve_linked_references(link_ref, deployments)
                    for link_ref in unresolved_linked_refs
                )
                for linked_ref in resolved_linked_refs:
                    validate_linked_references(linked_ref, on_chain_bytecode)

        return Deployments(deployments, all_contract_instances)

    @to_dict
    def _get_all_contract_instances(
        self, deployments: Dict[str, DeploymentData]
    ) -> Iterable[Tuple[str, Contract]]:
        for deployment_name, deployment_data in deployments.items():
            if deployment_data['contractType'] not in self.contract_types:
                raise EthPMValidationError(
                    f"Contract type: {deployment_data['contractType']} for alias: "
                    f"{deployment_name} not found. Available contract types include: "
                    f"{self.contract_types}."
                )
            contract_instance = self.get_contract_instance(
                ContractName(deployment_data['contractType']),
                deployment_data['address'],
            )
            yield deployment_name, contract_instance

    @to_tuple
    def _resolve_linked_references(
        self, link_ref: Tuple[int, str, str], deployments: Dict[str, Any]
    ) -> Generator[Tuple[int, bytes], None, None]:
        # No nested deployment: i.e. 'Owned'
        offset, link_type, value = link_ref
        if link_type == "literal":
            yield offset, to_canonical_address(value)
        elif value in deployments:
            yield offset, to_canonical_address(deployments[value]["address"])
        # No nested deployment, but invalid ref
        elif ":" not in value:
            raise BytecodeLinkingError(
                f"Contract instance reference: {value} not found in package's deployment data."
            )
        # Expects child pkg in build_dependencies
        elif value.split(":")[0] not in self.build_dependencies:
            raise BytecodeLinkingError(
                f"Expected build dependency: {value.split(':')[0]} not found "
                "in package's build dependencies."
            )
        # Find and return resolved, nested ref
        else:
            unresolved_linked_ref = value.split(":", 1)[-1]
            build_dependency = self.build_dependencies[value.split(":")[0]]
            yield build_dependency._resolve_link_dependencies(unresolved_linked_ref)


def format_manifest(manifest: Manifest, *, prettify: bool = None) -> str:
    if prettify:
        return json.dumps(manifest, sort_keys=True, indent=4)
    return json.dumps(manifest, sort_keys=True, separators=(",", ":"))
