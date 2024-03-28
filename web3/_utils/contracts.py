from typing import (
    TYPE_CHECKING,
    Any,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

from eth_typing import (
    ChecksumAddress,
    HexStr,
)
from eth_utils import (
    add_0x_prefix,
    encode_hex,
    is_text,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    check_if_arguments_can_be_encoded,
    get_abi_input_types,
    get_fallback_func_abi,
    get_receive_func_abi,
    map_abi_data,
)
from web3._utils.blocks import (
    is_hex_encoded_block_hash,
)
from web3._utils.encoding import (
    to_hex,
)
from web3._utils.function_identifiers import (
    FallbackFn,
    ReceiveFn,
)
from web3._utils.method_formatters import (
    to_integer_if_hex,
)
from web3._utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_bytes,
    abi_ens_resolver,
    abi_string_to_text,
)
from web3.exceptions import (
    BlockNumberOutofRange,
    Web3ValidationError,
)
from web3.types import (
    ABI,
    ABIFunction,
    ABIFunctionInfo,
    BlockIdentifier,
    BlockNumber,
    TxParams,
)
from web3.utils.abi import (
    get_function_abi,
    get_function_info,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )


def encode_abi(
    w3: Union["AsyncWeb3", "Web3"],
    abi: ABIFunction,
    arguments: Sequence[Any],
    data: Optional[HexStr] = None,
) -> HexStr:
    argument_types = get_abi_input_types(abi)

    if not check_if_arguments_can_be_encoded(abi, w3.codec, arguments, {}):
        raise TypeError(
            "One or more arguments could not be encoded to the necessary "
            f"ABI type. Expected types are: {', '.join(argument_types)}"
        )

    normalizers = [
        abi_address_to_hex,
        abi_bytes_to_bytes,
        abi_string_to_text,
    ]
    if not w3.eth.is_async:
        normalizers.append(abi_ens_resolver(w3))

    normalized_arguments = map_abi_data(
        normalizers,
        argument_types,
        arguments,
    )
    encoded_arguments = w3.codec.encode(
        argument_types,
        normalized_arguments,
    )
    if data:
        return to_hex(HexBytes(data) + encoded_arguments)
    else:
        return encode_hex(encoded_arguments)


def build_transaction(
    address: ChecksumAddress, transaction: Optional[TxParams] = None
) -> TxParams:
    if transaction is None:
        built_transaction: TxParams = {}
    else:
        built_transaction = cast(TxParams, dict(**transaction))

    if "data" in built_transaction:
        raise ValueError("Cannot set 'data' field in build transaction")

    if not address and "to" not in built_transaction:
        raise ValueError(
            "When using `ContractFunction.build_transaction` from a contract "
            "factory you must provide a `to` address with the transaction"
        )
    if address and "to" in built_transaction:
        raise ValueError("Cannot set 'to' field in contract call build transaction")

    if address:
        built_transaction.setdefault("to", address)

    if "to" not in built_transaction:
        raise ValueError("Please ensure that this contract instance has an address.")

    return built_transaction


def prepare_transaction(
    address: ChecksumAddress,
    w3: Union["AsyncWeb3", "Web3"],
    fn_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]],
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    transaction: Optional[TxParams] = None,
    fn_args: Optional[Sequence[Any]] = None,
    fn_kwargs: Optional[Any] = None,
) -> TxParams:
    """
    Returns a dictionary of transaction parameters
    TODO: make this a public API
    TODO: add new prepare_deploy_transaction API
    """
    if fn_abi is None:
        fn_abi = get_function_abi(contract_abi, fn_identifier, fn_args, fn_kwargs)

    validate_payable(transaction, fn_abi)

    prepared_transaction = build_transaction(address, transaction)

    prepared_transaction["data"] = encode_transaction_data(
        w3,
        fn_identifier,
        contract_abi,
        fn_abi,
        fn_args,
        fn_kwargs,
    )
    return prepared_transaction


def encode_transaction_data(
    w3: Union["AsyncWeb3", "Web3"],
    fn_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]],
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
) -> HexStr:
    if fn_identifier is FallbackFn:
        fn_info = get_fallback_function_info(contract_abi, fn_abi)
    elif fn_identifier is ReceiveFn:
        fn_info = get_receive_function_info(contract_abi, fn_abi)
    elif is_text(fn_identifier):
        fn_info = get_function_info(
            contract_abi,
            fn_identifier,
            args,
            kwargs,
        )
    else:
        raise TypeError("Unsupported function identifier")

    return add_0x_prefix(
        encode_abi(w3, fn_info["abi"], fn_info["arguments"], fn_info["selector"])
    )


def get_fallback_function_info(
    abi: Optional[ABI] = None, fn_abi: Optional[ABIFunction] = None
) -> ABIFunctionInfo:
    if fn_abi is None:
        fn_abi = get_fallback_func_abi(abi)

    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()

    return ABIFunctionInfo(abi=fn_abi, selector=fn_selector, arguments=fn_arguments)


def get_receive_function_info(
    abi: Optional[ABI] = None, fn_abi: Optional[ABIFunction] = None
) -> ABIFunctionInfo:
    if fn_abi is None:
        fn_abi = get_receive_func_abi(abi)

    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()

    return ABIFunctionInfo(abi=fn_abi, selector=fn_selector, arguments=fn_arguments)


def validate_payable(transaction: TxParams, abi: ABIFunction) -> None:
    """Raise Web3ValidationError if non-zero ether
    is sent to a non-payable function.
    """
    if "value" in transaction:
        if to_integer_if_hex(transaction["value"]) != 0:
            if (
                "payable" in abi
                and not abi["payable"]
                or "stateMutability" in abi
                and abi["stateMutability"] == "nonpayable"
            ):
                raise Web3ValidationError(
                    "Sending non-zero ether to a contract function "
                    "with payable=False. Please ensure that "
                    "transaction's value is 0."
                )


def parse_block_identifier(
    w3: "Web3", block_identifier: BlockIdentifier
) -> BlockIdentifier:
    if block_identifier is None:
        return w3.eth.default_block
    if isinstance(block_identifier, int):
        return parse_block_identifier_int(w3, block_identifier)
    elif block_identifier in ["latest", "earliest", "pending", "safe", "finalized"]:
        return block_identifier
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(
        block_identifier
    ):
        return w3.eth.get_block(block_identifier)["number"]
    else:
        raise BlockNumberOutofRange


def parse_block_identifier_int(w3: "Web3", block_identifier_int: int) -> BlockNumber:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = w3.eth.get_block("latest")["number"]
        block_num = last_block + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutofRange
    return BlockNumber(block_num)


async def async_parse_block_identifier(
    async_w3: "AsyncWeb3", block_identifier: BlockIdentifier
) -> BlockIdentifier:
    if block_identifier is None:
        return async_w3.eth.default_block
    if isinstance(block_identifier, int):
        return await async_parse_block_identifier_int(async_w3, block_identifier)
    elif block_identifier in ["latest", "earliest", "pending", "safe", "finalized"]:
        return block_identifier
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(
        block_identifier
    ):
        requested_block = await async_w3.eth.get_block(block_identifier)
        return requested_block["number"]
    else:
        raise BlockNumberOutofRange


async def async_parse_block_identifier_int(
    async_w3: "AsyncWeb3", block_identifier_int: int
) -> BlockNumber:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = await async_w3.eth.get_block("latest")
        last_block_num = last_block["number"]
        block_num = last_block_num + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutofRange
    return BlockNumber(block_num)
