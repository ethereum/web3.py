import pytest

from web3.exceptions import (
    BlockNumberOutOfRange,
    MismatchedABI,
    NoABIFound,
    NoABIFunctionsFound,
)


@pytest.fixture()
def address(w3):
    return w3.eth.accounts[1]


@pytest.fixture()
def transaction_dict(w3, address):
    return {
        "from": address,
        "gas": 210000,
        "maxFeePerGas": w3.to_wei(1, "gwei"),
        "maxPriorityFeePerGas": w3.to_wei(1, "gwei"),
        "value": 12345,
    }


decode_tuples_args = (
    "method_input, tuple_output, type_str, namedtuple_repr",
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
            "<class 'web3._utils.abi.abi_decoded_namedtuple_factory.<locals>.ABIDecodedNamedTuple'>",  # noqa: E501
            "ABIDecodedNamedTuple(a=123, b=[1, 2], c=[ABIDecodedNamedTuple(x=234, y=[True, False], z=['0x4AD7E79d88650B01EEA2B1f069f01EE9db343d5c', '0xfdF1946A9b40245224488F1a36f4A9ed4844a523', '0xfdF1946A9b40245224488F1a36f4A9ed4844a523']), ABIDecodedNamedTuple(x=345, y=[False, False], z=['0xefd1FF70c185A1C0b125939815225199079096Ee', '0xf35C0784794F3Cd935F5754d3a0EbcE95bEf851e'])])",  # noqa: E501
        ),
    ),
)


def test_caller_default(math_contract):
    result = math_contract.caller.add(3, 5)
    assert result == 8


def test_caller_with_parens(math_contract):
    result = math_contract.caller().add(3, 5)
    assert result == 8


def test_caller_with_no_abi(w3):
    contract = w3.eth.contract()
    with pytest.raises(NoABIFound):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_with_no_abi_and_parens(w3):
    contract = w3.eth.contract()
    with pytest.raises(NoABIFound):
        contract.caller().thisFunctionDoesNotExist()


def test_caller_with_empty_abi_and_parens(w3):
    contract = w3.eth.contract(abi=[])
    with pytest.raises(NoABIFunctionsFound):
        contract.caller().thisFunctionDoesNotExist()


def test_caller_with_empty_abi(w3):
    contract = w3.eth.contract(abi=[])
    with pytest.raises(NoABIFunctionsFound):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_raw_getattr_with_missing_element(math_contract):
    with pytest.raises(MismatchedABI, match="not found in this contract's ABI"):
        math_contract.caller.__getattr__("notafunction")


def test_caller_raw_getattr_with_present_element(math_contract):
    attr = math_contract.caller.__getattr__("return13")
    assert attr


def test_caller_with_a_nonexistent_function(math_contract):
    contract = math_contract
    with pytest.raises(MismatchedABI, match="not found in this contract's ABI"):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_with_invalid_block_identifier(w3, math_contract):
    w3.provider.make_request(method="evm_mine", params=[5])
    math_contract.functions.incrementCounter().transact()
    math_contract.functions.incrementCounter().transact()

    # Invalid `block_identifier` should not raise when passed to `caller` directly.
    # The function call itself parses the value.
    caller = math_contract.caller(block_identifier="abc")
    with pytest.raises(BlockNumberOutOfRange):
        caller.counter()

    # Calling the function with an invalid `block_identifier` will raise.
    default_caller = math_contract.caller()
    with pytest.raises(BlockNumberOutOfRange):
        default_caller.counter(block_identifier="abc")


def test_caller_with_block_identifier(w3, math_contract):
    start = w3.eth.get_block("latest")
    start_num = start.number
    block_hash = start.hash
    block_hex = w3.to_hex(block_hash)

    assert math_contract.caller.counter() == 0

    w3.provider.make_request(method="evm_mine", params=[5])
    math_contract.functions.incrementCounter().transact()
    math_contract.functions.incrementCounter().transact()

    assert_ids = [
        (block_hash, 0),
        (block_hex, 0),
        (start_num, 0),
        (start_num + 6, 1),
        (start_num + 7, 2),
        ("latest", 2),
        (None, 2),
    ]

    for block_identifier, expected_value in assert_ids:
        assert (
            math_contract.caller(block_identifier=block_identifier).counter()
            == expected_value
        )

        # Function arg `block_identifier` produces same result
        assert (
            math_contract.caller().counter(block_identifier=block_identifier)
            == expected_value
        )


def test_caller_with_block_identifier_and_transaction_dict(
    w3, contract_caller_tester_contract, transaction_dict, address
):
    start_num = w3.eth.get_block("latest").number
    assert contract_caller_tester_contract.caller.counter() == 0

    w3.provider.make_request(method="evm_mine", params=[5])
    contract_caller_tester_contract.functions.increment().transact()

    block_id = start_num + 6
    contract = contract_caller_tester_contract.caller(
        transaction=transaction_dict, block_identifier=block_id
    )

    sender, _, gasLeft, value, block_num = contract.returnMeta()
    counter = contract.counter()

    assert sender == address
    assert gasLeft <= transaction_dict["gas"]
    assert value == transaction_dict["value"]
    assert block_num == block_id
    assert counter == 1


def test_caller_with_transaction_keyword(
    w3, contract_caller_tester_contract, transaction_dict, address
):
    contract = contract_caller_tester_contract.caller(transaction=transaction_dict)

    sender, _, gasLeft, value, _ = contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict["gas"]
    assert value == transaction_dict["value"]


def test_caller_with_dict_but_no_transaction_keyword(
    w3, contract_caller_tester_contract, transaction_dict, address
):
    contract = contract_caller_tester_contract.caller(transaction_dict)

    sender, _, gasLeft, value, _ = contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict["gas"]
    assert value == transaction_dict["value"]


def test_caller_with_args_and_no_transaction_keyword(
    w3, contract_caller_tester_contract, transaction_dict, address
):
    contract = contract_caller_tester_contract.caller(transaction_dict)

    sender, _, gasLeft, value, _ = contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict["gas"]
    assert value == transaction_dict["value"]

    add_result = contract.add(3, 5)
    assert add_result == 8


@pytest.mark.parametrize(*decode_tuples_args)
def test_tuple_contract_caller_default_with_decode_tuples(
    tuple_contract_with_decode_tuples,
    method_input,
    tuple_output,
    type_str,
    namedtuple_repr,
):
    result = tuple_contract_with_decode_tuples.caller.method(method_input)
    assert result == tuple_output
    assert str(type(result)) == type_str
    assert result.__repr__() == namedtuple_repr


@pytest.mark.parametrize(*decode_tuples_args)
def test_tuple_contract_caller_with_parens_with_decode_tuples(
    tuple_contract_with_decode_tuples,
    method_input,
    tuple_output,
    type_str,
    namedtuple_repr,
):
    result = tuple_contract_with_decode_tuples.caller().method(method_input)
    assert result == tuple_output
    assert str(type(result)) == type_str
    assert result.__repr__() == namedtuple_repr


# --- async --- #


@pytest.mark.asyncio
async def test_async_caller_default(async_math_contract):
    result = await async_math_contract.caller.add(3, 5)
    assert result == 8


@pytest.mark.asyncio
async def test_async_caller_with_parens(async_math_contract):
    result = await async_math_contract.caller().add(3, 5)
    assert result == 8


@pytest.mark.asyncio
async def test_async_caller_with_no_abi(async_w3):
    contract = async_w3.eth.contract()
    with pytest.raises(NoABIFound):
        await contract.caller.thisFunctionDoesNotExist()


@pytest.mark.asyncio
async def test_async_caller_with_no_abi_and_parens(async_w3):
    contract = async_w3.eth.contract()
    with pytest.raises(NoABIFound):
        await contract.caller().thisFunctionDoesNotExist()


@pytest.mark.asyncio
async def test_async_caller_with_empty_abi_and_parens(async_w3):
    contract = async_w3.eth.contract(abi=[])
    with pytest.raises(NoABIFunctionsFound):
        await contract.caller().thisFunctionDoesNotExist()


@pytest.mark.asyncio
async def test_async_caller_with_empty_abi(async_w3):
    contract = async_w3.eth.contract(abi=[])
    with pytest.raises(NoABIFunctionsFound):
        await contract.caller.thisFunctionDoesNotExist()


@pytest.mark.asyncio
async def test_async_caller_raw_getattr_with_missing_element(async_math_contract):
    with pytest.raises(MismatchedABI, match="not found in this contract's ABI"):
        await async_math_contract.caller.__getattr__("notafunction")


@pytest.mark.asyncio
async def test_async_caller_raw_getattr_with_present_element(async_math_contract):
    attr = async_math_contract.caller.__getattr__("return13")
    assert attr


@pytest.mark.asyncio
async def test_async_caller_with_a_nonexistent_function(async_math_contract):
    contract = async_math_contract
    with pytest.raises(MismatchedABI, match="not found in this contract's ABI"):
        await contract.caller.thisFunctionDoesNotExist()


@pytest.mark.asyncio
async def test_async_caller_with_invalid_block_identifier(
    async_w3, async_math_contract
):
    await async_w3.provider.make_request(method="evm_mine", params=[5])
    await async_math_contract.functions.incrementCounter().transact()
    await async_math_contract.functions.incrementCounter().transact()

    # Invalid `block_identifier` should not raise when passed to `caller` directly.
    # The function call itself parses the value.
    caller = async_math_contract.caller(block_identifier="abc")
    with pytest.raises(BlockNumberOutOfRange):
        await caller.counter()

    # Calling the function with an invalid `block_identifier` will raise.
    default_caller = async_math_contract.caller()
    with pytest.raises(BlockNumberOutOfRange):
        await default_caller.counter(block_identifier="abc")


@pytest.mark.asyncio
async def test_async_caller_with_block_identifier(async_w3, async_math_contract):
    start = await async_w3.eth.get_block("latest")
    start_num = start.number
    block_hash = start.hash
    block_hex = async_w3.to_hex(block_hash)

    assert await async_math_contract.caller.counter() == 0

    await async_w3.provider.make_request(method="evm_mine", params=[5])
    await async_math_contract.functions.incrementCounter().transact()
    await async_math_contract.functions.incrementCounter().transact()

    assert_ids = [
        (block_hash, 0),
        (block_hex, 0),
        (start_num, 0),
        (start_num + 6, 1),
        (start_num + 7, 2),
        ("latest", 2),
        (None, 2),
    ]

    for block_identifier, expected_value in assert_ids:
        assert (
            await async_math_contract.caller(
                block_identifier=block_identifier
            ).counter()
            == expected_value
        )

        # Function arg `block_identifier` produces same result
        assert (
            await async_math_contract.caller().counter(
                block_identifier=block_identifier
            )
            == expected_value
        )


@pytest.mark.asyncio
async def test_async_caller_with_block_identifier_and_transaction_dict(
    async_w3, async_contract_caller_tester_contract, transaction_dict, address
):
    start = await async_w3.eth.get_block("latest")
    start_num = start.number
    assert await async_contract_caller_tester_contract.caller.counter() == 0

    await async_w3.provider.make_request(method="evm_mine", params=[5])
    await async_contract_caller_tester_contract.functions.increment().transact()

    block_id = start_num + 6
    contract = async_contract_caller_tester_contract.caller(
        transaction=transaction_dict, block_identifier=block_id
    )

    sender, _, gasLeft, value, block_num = await contract.returnMeta()
    counter = await contract.counter()

    assert sender == address
    assert gasLeft <= transaction_dict["gas"]
    assert value == transaction_dict["value"]
    assert block_num == block_id
    assert counter == 1


@pytest.mark.asyncio
async def test_async_caller_with_transaction_keyword(
    async_w3, async_contract_caller_tester_contract, transaction_dict, address
):
    contract = async_contract_caller_tester_contract.caller(
        transaction=transaction_dict
    )

    sender, _, gasLeft, value, _ = await contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict["gas"]
    assert value == transaction_dict["value"]


@pytest.mark.asyncio
async def test_async_caller_with_dict_but_no_transaction_keyword(
    async_w3, async_contract_caller_tester_contract, transaction_dict, address
):
    contract = async_contract_caller_tester_contract.caller(transaction_dict)

    sender, _, gasLeft, value, _ = await contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict["gas"]
    assert value == transaction_dict["value"]


@pytest.mark.asyncio
async def test_async_caller_with_args_and_no_transaction_keyword(
    async_w3, async_contract_caller_tester_contract, transaction_dict, address
):
    contract = async_contract_caller_tester_contract.caller(transaction_dict)

    sender, _, gasLeft, value, _ = await contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict["gas"]
    assert value == transaction_dict["value"]

    add_result = await contract.add(3, 5)
    assert add_result == 8


@pytest.mark.parametrize(*decode_tuples_args)
@pytest.mark.asyncio
async def test_async_tuple_contract_caller_default_with_decode_tuples(
    async_tuple_contract_with_decode_tuples,
    method_input,
    tuple_output,
    type_str,
    namedtuple_repr,
):
    result = await async_tuple_contract_with_decode_tuples.caller.method(method_input)
    assert result == tuple_output
    assert str(type(result)) == type_str
    assert result.__repr__() == namedtuple_repr


@pytest.mark.parametrize(*decode_tuples_args)
@pytest.mark.asyncio
async def test_async_tuple_contract_caller_with_parens_with_decode_tuples(
    async_tuple_contract_with_decode_tuples,
    method_input,
    tuple_output,
    type_str,
    namedtuple_repr,
):
    result = await async_tuple_contract_with_decode_tuples.caller().method(method_input)
    assert result == tuple_output
    assert str(type(result)) == type_str
    assert result.__repr__() == namedtuple_repr
