import pytest

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
    'args,kwargs',
    (
        (None, 'kwarg-is-ignored'),
        ('arg-is-ignored', None),
    ),
)
def test_contract_error_if_additional_args_are_supplied_with_no_constructor_fn(MathContract,
                                                                               args, kwargs):
    with pytest.raises(TypeError, match="Constructor args"):
        MathContract._encode_constructor_data(args, kwargs)


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
        '0x61626364',
    ),
)
def test_contract_constructor_encoding_encoding(web3, WithConstructorArgumentsContract, bytes_arg):
    deploy_data = WithConstructorArgumentsContract._encode_constructor_data([1234, bytes_arg])
    encoded_args = '0x00000000000000000000000000000000000000000000000000000000000004d26162636400000000000000000000000000000000000000000000000000000000'  # noqa: E501
    expected_ending = encode_hex(web3.codec.encode_abi(['uint256', 'bytes32'], [1234, b'abcd']))
    assert expected_ending == encoded_args
    assert deploy_data.endswith(remove_0x_prefix(expected_ending))


def test_contract_constructor_encoding_encoding_warning(web3, WithConstructorArgumentsContract):
    with pytest.warns(
        DeprecationWarning,
        match='in v6 it will be invalid to pass a hex string without the \"0x\" prefix'
    ):
        deploy_data = WithConstructorArgumentsContract._encode_constructor_data([1234, '61626364'])
        encoded_args = '0x00000000000000000000000000000000000000000000000000000000000004d26162636400000000000000000000000000000000000000000000000000000000'  # noqa: E501

        expected_ending = encode_hex(
            web3.codec.encode_abi(['uint256', 'bytes32'], [1234, b'abcd'])
        )
        assert expected_ending == encoded_args
        assert deploy_data.endswith(remove_0x_prefix(expected_ending))


@pytest.mark.parametrize(
    'bytes_arg,encoded_args',
    (
        ('0x' + '00' * 32, '0x00000000000000000000000000000000000000000000000000000000000004d20000000000000000000000000000000000000000000000000000000000000000'),  # noqa: E501
        (b'1' * 32, '0x00000000000000000000000000000000000000000000000000000000000004d23131313131313131313131313131313131313131313131313131313131313131'),  # noqa: E501
    ),
)
def test_contract_constructor_encoding_encoding_strict(
        w3_strict_abi,
        WithConstructorArgumentsContractStrict,
        encoded_args,
        bytes_arg):

    deploy_data = WithConstructorArgumentsContractStrict._encode_constructor_data([1234, bytes_arg])

    expected_ending = encode_hex(
        w3_strict_abi.codec.encode_abi(['uint256', 'bytes32'], [1234, bytes_arg])
    )
    assert expected_ending == encoded_args
    assert deploy_data.endswith(remove_0x_prefix(expected_ending))


@pytest.mark.parametrize(
    'bytes_arg',
    (
        b'abcd',
        '0x61626364',
        '',
        '61626364',
    ),
)
def test_contract_constructor_encoding_encoding_strict_errors(
        w3_strict_abi,
        WithConstructorArgumentsContractStrict,
        bytes_arg):
    with pytest.raises(
        TypeError,
        match="One or more arguments could not be encoded to the necessary ABI type."
    ):
        WithConstructorArgumentsContractStrict._encode_constructor_data([1234, bytes_arg])
