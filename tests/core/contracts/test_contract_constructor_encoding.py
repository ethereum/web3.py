import pytest

from eth_utils import (
    encode_hex,
    remove_0x_prefix,
)

from web3._utils.contract_sources.contract_data.constructor_contracts import (
    SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE,
)


def test_contract_constructor_abi_encoding_with_no_constructor_fn(
    math_contract_factory, math_contract_bytecode
):
    deploy_data = math_contract_factory._encode_constructor_data()
    assert deploy_data == math_contract_bytecode


def test_contract_constructor_abi_encoding_with_constructor_with_no_args(
    simple_constructor_contract_factory,
):
    deploy_data = simple_constructor_contract_factory._encode_constructor_data()
    assert deploy_data == SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE


@pytest.mark.parametrize(
    "args,kwargs",
    (
        (tuple(), {"kwarg-is-ignored": True}),
        ("arg-is-ignored", {}),
    ),
)
def test_contract_error_if_additional_args_are_supplied_with_no_constructor_fn(
    math_contract_factory, args, kwargs
):
    with pytest.raises(TypeError, match="Constructor args"):
        math_contract_factory._encode_constructor_data(*args, **kwargs)


@pytest.mark.parametrize(
    "arguments",
    (
        [],
        [1234],
        ["abcd", 1234],  # wrong order
        [1234, "abcd", "extra-arg"],  # extra arguments
        [-1234, "abcd"],  # wrong types
        ["1234", "abcd"],  # wrong types
    ),
)
def test_error_if_invalid_arguments_supplied(
    contract_with_constructor_args_factory, arguments
):
    with pytest.raises(TypeError):
        contract_with_constructor_args_factory._encode_constructor_data(*arguments)


@pytest.mark.parametrize(
    "bytes_arg,encoded_args",
    (
        (
            "0x" + "00" * 32,
            "0x00000000000000000000000000000000000000000000000000000000000004d20000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
        ),
        (
            b"1" * 32,
            "0x00000000000000000000000000000000000000000000000000000000000004d23131313131313131313131313131313131313131313131313131313131313131",  # noqa: E501
        ),
    ),
)
def test_contract_constructor_encoding(
    w3,
    contract_with_constructor_args_factory,
    encoded_args,
    bytes_arg,
):
    deploy_data = contract_with_constructor_args_factory._encode_constructor_data(
        *[1234, bytes_arg]
    )
    expected_ending = encode_hex(
        w3.codec.encode(["uint256", "bytes32"], [1234, bytes_arg])
    )
    assert expected_ending == encoded_args
    assert deploy_data.endswith(remove_0x_prefix(expected_ending))


@pytest.mark.parametrize(
    "bytes_arg",
    (
        b"abcd",
        "0x61626364",
        "61626364",
    ),
)
def test_contract_constructor_encoding_non_strict(
    w3_non_strict_abi, non_strict_contract_with_constructor_args_factory, bytes_arg
):
    deploy_data = (
        non_strict_contract_with_constructor_args_factory._encode_constructor_data(
            *[1234, bytes_arg]
        )
    )
    encoded_args = "0x00000000000000000000000000000000000000000000000000000000000004d26162636400000000000000000000000000000000000000000000000000000000"  # noqa: E501
    expected_ending = encode_hex(
        w3_non_strict_abi.codec.encode(["uint256", "bytes32"], [1234, b"abcd"])
    )
    assert expected_ending == encoded_args
    assert deploy_data.endswith(remove_0x_prefix(expected_ending))


@pytest.mark.parametrize(
    "bytes_arg",
    (
        b"abcd",
        "0x61626364",
        "",
        "61626364",
    ),
)
def test_contract_constructor_encoding_strict_errors(
    contract_with_constructor_args_factory, bytes_arg
):
    with pytest.raises(
        TypeError,
        match="One or more arguments could not be encoded to the necessary ABI type.",
    ):
        contract_with_constructor_args_factory._encode_constructor_data(
            *[1234, bytes_arg]
        )
