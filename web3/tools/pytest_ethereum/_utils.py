from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Tuple,
)

from eth_typing import (
    URI,
    Address,
    ContractName,
    Manifest,
)
from eth_utils import (
    to_dict,
    to_hex,
    to_list,
)
from eth_utils.toolz import (
    assoc,
    assoc_in,
    dissoc,
)

from ethpm import (
    Package,
)
from ethpm.uri import (
    check_if_chain_matches_chain_uri,
)
from web3 import (
    Web3,
)
from web3.tools.pytest_ethereum.exceptions import (
    LinkerError,
)
from web3.types import (
    TxReceipt,
)


def pluck_matching_uri(deployment_data: Dict[URI, Dict[str, str]], w3: Web3) -> URI:
    """
    Return any blockchain uri that matches w3-connected chain, if one
    is present in the deployment data keys.
    """
    for uri in deployment_data.keys():
        if check_if_chain_matches_chain_uri(w3, uri):
            return uri
    raise LinkerError(
        "No matching blockchain URI found in deployment_data: "
        f"{list(deployment_data.keys())}, for w3 instance: {w3.__repr__()}."
    )


def contains_matching_uri(deployment_data: Dict[str, Dict[str, str]], w3: Web3) -> bool:
    """
    Returns true if any blockchain uri in deployment data matches
    w3-connected chain.
    """
    for uri in deployment_data.keys():
        if check_if_chain_matches_chain_uri(w3, uri):
            return True
    return False


def insert_deployment(
    package: Package,
    deployment_name: str,
    deployment_data: Dict[str, str],
    latest_block_uri: URI,
) -> Manifest:
    """
    Returns a new manifest. If a matching chain uri is found
    in the old manifest, it will update the chain uri along
    with the new deployment data. If no match, it will simply add
    the new chain uri and deployment data.
    """
    old_deployments_data = package.manifest.get("deployments")
    if old_deployments_data and contains_matching_uri(old_deployments_data, package.w3):
        old_chain_uri = pluck_matching_uri(old_deployments_data, package.w3)
        old_deployments_chain_data = old_deployments_data[old_chain_uri]
        # Replace specific on-chain deployment (i.e. deployment_name)
        new_deployments_chain_data_init = dissoc(
            old_deployments_chain_data, deployment_name
        )
        new_deployments_chain_data = {
            **new_deployments_chain_data_init,
            **{deployment_name: deployment_data},
        }
        # Replace all on-chain deployments
        new_deployments_data_init = dissoc(
            old_deployments_data, "deployments", old_chain_uri
        )
        new_deployments_data = {
            **new_deployments_data_init,
            **{latest_block_uri: new_deployments_chain_data},
        }
        return assoc(package.manifest, "deployments", new_deployments_data)

    return assoc_in(
        package.manifest,
        ("deployments", latest_block_uri, deployment_name),
        deployment_data,
    )


@to_dict
def create_deployment_data(
    contract_name: ContractName,
    new_address: Address,
    tx_receipt: TxReceipt,
    link_refs: List[Dict[str, Any]] = None,
) -> Iterable[Tuple[str, Any]]:
    yield "contractType", contract_name
    yield "address", new_address
    yield "transaction", to_hex(tx_receipt["transactionHash"])
    yield "block", to_hex(tx_receipt["blockHash"])
    if link_refs:
        yield "runtimeBytecode", {"linkDependencies": create_link_dep(link_refs)}


@to_list
def create_link_dep(link_refs: List[Dict[str, Any]]) -> Iterable[Dict[str, Any]]:
    for link_ref in link_refs:
        yield {
            "offsets": link_ref["offsets"],
            "type": "reference",
            "value": link_ref["name"],
        }


def get_deployment_address(linked_type: str, package: Package) -> Address:
    """
    Return the address of a linked_type found in a package's manifest deployments.
    """
    try:
        deployment_address = package.deployments.get(linked_type)["address"]
    except KeyError:
        raise LinkerError(
            f"Package data does not contain a valid deployment of {linked_type} on the "
            "current w3-connected chain."
        )
    return deployment_address
