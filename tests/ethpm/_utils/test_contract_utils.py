import pytest

from ethpm._utils.contract import (
    generate_contract_factory_kwargs,
)
from ethpm.exceptions import (
    EthPMValidationError,
    InsufficientAssetsError,
)
from ethpm.validation.misc import (
    validate_w3_instance,
)
from ethpm.validation.package import (
    validate_contract_name,
    validate_minimal_contract_factory_data,
)


@pytest.mark.parametrize(
    "contract_data",
    (
        {"abi": "", "deploymentBytecode": ""},
        {
            "abi": "",
            "deploymentBytecode": {"bytecode": ""},
            "runtimeBytecode": {"bytecode": ""},
        },
    ),
)
def test_validate_minimal_contract_factory_data_validates(contract_data):
    assert validate_minimal_contract_factory_data(contract_data) is None


@pytest.mark.parametrize(
    "contract_data",
    (
        {"abi": ""},
        {"deploymentBytecode": {"bytecode": ""}},
        {"runtimeBytecode": {"bytecode": ""}, "other": ""},
    ),
)
def test_validate_minimal_contract_factory_data_invalidates(contract_data):
    with pytest.raises(InsufficientAssetsError):
        validate_minimal_contract_factory_data(contract_data)


@pytest.mark.parametrize("name", ("A1", "A-1", "A_1", "X" * 256))
def test_validate_contract_name_validates(name):
    assert validate_contract_name(name) is None


@pytest.mark.parametrize("name", ("", "-abc", "A=bc", "X" * 257))
def test_validate_contract_name_invalidates(name):
    with pytest.raises(EthPMValidationError):
        assert validate_contract_name(name)


@pytest.mark.parametrize(
    "contract_data,expected_kwargs",
    (
        ({"abi": ""}, ["abi"]),
        ({"deploymentBytecode": {"bytecode": ""}}, ["bytecode"]),
        (
            {"abi": "", "runtimeBytecode": {"bytecode": ""}},
            ["abi", "bytecode_runtime"],
        ),
        (
            {
                "abi": "",
                "deploymentBytecode": {
                    "bytecode": "",
                    "linkReferences": [
                        {"offsets": [402, 639], "length": 20, "name": "SafeSendLib"}
                    ],
                },
            },
            ["abi", "bytecode", "unlinked_references"],
        ),
    ),
)
def test_generate_contract_factory_kwargs(contract_data, expected_kwargs):
    contract_factory = generate_contract_factory_kwargs(contract_data)
    assert set(contract_factory.keys()) == set(expected_kwargs)


def test_validate_w3_instance_validates(w3):
    assert validate_w3_instance(w3) is None


@pytest.mark.parametrize("w3", ("NotWeb3", b"NotWeb3", 1234))
def test_validate_w3_instance_invalidates(w3):
    with pytest.raises(ValueError):
        assert validate_w3_instance(w3)
