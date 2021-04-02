import logging
from typing import (
    Any,
    Callable,
    Dict,
)

from eth_typing import (
    ContractName,
)
from eth_utils import (
    to_checksum_address,
    to_hex,
)
from eth_utils.toolz import (
    assoc_in,
    curry,
    pipe,
)

from ethpm import (
    Package,
)
from ethpm.uri import (
    create_latest_block_uri,
)
from web3.tools.pytest_ethereum._utils import (
    create_deployment_data,
    get_deployment_address,
    insert_deployment,
)
from web3.tools.pytest_ethereum.exceptions import (
    LinkerError,
)

logger = logging.getLogger("pytest_ethereum.linker")


def linker(*args: Callable[..., Any]) -> Callable[..., Any]:
    return _linker(args)


@curry
def _linker(operations: Callable[..., Any], package: Package) -> Callable[..., Package]:
    return pipe(package, *operations)


def deploy(
    contract_name: str, *args: Any, transaction: Dict[str, Any] = None
) -> Callable[..., Package]:
    """
    Return a newly created package and contract address.
    Will deploy the given contract_name, if data exists in package. If
    a deployment is found on the current w3 instance, it will return that deployment
    rather than creating a new instance.
    """
    return _deploy(contract_name, args, transaction)


@curry
def _deploy(
    contract_name: ContractName, args: Any, transaction: Dict[str, Any], package: Package
) -> Package:
    # Deploy new instance
    factory = package.get_contract_factory(contract_name)
    if not factory.linked_references and factory.unlinked_references:
        raise LinkerError(
            f"Contract factory: {contract_name} is missing runtime link references, which are "
            "necessary to populate manifest deployments that have a link reference. If using the "
            "builder tool, use `contract_type(..., runtime_bytecode=True)`."
        )
    tx_hash = factory.constructor(*args).transact(transaction)
    tx_receipt = package.w3.eth.wait_for_transaction_receipt(tx_hash)
    # Create manifest copy with new deployment instance
    latest_block_uri = create_latest_block_uri(package.w3, 0)
    deployment_data = create_deployment_data(
        contract_name,
        to_checksum_address(tx_receipt["contractAddress"]),
        tx_receipt,
        factory.linked_references,
    )
    manifest = insert_deployment(
        package, contract_name, deployment_data, latest_block_uri
    )
    logger.info("%s deployed." % contract_name)
    return Package(manifest, package.w3)


@curry
def link(contract: ContractName, linked_type: str, package: Package) -> Package:
    """
    Return a new package, created with a new manifest after applying the linked type
    reference to the contract factory.
    """
    deployment_address = get_deployment_address(linked_type, package)
    unlinked_factory = package.get_contract_factory(contract)
    if not unlinked_factory.needs_bytecode_linking:
        raise LinkerError(
            f"Contract factory: {unlinked_factory.__repr__()} does not need bytecode linking, "
            "so it is not a valid contract type for link()"
        )
    linked_factory = unlinked_factory.link_bytecode({linked_type: deployment_address})
    # todo replace runtime_bytecode in manifest
    manifest = assoc_in(
        package.manifest,
        ("contractTypes", contract, "deploymentBytecode", "bytecode"),
        to_hex(linked_factory.bytecode),
    )
    logger.info(
        "%s linked to %s at address %s."
        % (contract, linked_type, to_checksum_address(deployment_address))
    )
    return Package(manifest, package.w3)


@curry
def run_python(callback_fn: Callable[..., None], package: Package) -> Package:
    """
    Return the unmodified package, after performing any user-defined callback function on
    the contracts in the package.
    """
    callback_fn(package)
    logger.info("%s python function ran." % callback_fn.__name__)
    return package
