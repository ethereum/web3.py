import pytest

from web3.exceptions import (
    BadFunctionCallOutput,
    InvalidAddress,
)

from web3.utils.datastructures import (
    HexBytes,
)
from web3.utils.ens import (
    contract_ens_addresses,
)

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


def deploy(web3, Contract, args=None):
    deploy_txn = Contract.deploy(args=args)
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    contract = Contract(address=deploy_receipt['contractAddress'])
    return contract


@pytest.fixture()
def address_reflector_contract(web3, AddressReflectorContract):
    return deploy(web3, AddressReflectorContract)


@pytest.fixture()
def math_contract(web3, MathContract):
    return deploy(web3, MathContract)


@pytest.fixture()
def string_contract(web3, StringContract):
    return deploy(web3, StringContract, args=["Caqalai"])


@pytest.fixture()
def address_contract(web3, WithConstructorAddressArgumentsContract):
    return deploy(web3, WithConstructorAddressArgumentsContract, args=[
        "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
    ])


@pytest.fixture(params=[b'\x04\x06', '0x0406', '0406'])
def bytes_contract(web3, BytesContract, request):
    return deploy(web3, BytesContract, args=[request.param])


@pytest.fixture(params=[
    '0x0406040604060406040604060406040604060406040604060406040604060406',
    '0406040604060406040604060406040604060406040604060406040604060406',
    HexBytes('0406040604060406040604060406040604060406040604060406040604060406'),
])
def bytes32_contract(web3, Bytes32Contract, request):
    return deploy(web3, Bytes32Contract, args=[request.param])


@pytest.fixture()
def undeployed_math_contract(web3, MathContract):
    empty_address = "0x000000000000000000000000000000000000dEaD"
    _undeployed_math_contract = MathContract(address=empty_address)
    return _undeployed_math_contract


@pytest.fixture()
def mismatched_math_contract(web3, StringContract, MathContract):
    deploy_txn = StringContract.deploy(args=["Caqalai"])
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None

    _mismatched_math_contract = MathContract(address=deploy_receipt['contractAddress'])
    return _mismatched_math_contract


def test_invalid_address_in_deploy_arg(web3, WithConstructorAddressArgumentsContract):
    with pytest.raises(InvalidAddress):
        WithConstructorAddressArgumentsContract.deploy(args=[
            "0xd3cda913deb6f67967b99d67acdfa1712c293601",
        ])


def test_call_with_no_arguments(math_contract):
    result = math_contract.call().return13()
    assert result == 13


def test_call_with_one_argument(math_contract):
    result = math_contract.call().multiply7(3)
    assert result == 21


@pytest.mark.parametrize(
    'call_args,call_kwargs',
    (
        ((9, 7), {}),
        ((9,), {'b': 7}),
        (tuple(), {'a': 9, 'b': 7}),
    ),
)
def test_call_with_multiple_arguments(math_contract, call_args, call_kwargs):
    result = math_contract.call().add(*call_args, **call_kwargs)
    assert result == 16


def test_call_get_string_value(string_contract):
    result = string_contract.call().getValue()
    # eth_abi.decode_api() does not assume implicit utf-8
    # encoding of string return values. Thus, we need to decode
    # ourselves for fair comparison.
    assert result == "Caqalai"


def test_call_read_string_variable(string_contract):
    result = string_contract.call().constValue()
    assert result == b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff".decode(errors='backslashreplace')  # noqa: E501


def test_call_read_address_variable(address_contract):
    result = address_contract.call().testAddr()
    assert result == "0xd3CdA913deB6f67967B99D67aCDFa1712C293601"


def test_init_with_ens_name_arg(web3, WithConstructorAddressArgumentsContract):
    with contract_ens_addresses(
        WithConstructorAddressArgumentsContract,
        [("arg-name.eth", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413")],
    ):
        address_contract = deploy(web3, WithConstructorAddressArgumentsContract, args=[
            "arg-name.eth",
        ])

    assert address_contract.call().testAddr() == "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"


def test_call_read_bytes_variable(bytes_contract):
    result = bytes_contract.call().constValue()
    assert result == b"\x01\x23"


def test_call_get_bytes_value(bytes_contract):
    result = bytes_contract.call().getValue()
    assert result == b'\x04\x06'


def test_call_read_bytes32_variable(bytes32_contract):
    result = bytes32_contract.call().constValue()
    assert result == b"\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23"  # noqa


def test_call_get_bytes32_value(bytes32_contract):
    result = bytes32_contract.call().getValue()
    assert result == b'\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06'  # noqa


@pytest.mark.parametrize(
    'value, expected',
    [
        (
            '0x' + '11' * 20,
            '0x' + '11' * 20,
        ),
        (
            '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
            InvalidAddress,
        ),
        (
            '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413',
            '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413',
        ),
    ]
)
def test_call_address_reflector_with_address(address_reflector_contract, value, expected):
    if not isinstance(expected, str):
        with pytest.raises(expected):
            address_reflector_contract.call().reflect(value)
    else:
        assert address_reflector_contract.call().reflect(value) == expected


@pytest.mark.parametrize(
    'value, expected',
    [
        (
            ['0x' + '11' * 20, '0x' + '22' * 20],
            ['0x' + '11' * 20, '0x' + '22' * 20],
        ),
        (
            ['0x' + '11' * 20, '0x' + 'aa' * 20],
            InvalidAddress
        ),
        (
            [
                '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4',
                '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413',
            ],
            [
                '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4',
                '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413',
            ],
        ),
    ]
)
def test_call_address_list_reflector_with_address(address_reflector_contract, value, expected):
    if not isinstance(expected, list):
        with pytest.raises(expected):
            address_reflector_contract.call().reflect(value)
    else:
        assert address_reflector_contract.call().reflect(value) == expected


def test_call_address_reflector_single_name(address_reflector_contract):
    with contract_ens_addresses(
        address_reflector_contract,
        [("dennisthepeasant.eth", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413")],
    ):
        result = address_reflector_contract.call().reflect('dennisthepeasant.eth')
        assert result == '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413'


def test_call_address_reflector_name_array(address_reflector_contract):
    names = [
        'autonomouscollective.eth',
        'wedonthavealord.eth',
    ]
    addresses = [
        '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413',
        '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4',
    ]

    with contract_ens_addresses(address_reflector_contract, zip(names, addresses)):
        result = address_reflector_contract.call().reflect(names)

    assert addresses == result


def test_call_reject_invalid_ens_name(address_reflector_contract):
    with contract_ens_addresses(address_reflector_contract, []):
        with pytest.raises(ValueError):
            address_reflector_contract.call().reflect('typ0.eth')


def test_call_missing_function(mismatched_math_contract):
    expected_missing_function_error_message = "Could not decode contract function call"
    with pytest.raises(BadFunctionCallOutput) as exception_info:
        mismatched_math_contract.call().return13()
    assert expected_missing_function_error_message in str(exception_info.value)


def test_call_undeployed_contract(undeployed_math_contract):
    expected_undeployed_call_error_message = "Could not transact with/call contract function"
    with pytest.raises(BadFunctionCallOutput) as exception_info:
        undeployed_math_contract.call().return13()
    assert expected_undeployed_call_error_message in str(exception_info.value)
