import pytest

from web3.utils.abi import (
    get_abi_input_names,
)


@pytest.mark.parameterize(
    "abi_element,expected_names",
    (
        (
            {
                "anonymous": False,
                "inputs": [
                    {"indexed": True, "name": "node", "type": "bytes32"},
                    {"indexed": False, "name": "owner", "type": "address"},
                ],
                "name": "Transfer",
                "type": "event",
            },
            ["node", "node"],
        ),
    ),
)
def test_get_abi_input_names(abi_element, expected_names):
    actual = get_abi_input_names(abi_element)
    assert expected_names == actual
