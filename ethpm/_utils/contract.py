from typing import (
    Any,
    Dict,
    Generator,
    Tuple,
)

from eth_utils import (
    to_dict,
)


@to_dict
def generate_contract_factory_kwargs(
    contract_data: Dict[str, Any]
) -> Generator[Tuple[str, Any], None, None]:
    """
    Build a dictionary of kwargs to be passed into contract factory.
    """
    if "abi" in contract_data:
        yield "abi", contract_data["abi"]

    if "deployment_bytecode" in contract_data:
        yield "bytecode", contract_data["deployment_bytecode"]["bytecode"]
        if "link_references" in contract_data["deployment_bytecode"]:
            yield "unlinked_references", tuple(
                contract_data["deployment_bytecode"]["link_references"]
            )

    if "runtime_bytecode" in contract_data:
        yield "bytecode_runtime", contract_data["runtime_bytecode"]["bytecode"]
        if "link_references" in contract_data["runtime_bytecode"]:
            yield "linked_references", tuple(
                contract_data["runtime_bytecode"]["link_references"]
            )
