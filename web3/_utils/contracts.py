import functools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

from eth_abi.codec import (
    ABICodec,
)
from eth_abi.registry import (
    registry as default_registry,
)
from eth_typing import (
    ABI,
    ABICallable,
    ABIConstructor,
    ABIElement,
    ABIEvent,
    ABIFallback,
    ABIFunction,
    ABIReceive,
    ChecksumAddress,
    HexStr,
    TypeStr,
)
from eth_utils import (
    add_0x_prefix,
    encode_hex,
    filter_abi_by_name,
    filter_abi_by_type,
    get_abi_input_types,
)
from eth_utils.toolz import (
    pipe,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    filter_by_argument_name,
    map_abi_data,
    named_tree,
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
    BlockNumberOutOfRange,
    Web3TypeError,
    Web3ValidationError,
    Web3ValueError,
)
from web3.types import (
    BlockIdentifier,
    BlockNumber,
    FunctionIdentifier,
    TxParams,
)
from web3.utils.abi import (
    check_if_arguments_can_be_encoded,
    get_abi_element,
    get_abi_element_info,
    get_constructor_function_abi,
    get_fallback_function_abi,
    get_receive_function_abi,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )


def find_matching_event_abi(
    abi: ABI,
    event_name: Optional[str] = None,
    argument_names: Optional[Sequence[str]] = None,
) -> ABIEvent:
    filters = [
        functools.partial(filter_abi_by_type, "event"),
    ]

    if event_name is not None:
        filters.append(functools.partial(filter_abi_by_name, event_name))

    if argument_names is not None:
        filters.append(functools.partial(filter_by_argument_name, argument_names))

    event_abi_candidates = pipe(abi, *filters)

    if len(event_abi_candidates) == 1:
        return event_abi_candidates[0]
    elif not event_abi_candidates:
        raise Web3ValueError("No matching events found")
    else:
        raise Web3ValueError("Multiple events found")


def encode_abi(
    w3: Union["AsyncWeb3", "Web3"],
    abi: ABIElement,
    arguments: Sequence[Any],
    data: Optional[HexStr] = None,
) -> HexStr:
    argument_types = []
    try:
        argument_types = get_abi_input_types(abi)
    except ValueError:
        # Use the default argument_types if the abi doesn't have inputs
        pass

    if not check_if_arguments_can_be_encoded(
        abi,
        *arguments,
        abi_codec=w3.codec,
        **{},
    ):
        raise Web3TypeError(
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


def prepare_transaction(
    address: ChecksumAddress,
    w3: Union["AsyncWeb3", "Web3"],
    fn_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]],
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIElement] = None,
    transaction: Optional[TxParams] = None,
    fn_args: Optional[Sequence[Any]] = None,
    fn_kwargs: Optional[Any] = None,
) -> TxParams:
    """
    Returns a dictionary of the transaction that could be used to call this
    TODO: make this a public API
    TODO: add new prepare_deploy_transaction API
    """
    fn_args = fn_args or []
    fn_kwargs = fn_kwargs or {}
    if fn_abi is None:
        fn_abi = get_abi_element(
            contract_abi, fn_identifier, *fn_args, abi_codec=w3.codec, **fn_kwargs
        )

    if fn_abi["type"] == "error" or fn_abi["type"] == "event":
        raise Web3ValidationError(
            f"Cannot make a transaction with an `{fn_abi['type']}` ABI."
        )

    validate_payable(transaction, fn_abi)

    if transaction is None:
        prepared_transaction: TxParams = {}
    else:
        prepared_transaction = cast(TxParams, dict(**transaction))

    if "data" in prepared_transaction:
        raise Web3ValueError("Transaction parameter may not contain a 'data' key")

    if address:
        prepared_transaction.setdefault("to", address)

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
    fn_identifier: FunctionIdentifier,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABICallable] = None,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
) -> HexStr:
    info_abi: ABIElement
    if fn_identifier is FallbackFn:
        info_abi, info_selector, info_arguments = get_fallback_function_info(
            contract_abi, cast(ABIFallback, fn_abi)
        )
    elif fn_identifier is ReceiveFn:
        info_abi, info_selector, info_arguments = get_receive_function_info(
            contract_abi, cast(ABIReceive, fn_abi)
        )
    elif isinstance(fn_identifier, str):
        fn_info = get_abi_element_info(
            contract_abi,
            fn_identifier,
            *args,
            abi_codec=w3.codec,
            **kwargs,
        )
        info_abi = fn_info["abi"]
        info_selector = fn_info["selector"]
        info_arguments = fn_info["arguments"]
    else:
        raise Web3TypeError("Unsupported function identifier")

    return add_0x_prefix(encode_abi(w3, info_abi, info_arguments, info_selector))


def decode_transaction_data(
    fn_abi: ABIFunction,
    data: HexStr,
    normalizers: Sequence[Callable[[TypeStr, Any], Tuple[TypeStr, Any]]] = None,
) -> Dict[str, Any]:
    data_bytes = HexBytes(data)
    types = get_abi_input_types(fn_abi)
    abi_codec = ABICodec(default_registry)
    decoded = abi_codec.decode(types, data_bytes[4:])
    if normalizers:
        decoded = map_abi_data(normalizers, types, decoded)
    return named_tree(fn_abi["inputs"], decoded)


def get_constructor_function_info(
    contract_abi: Optional[ABI] = None, fn_abi: Optional[ABIConstructor] = None
) -> Tuple[ABIConstructor, HexStr, Tuple[Any, ...]]:
    if fn_abi is None:
        fn_abi = get_constructor_function_abi(contract_abi)
    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()
    return fn_abi, fn_selector, fn_arguments


def get_fallback_function_info(
    contract_abi: Optional[ABI] = None, fn_abi: Optional[ABIFallback] = None
) -> Tuple[ABIFallback, HexStr, Tuple[Any, ...]]:
    if fn_abi is None:
        fn_abi = get_fallback_function_abi(contract_abi)
    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()
    return fn_abi, fn_selector, fn_arguments


def get_receive_function_info(
    contract_abi: Optional[ABI] = None, fn_abi: Optional[ABIReceive] = None
) -> Tuple[ABIReceive, HexStr, Tuple[Any, ...]]:
    if fn_abi is None:
        fn_abi = get_receive_function_abi(contract_abi)
    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()
    return fn_abi, fn_selector, fn_arguments


def validate_payable(transaction: TxParams, abi_element: ABICallable) -> None:
    """
    Raise Web3ValidationError if non-zero ether
    is sent to a non-payable function.
    """
    if (
        "value" in transaction
        and to_integer_if_hex(transaction["value"]) != 0
        and (
            "payable" in abi_element
            and not abi_element["payable"]
            or "stateMutability" in abi_element
            and abi_element["stateMutability"] == "nonpayable"
        )
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
        raise BlockNumberOutOfRange


def parse_block_identifier_int(w3: "Web3", block_identifier_int: int) -> BlockNumber:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = w3.eth.get_block("latest")["number"]
        block_num = last_block + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutOfRange
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
        raise BlockNumberOutOfRange


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
            raise BlockNumberOutOfRange
    return BlockNumber(block_num)
