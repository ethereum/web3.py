import json
import pytest


@pytest.fixture()
def MathContract(web3_tester, MATH_ABI, MATH_CODE, MATH_RUNTIME, MATH_SOURCE):
    return web3_tester.eth.contract(
        abi=MATH_ABI,
        code=MATH_CODE,
        code_runtime=MATH_RUNTIME,
        source=MATH_SOURCE,
    )


def test_contract_constructor_abi_encoding_with_no_constructor_fn(MathContract, MATH_CODE):
    deploy_data = MathContract.encodeConstructorData()
    assert deploy_data == MATH_CODE


CONTRACT_SIMPLE_CONSTRUCTOR_SOURCE = "contract WithNoArgumentConstructor { uint public data; function WithNoArgumentConstructor() { data = 3; }}"
CONTRACT_SIMPLE_CONSTRUCTOR_CODE = b'0x60606040526003600055602c8060156000396000f3606060405260e060020a600035046373d4a13a8114601a575b005b602260005481565b6060908152602090f3'
CONTRACT_SIMPLE_CONSTRUCTOR_RUNTIME = b'0x606060405260e060020a600035046373d4a13a8114601a575b005b602260005481565b6060908152602090f3'
CONTRACT_SIMPLE_CONSTRUCTOR_ABI = json.loads('[{"constant":true,"inputs":[],"name":"data","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"inputs":[],"type":"constructor"}]')


@pytest.fixture()
def SimpleConstructorContract(web3_tester):
    return web3_tester.eth.contract(
        abi=CONTRACT_SIMPLE_CONSTRUCTOR_ABI,
        code=CONTRACT_SIMPLE_CONSTRUCTOR_CODE,
        code_runtime=CONTRACT_SIMPLE_CONSTRUCTOR_RUNTIME,
        source=CONTRACT_SIMPLE_CONSTRUCTOR_SOURCE,
    )


def test_contract_constructor_abi_encoding_with_no_constructor_fn(SimpleConstructorContract):
    deploy_data = SimpleConstructorContract.encodeConstructorData()
    assert deploy_data == CONTRACT_SIMPLE_CONSTRUCTOR_CODE

CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_SOURCE =  "contract WithConstructorArguments { uint public data_a; bytes32 public data_b; function WithConstructorArguments(uint a, bytes32 b) { data_a = a; data_b = b; }}"

CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_CODE = b"0x60606040818152806066833960a09052516080516000918255600155603e908190602890396000f3606060405260e060020a600035046388ec134681146024578063d4c46c7614602c575b005b603460005481565b603460015481565b6060908152602090f3"
CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME = b"0x606060405260e060020a600035046388ec134681146024578063d4c46c7614602c575b005b603460005481565b603460015481565b6060908152602090f3"
CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_ABI = json.loads('[{"constant":true,"inputs":[],"name":"data_a","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"data_b","outputs":[{"name":"","type":"bytes32"}],"type":"function"},{"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"bytes32"}],"type":"constructor"}]')


@pytest.fixture()
def WithConstructorArgumentsContract(web3_tester):
    return web3_tester.eth.contract(
        abi=CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_ABI,
        code=CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_CODE,
        code_runtime=CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
        source=CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_SOURCE,
    )


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
    with pytest.raises(ValueError):
        WithConstructorArgumentsContract.encodeConstructorData(arguments)


def test_contract_constructor_encoding_encoding(WithConstructorArgumentsContract):
    deploy_data = WithConstructorArgumentsContract.encodeConstructorData([1234, 'abcd'])
    encoded_args = b'00000000000000000000000000000000000000000000000000000000000004d26162636400000000000000000000000000000000000000000000000000000000'
    assert deploy_data.endswith(encoded_args)
