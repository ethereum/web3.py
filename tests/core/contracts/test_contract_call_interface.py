from decimal import (
    Decimal,
    getcontext,
)
import json
import pytest

from eth_tester.exceptions import (
    TransactionFailed,
)
from eth_utils import (
    is_text,
)
from hexbytes import (
    HexBytes,
)
import pytest_asyncio

from _utils import (
    async_deploy,
    deploy,
)
from web3._utils.ens import (
    contract_ens_addresses,
)
from web3.exceptions import (
    BadFunctionCallOutput,
    BlockNumberOutofRange,
    FallbackNotFound,
    InvalidAddress,
    MismatchedABI,
    NoABIFound,
    NoABIFunctionsFound,
    ValidationError,
)

MULTIPLE_FUNCTIONS = json.loads(
    '[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"bytes32"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"uint8"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"int8"}],"name":"a","outputs":[],"type":"function"}]'  # noqa: E501
)


@pytest.fixture(params=[b"\x04\x06", "0x0406", "0406"])
def bytes_contract(w3, BytesContract, request, address_conversion_func):
    if is_text(request.param) and request.param[:2] != "0x":
        with pytest.warns(
            DeprecationWarning,
            match="in v6 it will be invalid to pass a hex string without "
            'the "0x" prefix',
        ):
            return deploy(
                w3, BytesContract, address_conversion_func, args=[request.param]
            )
    else:
        return deploy(w3, BytesContract, address_conversion_func, args=[request.param])


@pytest_asyncio.fixture(params=[b"\x04\x06", "0x0406", "0406"])
async def async_bytes_contract(
    async_w3, AsyncBytesContract, request, address_conversion_func
):
    if is_text(request.param) and request.param[:2] != "0x":
        with pytest.warns(
            DeprecationWarning,
            match="in v6 it will be invalid to pass a hex string without "
            'the "0x" prefix',
        ):
            return await async_deploy(
                async_w3,
                AsyncBytesContract,
                address_conversion_func,
                args=[request.param],
            )
    else:
        return await async_deploy(
            async_w3, AsyncBytesContract, address_conversion_func, args=[request.param]
        )


@pytest.fixture()
def fixed_reflection_contract(w3, FixedReflectionContract, address_conversion_func):
    return deploy(w3, FixedReflectionContract, address_conversion_func)


@pytest_asyncio.fixture()
async def async_fixed_reflection_contract(
    async_w3, AsyncFixedReflectionContract, address_conversion_func
):
    return await async_deploy(
        async_w3, AsyncFixedReflectionContract, address_conversion_func
    )


@pytest.fixture()
def call_transaction():
    return {"data": "0x61bc221a", "to": "0xc305c901078781C232A2a521C2aF7980f8385ee9"}


@pytest.fixture(
    params=[
        "0x0406040604060406040604060406040604060406040604060406040604060406",
        "0406040604060406040604060406040604060406040604060406040604060406",
        HexBytes("0406040604060406040604060406040604060406040604060406040604060406"),
    ]
)
def bytes32_contract(w3, Bytes32Contract, request, address_conversion_func):
    if is_text(request.param) and request.param[:2] != "0x":
        with pytest.warns(DeprecationWarning):
            return deploy(
                w3, Bytes32Contract, address_conversion_func, args=[request.param]
            )
    else:
        return deploy(
            w3, Bytes32Contract, address_conversion_func, args=[request.param]
        )


@pytest_asyncio.fixture(
    params=[
        "0x0406040604060406040604060406040604060406040604060406040604060406",
        "0406040604060406040604060406040604060406040604060406040604060406",
        HexBytes("0406040604060406040604060406040604060406040604060406040604060406"),
    ]
)
async def async_bytes32_contract(
    async_w3, AsyncBytes32Contract, request, address_conversion_func
):
    if is_text(request.param) and request.param[:2] != "0x":
        with pytest.warns(DeprecationWarning):
            return await async_deploy(
                async_w3,
                AsyncBytes32Contract,
                address_conversion_func,
                args=[request.param],
            )
    else:
        return await async_deploy(
            async_w3,
            AsyncBytes32Contract,
            address_conversion_func,
            args=[request.param],
        )


@pytest.fixture()
def undeployed_math_contract(MathContract, address_conversion_func):
    empty_address = address_conversion_func(
        "0x000000000000000000000000000000000000dEaD"
    )
    _undeployed_math_contract = MathContract(address=empty_address)
    return _undeployed_math_contract


@pytest_asyncio.fixture()
async def async_undeployed_math_contract(AsyncMathContract, address_conversion_func):
    empty_address = address_conversion_func(
        "0x000000000000000000000000000000000000dEaD"
    )
    _undeployed_math_contract = AsyncMathContract(address=empty_address)
    return _undeployed_math_contract


@pytest.fixture()
def mismatched_math_contract(w3, StringContract, MathContract, address_conversion_func):
    deploy_txn = StringContract.constructor("Caqalai").transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    address = address_conversion_func(deploy_receipt["contractAddress"])
    _mismatched_math_contract = MathContract(address=address)
    return _mismatched_math_contract


@pytest_asyncio.fixture()
async def async_mismatched_math_contract(
    async_w3, AsyncStringContract, AsyncMathContract, address_conversion_func
):
    deploy_txn = await AsyncStringContract.constructor("Caqalai").transact()
    deploy_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    address = address_conversion_func(deploy_receipt["contractAddress"])
    _mismatched_math_contract = AsyncMathContract(address=address)
    return _mismatched_math_contract


@pytest.fixture()
def tuple_contract(w3, TupleContract, address_conversion_func):
    return deploy(w3, TupleContract, address_conversion_func)


@pytest_asyncio.fixture()
async def async_tuple_contract(async_w3, AsyncTupleContract, address_conversion_func):
    return await async_deploy(async_w3, AsyncTupleContract, address_conversion_func)


@pytest.fixture()
def nested_tuple_contract(w3, NestedTupleContract, address_conversion_func):
    return deploy(w3, NestedTupleContract, address_conversion_func)


@pytest_asyncio.fixture()
async def async_nested_tuple_contract(
    async_w3, AsyncNestedTupleContract, address_conversion_func
):
    return await async_deploy(
        async_w3, AsyncNestedTupleContract, address_conversion_func
    )


def test_invalid_address_in_deploy_arg(WithConstructorAddressArgumentsContract):
    with pytest.raises(InvalidAddress):
        WithConstructorAddressArgumentsContract.constructor(
            "0xd3cda913deb6f67967b99d67acdfa1712c293601",
        ).transact()


def test_call_with_no_arguments(math_contract, call):
    result = call(contract=math_contract, contract_function="return13")
    assert result == 13


def test_call_with_one_argument(math_contract, call):
    result = call(contract=math_contract, contract_function="multiply7", func_args=[3])
    assert result == 21


@pytest.mark.parametrize(
    "call_args,call_kwargs",
    (
        ((9, 7), {}),
        ((9,), {"b": 7}),
        (tuple(), {"a": 9, "b": 7}),
    ),
)
def test_call_with_multiple_arguments(math_contract, call, call_args, call_kwargs):
    result = call(
        contract=math_contract,
        contract_function="add",
        func_args=call_args,
        func_kwargs=call_kwargs,
    )
    assert result == 16


@pytest.mark.parametrize(
    "call_args,call_kwargs",
    (
        ((9, 7), {}),
        ((9,), {"b": 7}),
        (tuple(), {"a": 9, "b": 7}),
    ),
)
def test_saved_method_call_with_multiple_arguments(
    math_contract, call_args, call_kwargs
):
    math_contract_add = math_contract.functions.add(*call_args, **call_kwargs)
    result = math_contract_add.call()
    assert result == 16


def test_call_get_string_value(string_contract, call):
    result = call(contract=string_contract, contract_function="getValue")
    # eth_abi.decode_abi() does not assume implicit utf-8
    # encoding of string return values. Thus, we need to decode
    # ourselves for fair comparison.
    assert result == "Caqalai"


def test_call_get_bytes32_array(arrays_contract, call):
    result = call(contract=arrays_contract, contract_function="getBytes32Value")
    # expected_bytes32_array = [keccak('0'), keccak('1')]
    expected_bytes32_array = [
        b"\x04HR\xb2\xa6p\xad\xe5@~x\xfb(c\xc5\x1d\xe9\xfc\xb9eB\xa0q\x86\xfe:\xed\xa6\xbb\x8a\x11m",  # noqa: E501
        b"\xc8\x9e\xfd\xaaT\xc0\xf2\x0cz\xdfa(\x82\xdf\tP\xf5\xa9Qc~\x03\x07\xcd\xcbLg/)\x8b\x8b\xc6",  # noqa: E501
    ]
    assert result == expected_bytes32_array


def test_call_get_bytes32_const_array(arrays_contract, call):
    result = call(contract=arrays_contract, contract_function="getBytes32ConstValue")
    # expected_bytes32_array = [keccak('A'), keccak('B')]
    expected_bytes32_array = [
        b"\x03x?\xac.\xfe\xd8\xfb\xc9\xadD>Y.\xe3\x0ea\xd6_G\x11@\xc1\x0c\xa1U\xe97\xb45\xb7`",  # noqa: E501
        b"\x1fg[\xff\x07Q_]\xf9g7\x19N\xa9E\xc3lA\xe7\xb4\xfc\xef0{|\xd4\xd0\xe6\x02\xa6\x91\x11",  # noqa: E501
    ]
    assert result == expected_bytes32_array


def test_call_get_byte_array(arrays_contract, call):
    result = call(contract=arrays_contract, contract_function="getByteValue")
    expected_byte_arr = [b"\xff", b"\xff", b"\xff", b"\xff"]
    assert result == expected_byte_arr


@pytest.mark.parametrize("args,expected", [([b""], [b"\x00"]), (["0x"], [b"\x00"])])
def test_set_byte_array(arrays_contract, call, transact, args, expected):
    transact(
        contract=arrays_contract, contract_function="setByteValue", func_args=[args]
    )
    result = call(contract=arrays_contract, contract_function="getByteValue")

    assert result == expected


@pytest.mark.parametrize("args,expected", [([b"1"], [b"1"]), (["0xDe"], [b"\xDe"])])
def test_set_strict_byte_array(strict_arrays_contract, call, transact, args, expected):
    transact(
        contract=strict_arrays_contract,
        contract_function="setByteValue",
        func_args=[args],
    )
    result = call(contract=strict_arrays_contract, contract_function="getByteValue")

    assert result == expected


@pytest.mark.parametrize("args", ([""], ["s"]))
def test_set_strict_byte_array_with_invalid_args(
    strict_arrays_contract, transact, args
):
    with pytest.raises(ValidationError):
        transact(
            contract=strict_arrays_contract,
            contract_function="setByteValue",
            func_args=[args],
        )


def test_call_get_byte_const_array(arrays_contract, call):
    result = call(contract=arrays_contract, contract_function="getByteConstValue")
    expected_byte_arr = [b"\x00", b"\x01"]
    assert result == expected_byte_arr


def test_call_read_address_variable(address_contract, call):
    result = call(contract=address_contract, contract_function="testAddr")
    assert result == "0xd3CdA913deB6f67967B99D67aCDFa1712C293601"


def test_init_with_ens_name_arg(w3, WithConstructorAddressArgumentsContract, call):
    with contract_ens_addresses(
        WithConstructorAddressArgumentsContract,
        [("arg-name.eth", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413")],
    ):
        address_contract = deploy(
            w3,
            WithConstructorAddressArgumentsContract,
            args=[
                "arg-name.eth",
            ],
        )

    result = call(contract=address_contract, contract_function="testAddr")
    assert result == "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"


def test_call_read_bytes_variable(bytes_contract, call):
    result = call(contract=bytes_contract, contract_function="constValue")
    assert result == b"\x01\x23"


def test_call_get_bytes_value(bytes_contract, call):
    result = call(contract=bytes_contract, contract_function="getValue")
    assert result == b"\x04\x06"


def test_call_read_bytes32_variable(bytes32_contract, call):
    result = call(contract=bytes32_contract, contract_function="constValue")
    assert (
        result
        == b"\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23"  # noqa: E501
    )


def test_call_get_bytes32_value(bytes32_contract, call):
    result = call(contract=bytes32_contract, contract_function="getValue")
    assert (
        result
        == b"\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06"  # noqa: E501
    )


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "0x" + "11" * 20,
            "0x" + "11" * 20,
        ),
        (
            "0xbb9bc244d798123fde783fcc1c72d3bb8c189413",
            InvalidAddress,
        ),
        (
            "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
            "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
        ),
    ],
)
def test_call_address_reflector_with_address(
    address_reflector_contract, value, expected, call
):
    if not isinstance(expected, str):
        with pytest.raises(expected):
            call(
                contract=address_reflector_contract,
                contract_function="reflect",
                func_args=[value],
            )
    else:
        assert (
            call(
                contract=address_reflector_contract,
                contract_function="reflect",
                func_args=[value],
            )
            == expected
        )


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            ["0x" + "11" * 20, "0x" + "22" * 20],
            ["0x" + "11" * 20, "0x" + "22" * 20],
        ),
        (["0x" + "11" * 20, "0x" + "aa" * 20], InvalidAddress),
        (
            [
                "0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4",
                "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
            ],
            [
                "0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4",
                "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
            ],
        ),
    ],
)
def test_call_address_list_reflector_with_address(
    address_reflector_contract, value, expected, call
):
    if not isinstance(expected, list):
        with pytest.raises(expected):
            call(
                contract=address_reflector_contract,
                contract_function="reflect",
                func_args=[value],
            )
    else:
        assert (
            call(
                contract=address_reflector_contract,
                contract_function="reflect",
                func_args=[value],
            )
            == expected
        )


def test_call_address_reflector_single_name(address_reflector_contract, call):
    with contract_ens_addresses(
        address_reflector_contract,
        [("dennisthepeasant.eth", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413")],
    ):
        result = call(
            contract=address_reflector_contract,
            contract_function="reflect",
            func_args=["dennisthepeasant.eth"],
        )
        assert result == "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"


def test_call_address_reflector_name_array(address_reflector_contract, call):
    names = [
        "autonomouscollective.eth",
        "wedonthavealord.eth",
    ]
    addresses = [
        "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
        "0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4",
    ]

    with contract_ens_addresses(address_reflector_contract, zip(names, addresses)):
        result = call(
            contract=address_reflector_contract,
            contract_function="reflect",
            func_args=[names],
        )

    assert addresses == result


def test_call_reject_invalid_ens_name(address_reflector_contract, call):
    with contract_ens_addresses(address_reflector_contract, []):
        with pytest.raises(ValueError):
            call(
                contract=address_reflector_contract,
                contract_function="reflect",
                func_args=["type0.eth"],
            )


def test_call_missing_function(mismatched_math_contract, call):
    expected_missing_function_error_message = "Could not decode contract function call"
    with pytest.raises(BadFunctionCallOutput) as exception_info:
        call(contract=mismatched_math_contract, contract_function="return13")
    assert expected_missing_function_error_message in str(exception_info.value)


def test_call_undeployed_contract(undeployed_math_contract, call):
    expected_undeployed_call_error_message = (
        "Could not transact with/call contract function"
    )
    with pytest.raises(BadFunctionCallOutput) as exception_info:
        call(contract=undeployed_math_contract, contract_function="return13")
    assert expected_undeployed_call_error_message in str(exception_info.value)


def test_call_fallback_function(fallback_function_contract):
    result = fallback_function_contract.fallback.call()
    assert result == []


@pytest.mark.parametrize(
    "tx_params,contract_name,expected",
    (
        ({"gas": 210000}, "no_receive", "fallback"),
        ({"gas": 210000, "value": 2}, "no_receive", ""),
        ({"value": 2, "gas": 210000, "data": "0x477a5c98"}, "no_receive", ""),
        ({"gas": 210000, "data": "0x477a5c98"}, "no_receive", "fallback"),
        ({"data": "0x477a5c98"}, "receive", "fallback"),
        ({"value": 2}, "receive", "receive"),
    ),
)
def test_call_receive_fallback_function(
    w3,
    tx_params,
    expected,
    call,
    receive_function_contract,
    no_receive_function_contract,
    contract_name,
):
    if contract_name == "receive":
        contract = receive_function_contract
    elif contract_name == "no_receive":
        contract = no_receive_function_contract
    else:
        raise AssertionError("contract must be either receive or no_receive")

    initial_value = call(contract=contract, contract_function="getText")
    assert initial_value == ""
    to = {"to": contract.address}
    merged = {**to, **tx_params}
    w3.eth.send_transaction(merged)
    final_value = call(contract=contract, contract_function="getText")
    assert final_value == expected


def test_call_nonexistent_receive_function(fallback_function_contract):
    with pytest.raises(FallbackNotFound, match="No receive function was found"):
        fallback_function_contract.receive.call()


def test_throws_error_if_block_out_of_range(w3, math_contract):
    w3.provider.make_request(method="evm_mine", params=[20])
    with pytest.raises(BlockNumberOutofRange):
        math_contract.functions.counter().call(block_identifier=-50)


def test_accepts_latest_block(w3, math_contract):
    w3.provider.make_request(method="evm_mine", params=[5])
    math_contract.functions.increment().transact()

    late = math_contract.functions.counter().call(block_identifier="latest")
    pend = math_contract.functions.counter().call(block_identifier="pending")

    assert late == 1
    assert pend == 1


def test_accepts_block_hash_as_identifier(w3, math_contract):
    blocks = w3.provider.make_request(method="evm_mine", params=[5])
    math_contract.functions.increment().transact()
    more_blocks = w3.provider.make_request(method="evm_mine", params=[5])

    old = math_contract.functions.counter().call(block_identifier=blocks["result"][2])
    new = math_contract.functions.counter().call(
        block_identifier=more_blocks["result"][2]
    )

    assert old == 0
    assert new == 1


def test_neg_block_indexes_from_the_end(w3, math_contract):
    w3.provider.make_request(method="evm_mine", params=[5])
    math_contract.functions.increment().transact()
    math_contract.functions.increment().transact()
    w3.provider.make_request(method="evm_mine", params=[5])

    output1 = math_contract.functions.counter().call(block_identifier=-7)
    output2 = math_contract.functions.counter().call(block_identifier=-6)

    assert output1 == 1
    assert output2 == 2


def test_returns_data_from_specified_block(w3, math_contract):
    start_num = w3.eth.get_block("latest").number
    w3.provider.make_request(method="evm_mine", params=[5])
    math_contract.functions.increment().transact()
    math_contract.functions.increment().transact()

    output1 = math_contract.functions.counter().call(block_identifier=start_num + 6)
    output2 = math_contract.functions.counter().call(block_identifier=start_num + 7)

    assert output1 == 1
    assert output2 == 2


message_regex = (
    r"\nCould not identify the intended function with name `.*`, positional arguments "
    r"with type\(s\) `.*` and keyword arguments with type\(s\) `.*`."
    r"\nFound .* function\(s\) with the name `.*`: .*"
)
diagnosis_arg_regex = (
    r"\nFunction invocation failed due to improper number of arguments."
)
diagnosis_encoding_regex = (
    r"\nFunction invocation failed due to no matching argument types."
)
diagnosis_ambiguous_encoding = (
    r"\nAmbiguous argument encoding. "
    r"Provided arguments can be encoded to multiple functions matching this call."
)


def test_no_functions_match_identifier(arrays_contract):
    with pytest.raises(MismatchedABI):
        arrays_contract.functions.thisFunctionDoesNotExist().call()


def test_function_1_match_identifier_wrong_number_of_args(arrays_contract):
    regex = message_regex + diagnosis_arg_regex
    with pytest.raises(ValidationError, match=regex):
        arrays_contract.functions.setBytes32Value().call()


def test_function_1_match_identifier_wrong_args_encoding(arrays_contract):
    regex = message_regex + diagnosis_encoding_regex
    with pytest.raises(ValidationError, match=regex):
        arrays_contract.functions.setBytes32Value("dog").call()


@pytest.mark.parametrize(
    "arg1,arg2,diagnosis",
    (
        (100, "dog", diagnosis_arg_regex),
        ("dog", None, diagnosis_encoding_regex),
        (100, None, diagnosis_ambiguous_encoding),
    ),
)
def test_function_multiple_error_diagnoses(w3, arg1, arg2, diagnosis):
    Contract = w3.eth.contract(abi=MULTIPLE_FUNCTIONS)
    regex = message_regex + diagnosis
    with pytest.raises(ValidationError, match=regex):
        if arg2:
            Contract.functions.a(arg1, arg2).call()
        else:
            Contract.functions.a(arg1).call()


@pytest.mark.parametrize(
    "address", (
        "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",  # checksummed
        b'\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee',  # noqa: E501
    )
)
def test_function_wrong_args_for_tuple_collapses_args_in_message(
    address, tuple_contract,
):
    with pytest.raises(ValidationError) as e:
        tuple_contract.functions.method(
            (1, [2, 3], [(4, [True, [False]], [address])])
        ).call()

    # assert the user arguments are formatted as expected:
    # (int,(int,int),((int,(bool,(bool)),(address))))
    e.match("\\(int,\\(int,int\\),\\(\\(int,\\(bool,\\(bool\\)\\),\\(address\\)\\)\\)\\)")  # noqa: E501

    # assert the found method signature is formatted as expected:
    # ['method((uint256,uint256[],(int256,bool[2],address[])[]))']
    e.match("\\['method\\(\\(uint256,uint256\\[\\],\\(int256,bool\\[2\\],address\\[\\]\\)\\[\\]\\)\\)'\\]")  # noqa: E501


@pytest.mark.parametrize(
    "address", (
        "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",  # checksummed
        b'\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee',  # noqa: E501
    )
)
def test_function_wrong_args_for_tuple_collapses_kwargs_in_message(
    address, tuple_contract
):
    with pytest.raises(ValidationError) as e:
        tuple_contract.functions.method(
            a=(1, [2, 3], [(4, [True, [False]], [address])])  # noqa: E501
        ).call()

    # assert the user keyword arguments are formatted as expected:
    # {'a': '(int,(int,int),((int,(bool,(bool)),(address))))'}
    e.match("{'a': '\\(int,\\(int,int\\),\\(\\(int,\\(bool,\\(bool\\)\\),\\(address\\)\\)\\)\\)'}")  # noqa: E501

    # assert the found method signature is formatted as expected:
    # ['method((uint256,uint256[],(int256,bool[2],address[])[]))']
    e.match("\\['method\\(\\(uint256,uint256\\[\\],\\(int256,bool\\[2\\],address\\[\\]\\)\\[\\]\\)\\)'\\]")  # noqa: E501


def test_function_no_abi(w3):
    contract = w3.eth.contract()
    with pytest.raises(NoABIFound):
        contract.functions.thisFunctionDoesNotExist().call()


def test_call_abi_no_functions(w3):
    contract = w3.eth.contract(abi=[])
    with pytest.raises(NoABIFunctionsFound):
        contract.functions.thisFunctionDoesNotExist().call()


def test_call_not_sending_ether_to_nonpayable_function(payable_tester_contract, call):
    result = call(contract=payable_tester_contract, contract_function="doNoValueCall")
    assert result == []


def test_call_sending_ether_to_nonpayable_function(payable_tester_contract, call):
    with pytest.raises(ValidationError):
        call(
            contract=payable_tester_contract,
            contract_function="doNoValueCall",
            tx_params={"value": 1},
        )


@pytest.mark.parametrize(
    "function, value",
    (
        # minimum positive unambiguous value (larger than fixed8x1)
        ("reflect", Decimal("12.8")),
        # maximum value (for ufixed256x1)
        ("reflect", Decimal(2**256 - 1) / 10),
        # maximum negative unambiguous value (less than 0 from ufixed*)
        ("reflect", Decimal("-0.1")),
        # minimum value (for fixed8x1)
        ("reflect", Decimal("-12.8")),
        # only ufixed256x80 type supports 2-80 decimals
        ("reflect", Decimal(2**256 - 1) / 10**80),  # maximum allowed value
        ("reflect", Decimal(1) / 10**80),  # smallest non-zero value
        # minimum value (for ufixed8x1)
        ("reflect_short_u", 0),
        # maximum value (for ufixed8x1)
        ("reflect_short_u", Decimal("25.5")),
    ),
)
def test_reflect_fixed_value(fixed_reflection_contract, function, value):
    contract_func = fixed_reflection_contract.functions[function]
    reflected = contract_func(value).call({"gas": 420000})
    assert reflected == value


DEFAULT_DECIMALS = getcontext().prec


@pytest.mark.parametrize(
    "function, value, error",
    (
        # out of range
        ("reflect_short_u", Decimal("25.6"), "no matching argument types"),
        ("reflect_short_u", Decimal("-.1"), "no matching argument types"),
        # too many digits for *x1, too large for 256x80
        ("reflect", Decimal("0.01"), "no matching argument types"),
        # too many digits
        ("reflect_short_u", Decimal("0.01"), "no matching argument types"),
        (
            "reflect_short_u",
            Decimal(f"1e-{DEFAULT_DECIMALS + 1}"),
            "no matching argument types",
        ),
        (
            "reflect_short_u",
            Decimal("25.4" + "9" * DEFAULT_DECIMALS),
            "no matching argument types",
        ),
        ("reflect", Decimal(1) / 10**81, "no matching argument types"),
        # floats not accepted, for floating point error concerns
        ("reflect_short_u", 0.1, "no matching argument types"),
        # ambiguous
        ("reflect", Decimal("12.7"), "Ambiguous argument encoding"),
        ("reflect", Decimal(0), "Ambiguous argument encoding"),
        ("reflect", 0, "Ambiguous argument encoding"),
    ),
)
def test_invalid_fixed_value_reflections(
    fixed_reflection_contract, function, value, error
):
    contract_func = fixed_reflection_contract.functions[function]
    with pytest.raises(ValidationError, match=error):
        contract_func(value).call({"gas": 420000})


@pytest.mark.parametrize(
    "method_input, expected",
    (
        (
            {
                "a": 123,
                "b": [1, 2],
                "c": [
                    {
                        "x": 234,
                        "y": [True, False],
                        "z": [
                            "0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                        ],
                    },
                    {
                        "x": 345,
                        "y": [False, False],
                        "z": [
                            "0xefd1FF70c185A1C0b125939815225199079096Ee",
                            "0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e",
                        ],
                    },
                ],
            },
            (
                123,
                [1, 2],
                [
                    (
                        234,
                        [True, False],
                        [
                            "0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                        ],
                    ),
                    (
                        345,
                        [False, False],
                        [
                            "0xefd1FF70c185A1C0b125939815225199079096Ee",
                            "0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e",
                        ],
                    ),
                ],
            ),
        ),
        (
            (
                123,
                [1, 2],
                [
                    (
                        234,
                        [True, False],
                        [
                            "0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                        ],
                    ),
                    (
                        345,
                        [False, False],
                        [
                            "0xefd1FF70c185A1C0b125939815225199079096Ee",
                            "0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e",
                        ],
                    ),
                ],
            ),
            (
                123,
                [1, 2],
                [
                    (
                        234,
                        [True, False],
                        [
                            "0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                        ],
                    ),
                    (
                        345,
                        [False, False],
                        [
                            "0xefd1FF70c185A1C0b125939815225199079096Ee",
                            "0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e",
                        ],
                    ),
                ],
            ),
        ),
    ),
)
def test_call_tuple_contract(tuple_contract, method_input, expected):
    result = tuple_contract.functions.method(method_input).call()
    assert result == expected


@pytest.mark.parametrize(
    "method_input, expected",
    (
        (
            {
                "t": [
                    {
                        "u": [
                            {"x": 1, "y": 2},
                            {"x": 3, "y": 4},
                            {"x": 5, "y": 6},
                        ]
                    },
                    {
                        "u": [
                            {"x": 7, "y": 8},
                            {"x": 9, "y": 10},
                            {"x": 11, "y": 12},
                        ]
                    },
                ]
            },
            (
                [
                    (
                        [
                            (1, 2),
                            (3, 4),
                            (5, 6),
                        ],
                    ),
                    (
                        [
                            (7, 8),
                            (9, 10),
                            (11, 12),
                        ],
                    ),
                ],
            ),
        ),
        (
            (
                [
                    (
                        [
                            (1, 2),
                            (3, 4),
                            (5, 6),
                        ],
                    ),
                    (
                        [
                            (7, 8),
                            (9, 10),
                            (11, 12),
                        ],
                    ),
                ],
            ),
            (
                [
                    (
                        [
                            (1, 2),
                            (3, 4),
                            (5, 6),
                        ],
                    ),
                    (
                        [
                            (7, 8),
                            (9, 10),
                            (11, 12),
                        ],
                    ),
                ],
            ),
        ),
    ),
)
def test_call_nested_tuple_contract(nested_tuple_contract, method_input, expected):
    result = nested_tuple_contract.functions.method(method_input).call()
    assert result == expected


def test_call_revert_contract(revert_contract):
    with pytest.raises(TransactionFailed, match="Function has been reverted."):
        # eth-tester will do a gas estimation if we don't submit a gas value,
        # which does not contain the revert reason. Avoid that by giving a gas
        # value.
        revert_contract.functions.revertWithMessage().call({"gas": 100000})


@pytest.mark.asyncio
async def test_async_invalid_address_in_deploy_arg(
    AsyncWithConstructorAddressArgumentsContract,
):
    with pytest.raises(InvalidAddress):
        await AsyncWithConstructorAddressArgumentsContract.constructor(
            "0xd3cda913deb6f67967b99d67acdfa1712c293601",
        ).transact()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "call_args,call_kwargs",
    (
        ((9, 7), {}),
        ((9,), {"b": 7}),
        (tuple(), {"a": 9, "b": 7}),
    ),
)
async def test_async_call_with_multiple_arguments(
    async_math_contract, async_call, call_args, call_kwargs
):
    result = await async_call(
        contract=async_math_contract,
        contract_function="add",
        func_args=call_args,
        func_kwargs=call_kwargs,
    )
    assert result == 16


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "call_args,call_kwargs",
    (
        ((9, 7), {}),
        ((9,), {"b": 7}),
        (tuple(), {"a": 9, "b": 7}),
    ),
)
async def test_async_saved_method_call_with_multiple_arguments(
    async_math_contract, call_args, call_kwargs
):
    math_contract_add = async_math_contract.functions.add(*call_args, **call_kwargs)
    result = await math_contract_add.call()
    assert result == 16


@pytest.mark.asyncio
async def test_async_call_get_string_value(async_string_contract, async_call):
    result = await async_call(
        contract=async_string_contract, contract_function="getValue"
    )
    # eth_abi.decode_abi() does not assume implicit utf-8
    # encoding of string return values. Thus, we need to decode
    # ourselves for fair comparison.
    assert result == "Caqalai"


@pytest.mark.asyncio
async def test_async_call_get_bytes32_array(async_arrays_contract, async_call):
    result = await async_call(
        contract=async_arrays_contract, contract_function="getBytes32Value"
    )
    # expected_bytes32_array = [keccak('0'), keccak('1')]
    expected_bytes32_array = [
        b"\x04HR\xb2\xa6p\xad\xe5@~x\xfb(c\xc5\x1d\xe9\xfc\xb9eB\xa0q\x86\xfe:\xed\xa6\xbb\x8a\x11m",  # noqa: E501
        b"\xc8\x9e\xfd\xaaT\xc0\xf2\x0cz\xdfa(\x82\xdf\tP\xf5\xa9Qc~\x03\x07\xcd\xcbLg/)\x8b\x8b\xc6",  # noqa: E501
    ]
    assert result == expected_bytes32_array


@pytest.mark.asyncio
async def test_async_call_get_bytes32_const_array(async_arrays_contract, async_call):
    result = await async_call(
        contract=async_arrays_contract, contract_function="getBytes32ConstValue"
    )
    # expected_bytes32_array = [keccak('A'), keccak('B')]
    expected_bytes32_array = [
        b"\x03x?\xac.\xfe\xd8\xfb\xc9\xadD>Y.\xe3\x0ea\xd6_G\x11@\xc1\x0c\xa1U\xe97\xb45\xb7`",  # noqa: E501
        b"\x1fg[\xff\x07Q_]\xf9g7\x19N\xa9E\xc3lA\xe7\xb4\xfc\xef0{|\xd4\xd0\xe6\x02\xa6\x91\x11",  # noqa: E501
    ]
    assert result == expected_bytes32_array


@pytest.mark.asyncio
async def test_async_call_get_byte_array(async_arrays_contract, async_call):
    result = await async_call(
        contract=async_arrays_contract, contract_function="getByteValue"
    )
    expected_byte_arr = [b"\xff", b"\xff", b"\xff", b"\xff"]
    assert result == expected_byte_arr


@pytest.mark.asyncio
@pytest.mark.parametrize("args,expected", [([b""], [b"\x00"]), (["0x"], [b"\x00"])])
async def test_async_set_byte_array(
    async_arrays_contract, async_call, async_transact, args, expected
):
    await async_transact(
        contract=async_arrays_contract,
        contract_function="setByteValue",
        func_args=[args],
    )
    result = await async_call(
        contract=async_arrays_contract, contract_function="getByteValue"
    )

    assert result == expected


@pytest.mark.asyncio
@pytest.mark.parametrize("args,expected", [([b"1"], [b"1"]), (["0xDe"], [b"\xDe"])])
async def test_async_set_strict_byte_array(
    async_strict_arrays_contract, async_call, async_transact, args, expected
):
    await async_transact(
        contract=async_strict_arrays_contract,
        contract_function="setByteValue",
        func_args=[args],
    )
    result = await async_call(
        contract=async_strict_arrays_contract, contract_function="getByteValue"
    )

    assert result == expected


@pytest.mark.asyncio
@pytest.mark.parametrize("args", ([""], ["s"]))
async def test_async_set_strict_byte_array_with_invalid_args(
    async_strict_arrays_contract, async_transact, args
):
    with pytest.raises(ValidationError):
        await async_transact(
            contract=async_strict_arrays_contract,
            contract_function="setByteValue",
            func_args=[args],
        )


@pytest.mark.asyncio
async def test_async_call_get_byte_const_array(async_arrays_contract, async_call):
    result = await async_call(
        contract=async_arrays_contract, contract_function="getByteConstValue"
    )
    expected_byte_arr = [b"\x00", b"\x01"]
    assert result == expected_byte_arr


@pytest.mark.asyncio
async def test_async_call_read_address_variable(async_address_contract, async_call):
    result = await async_call(
        contract=async_address_contract, contract_function="testAddr"
    )
    assert result == "0xd3CdA913deB6f67967B99D67aCDFa1712C293601"


@pytest.mark.xfail
@pytest.mark.asyncio
async def test_async_init_with_ens_name_arg(
    async_w3, AsyncWithConstructorAddressArgumentsContract, async_call
):
    with contract_ens_addresses(
        AsyncWithConstructorAddressArgumentsContract,
        [("arg-name.eth", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413")],
    ):
        address_contract = await async_deploy(
            async_w3,
            AsyncWithConstructorAddressArgumentsContract,
            args=[
                "arg-name.eth",
            ],
        )

    result = await async_call(contract=address_contract, contract_function="testAddr")
    assert result == "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"


@pytest.mark.asyncio
async def test_async_call_read_bytes_variable(async_bytes_contract, async_call):
    result = await async_call(
        contract=async_bytes_contract, contract_function="constValue"
    )
    assert result == b"\x01\x23"


@pytest.mark.asyncio
async def test_async_call_get_bytes_value(async_bytes_contract, async_call):
    result = await async_call(
        contract=async_bytes_contract, contract_function="getValue"
    )
    assert result == b"\x04\x06"


@pytest.mark.asyncio
async def test_async_call_read_bytes32_variable(async_bytes32_contract, async_call):
    result = await async_call(
        contract=async_bytes32_contract, contract_function="constValue"
    )
    assert (
        result
        == b"\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23\x01\x23"  # noqa: E501
    )


@pytest.mark.asyncio
async def test_async_call_get_bytes32_value(async_bytes32_contract, async_call):
    result = await async_call(
        contract=async_bytes32_contract, contract_function="getValue"
    )
    assert (
        result
        == b"\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06\x04\x06"  # noqa: E501
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "0x" + "11" * 20,
            "0x" + "11" * 20,
        ),
        (
            "0xbb9bc244d798123fde783fcc1c72d3bb8c189413",
            InvalidAddress,
        ),
        (
            "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
            "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
        ),
    ],
)
async def test_async_call_address_reflector_with_address(
    async_address_reflector_contract, value, expected, async_call
):
    if not isinstance(expected, str):
        with pytest.raises(expected):
            await async_call(
                contract=async_address_reflector_contract,
                contract_function="reflect",
                func_args=[value],
            )
    else:
        assert (
            await async_call(
                contract=async_address_reflector_contract,
                contract_function="reflect",
                func_args=[value],
            )
            == expected
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            ["0x" + "11" * 20, "0x" + "22" * 20],
            ["0x" + "11" * 20, "0x" + "22" * 20],
        ),
        (["0x" + "11" * 20, "0x" + "aa" * 20], InvalidAddress),
        (
            [
                "0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4",
                "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
            ],
            [
                "0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4",
                "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
            ],
        ),
    ],
)
async def test_async_call_address_list_reflector_with_address(
    async_address_reflector_contract, value, expected, async_call
):
    if not isinstance(expected, list):
        with pytest.raises(expected):
            await async_call(
                contract=async_address_reflector_contract,
                contract_function="reflect",
                func_args=[value],
            )
    else:
        assert (
            await async_call(
                contract=async_address_reflector_contract,
                contract_function="reflect",
                func_args=[value],
            )
            == expected
        )


@pytest.mark.xfail
@pytest.mark.asyncio
async def test_async_call_address_reflector_single_name(
    async_address_reflector_contract, async_call
):
    with contract_ens_addresses(
        async_address_reflector_contract,
        [("dennisthepeasant.eth", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413")],
    ):
        result = await async_call(
            contract=async_address_reflector_contract,
            contract_function="reflect",
            func_args=["dennisthepeasant.eth"],
        )
        assert result == "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"


@pytest.mark.xfail
@pytest.mark.asyncio
async def test_async_call_address_reflector_name_array(
    async_address_reflector_contract, async_call
):
    names = [
        "autonomouscollective.eth",
        "wedonthavealord.eth",
    ]
    addresses = [
        "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
        "0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4",
    ]

    with contract_ens_addresses(
        async_address_reflector_contract, zip(names, addresses)
    ):
        result = await async_call(
            contract=async_address_reflector_contract,
            contract_function="reflect",
            func_args=[names],
        )

    assert addresses == result


@pytest.mark.xfail
@pytest.mark.asyncio
async def test_async_call_reject_invalid_ens_name(
    async_address_reflector_contract, async_call
):
    with contract_ens_addresses(async_address_reflector_contract, []):
        with pytest.raises(ValueError):
            await async_call(
                contract=async_address_reflector_contract,
                contract_function="reflect",
                func_args=["type0.eth"],
            )


@pytest.mark.asyncio
async def test_async_call_missing_function(async_mismatched_math_contract, async_call):
    expected_missing_function_error_message = "Could not decode contract function call"
    with pytest.raises(BadFunctionCallOutput) as exception_info:
        await async_call(
            contract=async_mismatched_math_contract, contract_function="return13"
        )
    assert expected_missing_function_error_message in str(exception_info.value)


@pytest.mark.asyncio
async def test_async_call_undeployed_contract(
    async_undeployed_math_contract, async_call
):
    expected_undeployed_call_error_message = (
        "Could not transact with/call contract function"
    )
    with pytest.raises(BadFunctionCallOutput) as exception_info:
        await async_call(
            contract=async_undeployed_math_contract, contract_function="return13"
        )
    assert expected_undeployed_call_error_message in str(exception_info.value)


@pytest.mark.asyncio
async def test_async_call_fallback_function(async_fallback_function_contract):
    result = await async_fallback_function_contract.fallback.call()
    assert result == []


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "tx_params,contract_name,expected",
    (
        ({"gas": 210000}, "no_receive", "fallback"),
        ({"gas": 210000, "value": 2}, "no_receive", ""),
        ({"value": 2, "gas": 210000, "data": "0x477a5c98"}, "no_receive", ""),
        ({"gas": 210000, "data": "0x477a5c98"}, "no_receive", "fallback"),
        ({"data": "0x477a5c98"}, "receive", "fallback"),
        ({"value": 2}, "receive", "receive"),
    ),
)
async def test_async_call_receive_fallback_function(
    async_w3,
    tx_params,
    expected,
    async_call,
    async_receive_function_contract,
    async_no_receive_function_contract,
    contract_name,
):
    if contract_name == "receive":
        contract = async_receive_function_contract
    elif contract_name == "no_receive":
        contract = async_no_receive_function_contract
    else:
        raise AssertionError("contract must be either receive or no_receive")

    initial_value = await async_call(contract=contract, contract_function="getText")
    assert initial_value == ""
    to = {"to": contract.address}
    merged = {**to, **tx_params}
    await async_w3.eth.send_transaction(merged)
    final_value = await async_call(contract=contract, contract_function="getText")
    assert final_value == expected


@pytest.mark.asyncio
async def test_async_call_nonexistent_receive_function(
    async_fallback_function_contract,
):
    with pytest.raises(FallbackNotFound, match="No receive function was found"):
        await async_fallback_function_contract.receive.call()


@pytest.mark.asyncio
async def test_async_throws_error_if_block_out_of_range(async_w3, async_math_contract):
    await async_w3.provider.make_request(method="evm_mine", params=[20])
    with pytest.raises(BlockNumberOutofRange):
        await async_math_contract.functions.counter().call(block_identifier=-50)


@pytest.mark.asyncio
async def test_async_accepts_latest_block(async_w3, async_math_contract):
    await async_w3.provider.make_request(method="evm_mine", params=[5])
    await async_math_contract.functions.increment().transact()

    late = await async_math_contract.functions.counter().call(block_identifier="latest")
    pend = await async_math_contract.functions.counter().call(
        block_identifier="pending"
    )

    assert late == 1
    assert pend == 1


@pytest.mark.asyncio
async def test_async_accepts_block_hash_as_identifier(async_w3, async_math_contract):
    blocks = await async_w3.provider.make_request(method="evm_mine", params=[5])
    await async_math_contract.functions.increment().transact()
    more_blocks = await async_w3.provider.make_request(method="evm_mine", params=[5])

    old = await async_math_contract.functions.counter().call(
        block_identifier=blocks["result"][2]
    )
    new = await async_math_contract.functions.counter().call(
        block_identifier=more_blocks["result"][2]
    )  # noqa: E501

    assert old == 0
    assert new == 1


@pytest.mark.asyncio
async def test_async_neg_block_indexes_from_the_end(async_w3, async_math_contract):
    await async_w3.provider.make_request(method="evm_mine", params=[5])
    await async_math_contract.functions.increment().transact()
    await async_math_contract.functions.increment().transact()
    await async_w3.provider.make_request(method="evm_mine", params=[5])

    output1 = await async_math_contract.functions.counter().call(block_identifier=-7)
    output2 = await async_math_contract.functions.counter().call(block_identifier=-6)

    assert output1 == 1
    assert output2 == 2


@pytest.mark.asyncio
async def test_async_no_functions_match_identifier(async_arrays_contract):
    with pytest.raises(MismatchedABI):
        await async_arrays_contract.functions.thisFunctionDoesNotExist().call()


@pytest.mark.asyncio
async def test_async_function_1_match_identifier_wrong_number_of_args(
    async_arrays_contract,
):
    regex = message_regex + diagnosis_arg_regex
    with pytest.raises(ValidationError, match=regex):
        await async_arrays_contract.functions.setBytes32Value().call()


@pytest.mark.asyncio
async def test_async_function_1_match_identifier_wrong_args_encoding(
    async_arrays_contract,
):
    regex = message_regex + diagnosis_encoding_regex
    with pytest.raises(ValidationError, match=regex):
        await async_arrays_contract.functions.setBytes32Value("dog").call()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "arg1,arg2,diagnosis",
    (
        (100, "dog", diagnosis_arg_regex),
        ("dog", None, diagnosis_encoding_regex),
        (100, None, diagnosis_ambiguous_encoding),
    ),
)
async def test_async_function_multiple_diagnoses(async_w3, arg1, arg2, diagnosis):
    Contract = async_w3.eth.contract(abi=MULTIPLE_FUNCTIONS)
    regex = message_regex + diagnosis
    with pytest.raises(ValidationError, match=regex):
        if arg2:
            await Contract.functions.a(arg1, arg2).call()
        else:
            await Contract.functions.a(arg1).call()


@pytest.mark.asyncio
async def test_async_function_no_abi(async_w3):
    contract = async_w3.eth.contract()
    with pytest.raises(NoABIFound):
        await contract.functions.thisFunctionDoesNotExist().call()


@pytest.mark.asyncio
async def test_async_call_abi_no_functions(async_w3):
    contract = async_w3.eth.contract(abi=[])
    with pytest.raises(NoABIFunctionsFound):
        await contract.functions.thisFunctionDoesNotExist().call()


@pytest.mark.asyncio
async def test_async_call_not_sending_ether_to_nonpayable_function(
    async_payable_tester_contract, async_call
):
    result = await async_call(
        contract=async_payable_tester_contract, contract_function="doNoValueCall"
    )
    assert result == []


@pytest.mark.asyncio
async def test_async_call_sending_ether_to_nonpayable_function(
    async_payable_tester_contract, async_call
):
    with pytest.raises(ValidationError):
        await async_call(
            contract=async_payable_tester_contract,
            contract_function="doNoValueCall",
            tx_params={"value": 1},
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "function, value",
    (
        # minimum positive unambiguous value (larger than fixed8x1)
        ("reflect", Decimal("12.8")),
        # maximum value (for ufixed256x1)
        ("reflect", Decimal(2**256 - 1) / 10),
        # maximum negative unambiguous value (less than 0 from ufixed*)
        ("reflect", Decimal("-0.1")),
        # minimum value (for fixed8x1)
        ("reflect", Decimal("-12.8")),
        # only ufixed256x80 type supports 2-80 decimals
        ("reflect", Decimal(2**256 - 1) / 10**80),  # maximum allowed value
        ("reflect", Decimal(1) / 10**80),  # smallest non-zero value
        # minimum value (for ufixed8x1)
        ("reflect_short_u", 0),
        # maximum value (for ufixed8x1)
        ("reflect_short_u", Decimal("25.5")),
    ),
)
async def test_async_reflect_fixed_value(
    async_fixed_reflection_contract, function, value
):
    contract_func = async_fixed_reflection_contract.functions[function]
    reflected = await contract_func(value).call({"gas": 420000})
    assert reflected == value


DEFAULT_DECIMALS = getcontext().prec


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "function, value, error",
    (
        # out of range
        ("reflect_short_u", Decimal("25.6"), "no matching argument types"),
        ("reflect_short_u", Decimal("-.1"), "no matching argument types"),
        # too many digits for *x1, too large for 256x80
        ("reflect", Decimal("0.01"), "no matching argument types"),
        # too many digits
        ("reflect_short_u", Decimal("0.01"), "no matching argument types"),
        (
            "reflect_short_u",
            Decimal(f"1e-{DEFAULT_DECIMALS + 1}"),
            "no matching argument types",
        ),
        (
            "reflect_short_u",
            Decimal("25.4" + "9" * DEFAULT_DECIMALS),
            "no matching argument types",
        ),
        ("reflect", Decimal(1) / 10**81, "no matching argument types"),
        # floats not accepted, for floating point error concerns
        ("reflect_short_u", 0.1, "no matching argument types"),
        # ambiguous
        ("reflect", Decimal("12.7"), "Ambiguous argument encoding"),
        ("reflect", Decimal(0), "Ambiguous argument encoding"),
        ("reflect", 0, "Ambiguous argument encoding"),
    ),
)
async def test_async_invalid_fixed_value_reflections(
    async_fixed_reflection_contract, function, value, error
):
    contract_func = async_fixed_reflection_contract.functions[function]
    with pytest.raises(ValidationError, match=error):
        await contract_func(value).call({"gas": 420000})


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "method_input, expected",
    (
        (
            {
                "a": 123,
                "b": [1, 2],
                "c": [
                    {
                        "x": 234,
                        "y": [True, False],
                        "z": [
                            "0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                        ],
                    },
                    {
                        "x": 345,
                        "y": [False, False],
                        "z": [
                            "0xefd1FF70c185A1C0b125939815225199079096Ee",
                            "0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e",
                        ],
                    },
                ],
            },
            (
                123,
                [1, 2],
                [
                    (
                        234,
                        [True, False],
                        [
                            "0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                        ],
                    ),
                    (
                        345,
                        [False, False],
                        [
                            "0xefd1FF70c185A1C0b125939815225199079096Ee",
                            "0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e",
                        ],
                    ),
                ],
            ),
        ),
        (
            (
                123,
                [1, 2],
                [
                    (
                        234,
                        [True, False],
                        [
                            "0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                        ],
                    ),
                    (
                        345,
                        [False, False],
                        [
                            "0xefd1FF70c185A1C0b125939815225199079096Ee",
                            "0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e",
                        ],
                    ),
                ],
            ),
            (
                123,
                [1, 2],
                [
                    (
                        234,
                        [True, False],
                        [
                            "0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                            "0xfdF1946A9b40245224488F1a36f4A9ed4844a523",
                        ],
                    ),
                    (
                        345,
                        [False, False],
                        [
                            "0xefd1FF70c185A1C0b125939815225199079096Ee",
                            "0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e",
                        ],
                    ),
                ],
            ),
        ),
    ),
)
async def test_async_call_tuple_contract(async_tuple_contract, method_input, expected):
    result = await async_tuple_contract.functions.method(method_input).call()
    assert result == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "method_input, expected",
    (
        (
            {
                "t": [
                    {
                        "u": [
                            {"x": 1, "y": 2},
                            {"x": 3, "y": 4},
                            {"x": 5, "y": 6},
                        ]
                    },
                    {
                        "u": [
                            {"x": 7, "y": 8},
                            {"x": 9, "y": 10},
                            {"x": 11, "y": 12},
                        ]
                    },
                ]
            },
            (
                [
                    (
                        [
                            (1, 2),
                            (3, 4),
                            (5, 6),
                        ],
                    ),
                    (
                        [
                            (7, 8),
                            (9, 10),
                            (11, 12),
                        ],
                    ),
                ],
            ),
        ),
        (
            (
                [
                    (
                        [
                            (1, 2),
                            (3, 4),
                            (5, 6),
                        ],
                    ),
                    (
                        [
                            (7, 8),
                            (9, 10),
                            (11, 12),
                        ],
                    ),
                ],
            ),
            (
                [
                    (
                        [
                            (1, 2),
                            (3, 4),
                            (5, 6),
                        ],
                    ),
                    (
                        [
                            (7, 8),
                            (9, 10),
                            (11, 12),
                        ],
                    ),
                ],
            ),
        ),
    ),
)
async def test_async_call_nested_tuple_contract(
    async_nested_tuple_contract, method_input, expected
):
    result = await async_nested_tuple_contract.functions.method(method_input).call()
    assert result == expected


@pytest.mark.asyncio
async def test_async_call_revert_contract(async_revert_contract):
    with pytest.raises(TransactionFailed, match="Function has been reverted."):
        # eth-tester will do a gas estimation if we don't submit a gas value,
        # which does not contain the revert reason. Avoid that by giving a gas
        # value.
        await async_revert_contract.functions.revertWithMessage().call({"gas": 100000})


@pytest.mark.asyncio
async def test_async_call_with_no_arguments(async_math_contract, call):
    result = await async_math_contract.functions.return13().call()
    assert result == 13


@pytest.mark.asyncio
async def test_async_call_with_one_argument(async_math_contract, call):
    result = await async_math_contract.functions.multiply7(3).call()
    assert result == 21


@pytest.mark.asyncio
async def test_async_returns_data_from_specified_block(async_w3, async_math_contract):
    start_num = await async_w3.eth.get_block("latest")
    await async_w3.provider.make_request(method="evm_mine", params=[5])
    await async_math_contract.functions.increment().transact()
    await async_math_contract.functions.increment().transact()

    output1 = await async_math_contract.functions.counter().call(
        block_identifier=start_num.number + 6
    )
    output2 = await async_math_contract.functions.counter().call(
        block_identifier=start_num.number + 7
    )

    assert output1 == 1
    assert output2 == 2
