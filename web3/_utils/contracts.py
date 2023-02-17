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
    ChecksumAddress,
    HexStr,
    TypeStr,
)
from eth_utils import (
    add_0x_prefix,
    encode_hex,
    function_abi_to_4byte_selector,
    is_binary_address,
    is_checksum_address,
    is_list_like,
    is_text,
)
from eth_utils.toolz import (
    pipe,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    abi_to_signature,
    check_if_arguments_can_be_encoded,
    filter_by_argument_count,
    filter_by_argument_name,
    filter_by_encodability,
    filter_by_name,
    filter_by_type,
    get_abi_input_types,
    get_aligned_abi_inputs,
    get_fallback_func_abi,
    get_receive_func_abi,
    map_abi_data,
    merge_args_and_kwargs,
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
    BlockNumberOutofRange,
    Web3ValidationError,
)
from web3.types import (
    ABI,
    ABIEvent,
    ABIFunction,
    BlockIdentifier,
    BlockNumber,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )


def extract_argument_types(*args: Sequence[Any]) -> str:
    """
    Takes a list of arguments and returns a string representation of the argument types,
    appropriately collapsing `tuple` types into the respective nested types.
    """
    collapsed_args = []

    for arg in args:
        if is_list_like(arg):
            collapsed_nested = []
            for nested in arg:
                if is_list_like(nested):
                    collapsed_nested.append(f"({extract_argument_types(nested)})")
                else:
                    collapsed_nested.append(_get_argument_readable_type(nested))
            collapsed_args.append(",".join(collapsed_nested))
        else:
            collapsed_args.append(_get_argument_readable_type(arg))

    return ",".join(collapsed_args)


def find_matching_event_abi(
    abi: ABI,
    event_name: Optional[str] = None,
    argument_names: Optional[Sequence[str]] = None,
) -> ABIEvent:
    filters = [
        functools.partial(filter_by_type, "event"),
    ]

    if event_name is not None:
        filters.append(functools.partial(filter_by_name, event_name))

    if argument_names is not None:
        filters.append(functools.partial(filter_by_argument_name, argument_names))

    event_abi_candidates = pipe(abi, *filters)

    if len(event_abi_candidates) == 1:
        return event_abi_candidates[0]
    elif not event_abi_candidates:
        raise ValueError("No matching events found")
    else:
        raise ValueError("Multiple events found")


def find_matching_fn_abi(
    abi: ABI,
    abi_codec: ABICodec,
    fn_identifier: Optional[Union[str, Type[FallbackFn], Type[ReceiveFn]]] = None,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
) -> ABIFunction:
    args = args or tuple()
    kwargs = kwargs or dict()
    num_arguments = len(args) + len(kwargs)

    if fn_identifier is FallbackFn:
        return get_fallback_func_abi(abi)

    if fn_identifier is ReceiveFn:
        return get_receive_func_abi(abi)

    if not is_text(fn_identifier):
        raise TypeError("Unsupported function identifier")

    name_filter = functools.partial(filter_by_name, fn_identifier)
    arg_count_filter = functools.partial(filter_by_argument_count, num_arguments)
    encoding_filter = functools.partial(filter_by_encodability, abi_codec, args, kwargs)

    function_candidates = pipe(abi, name_filter, arg_count_filter, encoding_filter)

    if len(function_candidates) == 1:
        return function_candidates[0]
    else:
        matching_identifiers = name_filter(abi)
        matching_function_signatures = [
            abi_to_signature(func) for func in matching_identifiers
        ]

        arg_count_matches = len(arg_count_filter(matching_identifiers))
        encoding_matches = len(encoding_filter(matching_identifiers))

        if arg_count_matches == 0:
            diagnosis = (
                "\nFunction invocation failed due to improper number of arguments."
            )
        elif encoding_matches == 0:
            diagnosis = (
                "\nFunction invocation failed due to no matching argument types."
            )
        elif encoding_matches > 1:
            diagnosis = (
                "\nAmbiguous argument encoding. "
                "Provided arguments can be encoded to multiple functions "
                "matching this call."
            )

        collapsed_args = extract_argument_types(args)
        collapsed_kwargs = dict(
            {(k, extract_argument_types([v])) for k, v in kwargs.items()}
        )
        message = (
            f"\nCould not identify the intended function with name `{fn_identifier}`, "
            f"positional arguments with type(s) `{collapsed_args}` and "
            f"keyword arguments with type(s) `{collapsed_kwargs}`."
            f"\nFound {len(matching_identifiers)} function(s) with "
            f"the name `{fn_identifier}`: {matching_function_signatures}{diagnosis}"
        )

        raise Web3ValidationError(message)


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
    :parameter `is_function_abi` is used to distinguish  function abi from contract abi
    Returns a dictionary of the transaction that could be used to call this
    TODO: make this a public API
    TODO: add new prepare_deploy_transaction API
    """
    if fn_abi is None:
        fn_abi = find_matching_fn_abi(
            contract_abi, w3.codec, fn_identifier, fn_args, fn_kwargs
        )

    validate_payable(transaction, fn_abi)

    if transaction is None:
        prepared_transaction: TxParams = {}
    else:
        prepared_transaction = cast(TxParams, dict(**transaction))

    if "data" in prepared_transaction:
        raise ValueError("Transaction parameter may not contain a 'data' key")

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
    fn_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]],
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
) -> HexStr:
    if fn_identifier is FallbackFn:
        fn_abi, fn_selector, fn_arguments = get_fallback_function_info(
            contract_abi, fn_abi
        )
    elif fn_identifier is ReceiveFn:
        fn_abi, fn_selector, fn_arguments = get_receive_function_info(
            contract_abi, fn_abi
        )
    elif is_text(fn_identifier):
        fn_abi, fn_selector, fn_arguments = get_function_info(
            # type ignored b/c fn_id here is always str b/c FallbackFn is handled above
            fn_identifier,  # type: ignore
            w3.codec,
            contract_abi,
            fn_abi,
            args,
            kwargs,
        )
    else:
        raise TypeError("Unsupported function identifier")

    return add_0x_prefix(encode_abi(w3, fn_abi, fn_arguments, fn_selector))


def decode_transaction_data(
    fn_abi: ABIFunction,
    data: HexStr,
    normalizers: Sequence[Callable[[TypeStr, Any], Tuple[TypeStr, Any]]] = None,
) -> Dict[str, Any]:
    # type ignored b/c expects data arg to be HexBytes
    data = HexBytes(data)  # type: ignore
    types = get_abi_input_types(fn_abi)
    abi_codec = ABICodec(default_registry)
    decoded = abi_codec.decode(types, HexBytes(data[4:]))
    if normalizers:
        decoded = map_abi_data(normalizers, types, decoded)
    return named_tree(fn_abi["inputs"], decoded)


def get_fallback_function_info(
    contract_abi: Optional[ABI] = None, fn_abi: Optional[ABIFunction] = None
) -> Tuple[ABIFunction, HexStr, Tuple[Any, ...]]:
    if fn_abi is None:
        fn_abi = get_fallback_func_abi(contract_abi)
    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()
    return fn_abi, fn_selector, fn_arguments


def get_receive_function_info(
    contract_abi: Optional[ABI] = None, fn_abi: Optional[ABIFunction] = None
) -> Tuple[ABIFunction, HexStr, Tuple[Any, ...]]:
    if fn_abi is None:
        fn_abi = get_receive_func_abi(contract_abi)
    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()
    return fn_abi, fn_selector, fn_arguments


def get_function_info(
    fn_name: str,
    abi_codec: ABICodec,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
) -> Tuple[ABIFunction, HexStr, Tuple[Any, ...]]:
    if args is None:
        args = tuple()
    if kwargs is None:
        kwargs = {}

    if fn_abi is None:
        fn_abi = find_matching_fn_abi(contract_abi, abi_codec, fn_name, args, kwargs)

    # typed dict cannot be used w/ a normal Dict
    # https://github.com/python/mypy/issues/4976
    fn_selector = encode_hex(function_abi_to_4byte_selector(fn_abi))  # type: ignore

    fn_arguments = merge_args_and_kwargs(fn_abi, args, kwargs)

    _, aligned_fn_arguments = get_aligned_abi_inputs(fn_abi, fn_arguments)

    return fn_abi, fn_selector, aligned_fn_arguments


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


def _get_argument_readable_type(arg: Any) -> str:
    if is_checksum_address(arg) or is_binary_address(arg):
        return "address"

    return arg.__class__.__name__


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


def parse_block_identifier_no_extra_call(
    w3: Union["Web3", "AsyncWeb3"], block_identifier: BlockIdentifier
) -> BlockIdentifier:
    if block_identifier is None:
        return w3.eth.default_block
    elif isinstance(block_identifier, int) and block_identifier >= 0:
        return block_identifier
    elif block_identifier in ["latest", "earliest", "pending", "safe", "finalized"]:
        return block_identifier
    elif isinstance(block_identifier, bytes):
        return HexBytes(block_identifier)
    elif is_hex_encoded_block_hash(block_identifier):
        return HexStr(str(block_identifier))
    else:
        raise BlockNumberOutofRange


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
