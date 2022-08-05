from typing import (
    List,
    Union,
)

from web3.types import (
    ABIEvent,
    ABIFunction,
)


def get_abi_input_names(abi: Union[ABIFunction, ABIEvent]) -> List[str]:
    if "inputs" not in abi and abi["type"] == "fallback":
        return []
    return [arg["name"] for arg in abi["inputs"]]


def get_abi_output_names(abi: Union[ABIFunction]) -> List[str]:
    if "outputs" not in abi and abi["type"] == "fallback":
        return []
    return [arg["name"] for arg in abi["outputs"]]
