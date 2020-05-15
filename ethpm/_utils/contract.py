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

    # camelCase b/c ethpm/3
    if "deploymentBytecode" in contract_data:
        yield "bytecode", contract_data["deploymentBytecode"]["bytecode"]
        if "linkReferences" in contract_data["deploymentBytecode"]:
            # snake_case to remain consistent with python code
            yield "unlinked_references", tuple(
                contract_data["deploymentBytecode"]["linkReferences"]
            )

    # camelCase b/c ethpm/3
    if "runtimeBytecode" in contract_data:
        # snake_case to remain consistent with python code
        yield "bytecode_runtime", contract_data["runtimeBytecode"]["bytecode"]
        if "linkReferences" in contract_data["runtimeBytecode"]:
            yield "linked_references", tuple(
                contract_data["runtimeBytecode"]["linkReferences"]
            )
