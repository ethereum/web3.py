from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Generator,
    List,
    Tuple,
)

from eth_utils import (
    is_same_address,
    to_bytes,
    to_tuple,
)
from eth_utils.toolz import (
    get_in,
)
from hexbytes import (
    HexBytes,
)

from ethpm.exceptions import (
    BytecodeLinkingError,
    EthPMValidationError,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def get_linked_deployments(deployments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Returns all deployments found in a chain URI's deployment data that
    contain link dependencies.
    """
    linked_deployments = {
        dep: data
        for dep, data in deployments.items()
        if get_in(("runtimeBytecode", "linkDependencies"), data)
    }
    for deployment, data in linked_deployments.items():
        if any(
            link_dep["value"] == deployment
            for link_dep in data["runtimeBytecode"]["linkDependencies"]
        ):
            raise BytecodeLinkingError(
                f"Link dependency found in {deployment} deployment that references its "
                "own contract instance, which is disallowed"
            )
    return linked_deployments


def validate_linked_references(
    link_deps: Tuple[Tuple[int, bytes], ...], bytecode: HexBytes
) -> None:
    """
    Validates that normalized linked_references (offset, expected_bytes)
    match the corresponding bytecode.
    """
    offsets, values = zip(*link_deps)
    for idx, offset in enumerate(offsets):
        value = values[idx]
        # https://github.com/python/mypy/issues/4975
        offset_value = int(offset)
        dep_length = len(value)
        end_of_bytes = offset_value + dep_length
        # Ignore b/c whitespace around ':' conflict b/w black & flake8
        actual_bytes = bytecode[offset_value:end_of_bytes]  # noqa: E203
        if actual_bytes != values[idx]:
            raise EthPMValidationError(
                "Error validating linked reference. "
                f"Offset: {offset} "
                f"Value: {values[idx]} "
                f"Bytecode: {bytecode!r} ."
            )


@to_tuple
def normalize_linked_references(
    data: List[Dict[str, Any]]
) -> Generator[Tuple[int, str, str], None, None]:
    """
    Return a tuple of information representing all insertions of a linked reference.
    (offset, type, value)
    """
    for deployment in data:
        for offset in deployment["offsets"]:
            yield offset, deployment["type"], deployment["value"]


def validate_deployments_tx_receipt(
    deployments: Dict[str, Any], w3: "Web3", allow_missing_data: bool = False
) -> None:
    """
    Validate that address and block hash found in deployment data match
    what is found on-chain. :allow_missing_data: by default, enforces
    validation of address and blockHash.
    """
    # todo: provide hook to lazily look up tx receipt via binary search if missing data
    for name, data in deployments.items():
        if "transaction" in data:
            tx_hash = data["transaction"]
            tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
            # tx_address will be None if contract created via contract factory
            tx_address = tx_receipt["contractAddress"]

            if tx_address is None and allow_missing_data is False:
                raise EthPMValidationError(
                    "No contract address found in tx receipt. Unable to verify "
                    "address found in tx receipt matches address in manifest's "
                    "deployment data. If this validation is not necessary, "
                    "please enable `allow_missing_data` arg. "
                )

            if tx_address is not None and not is_same_address(
                tx_address, data["address"]
            ):
                raise EthPMValidationError(
                    f"Error validating tx_receipt for {name} deployment. "
                    f"Address found in manifest's deployment data: {data['address']} "
                    f"Does not match address found on tx_receipt: {tx_address}."
                )

            if "block" in data:
                if tx_receipt["blockHash"] != to_bytes(hexstr=data["block"]):
                    raise EthPMValidationError(
                        f"Error validating tx_receipt for {name} deployment. "
                        f"Block found in manifest's deployment data: {data['block']!r} "
                        "Does not match block found on "
                        f"tx_receipt: {tx_receipt['blockHash']!r}."
                    )
            elif allow_missing_data is False:
                raise EthPMValidationError(
                    "No block hash found in deployment data. "
                    "Unable to verify block hash on tx receipt. "
                    "If this validation is not necessary, please enable "
                    "`allow_missing_data` arg."
                )
        elif allow_missing_data is False:
            raise EthPMValidationError(
                "No transaction hash found in deployment data. "
                "Unable to validate tx_receipt. "
                "If this validation is not necessary, please "
                "enable `allow_missing_data` arg."
            )
