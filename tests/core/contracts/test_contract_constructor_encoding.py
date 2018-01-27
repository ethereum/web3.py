import pytest

from eth_abi import (
    encode_abi,
)
from eth_utils import (
    encode_hex,
    remove_0x_prefix,
)


def test_contract_constructor_abi_encoding_with_no_constructor_fn(MathContract, MATH_CODE):
    deploy_data = MathContract._encode_constructor_data()
    assert deploy_data == MATH_CODE


def test_contract_constructor_abi_encoding_with_constructor_with_no_args(SimpleConstructorContract,
                                                                         SIMPLE_CONSTRUCTOR_CODE):
    deploy_data = SimpleConstructorContract._encode_constructor_data()
    assert deploy_data == SIMPLE_CONSTRUCTOR_CODE


@pytest.mark.parametrize(
    'arguments',
    (
        [],
        [1234],
        ['abcd', 1234],  # wrong order
        [1234, 'abcd', 'extra-arg'],  # extra arguments
        [-1234, 'abcd'],  # wrong types
        ['1234', 'abcd'],  # wrong types
    ),
)
def test_error_if_invalid_arguments_supplied(WithConstructorArgumentsContract, arguments):
    with pytest.raises(TypeError):
        WithConstructorArgumentsContract._encode_constructor_data(arguments)


@pytest.mark.parametrize(
    'bytes_arg',
    (
        b'abcd',
        '61626364',
        '0x61626364',
    ),
)
def test_contract_constructor_encoding_encoding(WithConstructorArgumentsContract, bytes_arg):
    deploy_data = WithConstructorArgumentsContract._encode_constructor_data([1234, bytes_arg])
    encoded_args = '0x00000000000000000000000000000000000000000000000000000000000004d26162636400000000000000000000000000000000000000000000000000000000'  # noqa: E501
    expected_ending = encode_hex(encode_abi(['uint256', 'bytes32'], [1234, b'abcd']))
    assert expected_ending == encoded_args
    assert deploy_data.endswith(remove_0x_prefix(expected_ending))
