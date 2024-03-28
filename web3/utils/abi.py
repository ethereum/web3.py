import functools
import itertools
from typing import (
    Any,
    Callable,
    Dict,
    List,
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
from eth_abi.exceptions import (
    DecodingError,
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
    event_abi_to_log_topic,
    function_abi_to_4byte_selector,
    is_list_like,
    is_string,
    is_text,
    to_hex,
)
from eth_utils.toolz import (
    cons,
    pipe,
)
from hexbytes import (
    HexBytes,
)

from ens import (
    ENS,
)
from web3._utils.abi import (
    abi_to_signature,
    check_if_arguments_can_be_encoded,
    exclude_indexed_event_inputs,
    extract_argument_types,
    filter_by_argument_count,
    filter_by_argument_name,
    filter_by_encodability,
    filter_by_name,
    filter_by_type,
    get_abi_input_names as _get_abi_input_names,
    get_abi_input_types as _get_abi_input_types,
    get_abi_output_names as _get_abi_output_names,
    get_abi_output_types as _get_abi_output_types,
    get_aligned_abi_inputs,
    get_fallback_func_abi,
    get_indexed_event_inputs,
    get_receive_func_abi,
    map_abi_data,
    merge_args_and_kwargs,
    named_tree,
    normalize_event_input_types,
    recursive_dict_to_namedtuple,
)
from web3._utils.contracts import (
    build_transaction,
    get_fallback_function_info,
    get_receive_function_info,
    validate_payable,
)
from web3._utils.events import (
    get_event_abi_types_for_decoding,
    log_entry_data_to_bytes,
    normalize_topic_list,
)
from web3._utils.function_identifiers import (
    FallbackFn,
    ReceiveFn,
)
from web3._utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
    abi_address_to_hex,
    abi_bytes_to_bytes,
    abi_ens_resolver,
    abi_string_to_text,
)
from web3._utils.validation import (
    validate_address,
)
from web3.exceptions import (
    BadFunctionCallOutput,
    InvalidEventABI,
    LogTopicError,
    MismatchedABI,
    Web3ValidationError,
)
from web3.providers.base import (
    BaseProvider,
)
from web3.providers.rpc.rpc import (
    HTTPProvider,
)
from web3.types import (
    ABI,
    ABIElement,
    ABIEvent,
    ABIFunction,
    ABIFunctionInfo,
    BlockIdentifier,
    EventData,
    EventDataArgs,
    FilterParams,
    LogReceipt,
    TxParams,
)


ACCEPTABLE_EMPTY_STRINGS = ["0x", b"0x", "", b""]


def encode_transaction(
    address: ChecksumAddress,
    abi: Optional[ABI] = None,
    function_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]] = None,
    function_args: Optional[Sequence[Any]] = None,
    function_kwargs: Optional[Any] = None,
    transaction: Optional[TxParams] = None,
) -> TxParams:
    """
    Return encoded transaction data without sending a transaction.

    :param address: Checksum address of the contract.
    :param type: `ChecksumAddress`
    :param abi: Contract ABI.
    :param type: `ABI`
    :param function_identifier: Find a function ABI with matching identifier.
    :param type: `str` or `FallbackFn` or `ReceiveFn`
    :kparam function_args: Find a function ABI with matching args.
    :param type: `list[Any]`
    :param function_kwargs: Find a function ABI with matching kwargs.
    :param type: `Any`
    :param transaction: Transaction parameters to be encoded.
    :param type: `TxParams`
    :return: Encoded contract call parameters for a transaction.
    :rtype: `TxParams`
    """
    fn_abi = get_function_abi(abi, function_identifier, function_args, function_kwargs)

    validate_payable(transaction, fn_abi)

    prepared_transaction = build_transaction(address, transaction)

    prepared_transaction["data"] = encode_transaction_data(
        abi,
        function_identifier,
        function_args,
        function_kwargs,
    )
    return prepared_transaction


def encode_transaction_data(
    abi: Optional[ABI],
    function_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]],
    function_args: Optional[Sequence[Any]] = None,
    function_kwargs: Optional[Any] = None,
    is_async: bool = False,
    provider: BaseProvider = None,
    abi_codec: ABICodec = None,
) -> HexStr:
    """
    Return encoded data to be used in a transaction.

    :param abi: Contract ABI.
    :param type: `ABI`
    :param function_identifier: Find a function ABI with matching identifier.
    :param type: `str` or `FallbackFn` or `ReceiveFn`
    :kparam function_args: Find a function ABI with matching args.
    :param type: `list[Any]`
    :param function_kwargs: Find a function ABI with matching kwargs.
    :param type: `Any`
    :param is_async: Enable async transaction encoder.
    :param type: `bool`
    :param provider: Provider instance to configure ENS for syncronous requests.
    :param type: `BaseProvider`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: Encoded data for a transaction.
    :rtype: `HexStr`
    """
    if provider is None:
        provider = HTTPProvider()

    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    fn_abi = get_function_abi(abi, function_identifier, function_args, function_kwargs)

    if function_identifier is FallbackFn:
        fn_info = get_fallback_function_info(abi, fn_abi)
    elif function_identifier is ReceiveFn:
        fn_info = get_receive_function_info(abi, fn_abi)
    elif is_text(function_identifier):
        fn_info = get_function_info(
            abi,
            function_identifier,
            function_args,
            function_kwargs,
        )
    else:
        raise TypeError("Unsupported function identifier")

    return add_0x_prefix(
        encode_abi(
            fn_info["abi"],
            fn_info["selector"],
            fn_info["arguments"],
            is_async,
            provider,
            abi_codec,
        )
    )


def encode_abi(
    function_abi: ABIFunction,
    data: Optional[HexStr] = None,
    arguments: Sequence[Any] = None,
    is_async: bool = False,
    provider: BaseProvider = None,
    abi_codec: ABICodec = None,
) -> HexStr:
    """
    Return encoded data from a function ABI and arguments.

    :param function_abi: Function ABI.
    :param type: `ABIFunction`
    :param data: Data to include in the encoded result.
    :param type: `HexStr`
    :param arguments: Arguments used for the transaction request.
    :param type: `Any`
    :param is_async: Enable async transaction encoder.
    :param type: `bool`
    :param provider: Provider instance to configure ENS for syncronous requests.
    :param type: `BaseProvider`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: Encoded data for a transaction.
    :rtype: `HexStr`
    """
    if provider is None:
        provider = HTTPProvider()

    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    argument_types = get_abi_input_types(function_abi)

    if not check_if_arguments_can_be_encoded(function_abi, abi_codec, arguments, {}):
        raise TypeError(
            "One or more arguments could not be encoded to the necessary "
            f"ABI type. Expected types are: {', '.join(argument_types)}"
        )

    normalizers = [
        abi_address_to_hex,
        abi_bytes_to_bytes,
        abi_string_to_text,
    ]

    if not is_async:
        ens = ENS(provider)
        normalizers.append(abi_ens_resolver(ens=ens))

    normalized_arguments = map_abi_data(
        normalizers,
        argument_types,
        arguments,
    )
    encoded_arguments = abi_codec.encode(
        argument_types,
        normalized_arguments,
    )
    if data:
        return to_hex(HexBytes(data) + encoded_arguments)
    else:
        return encode_hex(encoded_arguments)


def encode_event_filter_params(
    event_abi: ABIEvent,
    contract_address: Optional[ChecksumAddress] = None,
    argument_filters: Optional[Dict[str, Any]] = None,
    topics: Optional[Sequence[HexStr]] = None,
    fromBlock: Optional[BlockIdentifier] = None,
    toBlock: Optional[BlockIdentifier] = None,
    address: Optional[ChecksumAddress] = None,
    abi_codec: ABICodec = None,
) -> Tuple[List[List[Optional[HexStr]]], FilterParams]:
    """
    Return a raw event filter for a JSON-RPC query.

    :param event_abi: Event ABI.
    :param type: `ABIEvent`
    :param contract_address: Checksum address of the contract.
    :param type: `ChecksumAddress`
    :param argument_filters: Arguments for filter topics to be encoded.
    :param type: `dict[str, Any]`
    :param topics: Transaction topics from a `LogReceipt`.
    :param type: `list[HexBytes]`
    :param fromBlock: Initial block to include in the filter.
    :param type: `BlockIdentifier`
    :param toBlock: Final block to include in the filter.
    :param type: `BlockIdentifier`
    :param address: Additional checksum address(es) for the filter.
    :param type: `ChecksumAddress`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: Encoded filter parameters.
    :rtype: `tuple[list[list[HexStr]], FilterParams]`
    """
    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    filter_params: FilterParams = {}
    topic_set: Sequence[HexStr] = encode_event_filter_topics(
        event_abi, argument_filters, abi_codec
    )

    if topics is not None:
        if len(topic_set) > 1:
            raise TypeError(
                "Merging the topics argument with topics generated "
                "from argument_filters is not supported."
            )
        topic_set = topics

    if len(topic_set) == 1 and is_list_like(topic_set[0]):
        # type ignored b/c list-like check on line 88
        filter_params["topics"] = topic_set[0]  # type: ignore
    else:
        filter_params["topics"] = topic_set

    if address and contract_address:
        if is_list_like(address):
            filter_params["address"] = [address] + [contract_address]
        elif is_string(address):
            filter_params["address"] = (
                [address, contract_address]
                if address != contract_address
                else [address]
            )
        else:
            raise ValueError(
                f"Unsupported type for `address` parameter: {type(address)}"
            )
    elif address:
        filter_params["address"] = address
    elif contract_address:
        filter_params["address"] = contract_address

    if "address" not in filter_params:
        pass
    elif is_list_like(filter_params["address"]):
        for addr in filter_params["address"]:
            validate_address(addr)
    else:
        validate_address(filter_params["address"])

    if fromBlock is not None:
        filter_params["fromBlock"] = fromBlock

    if toBlock is not None:
        filter_params["toBlock"] = toBlock

    data_filters_set = encode_event_arguments(event_abi, argument_filters, abi_codec)

    return data_filters_set, filter_params


def encode_event_filter_topics(
    event_abi: ABIEvent,
    arguments: Optional[Union[Sequence[Any], Dict[str, Any]]] = None,
    abi_codec: ABICodec = None,
) -> List[HexStr]:
    """
    Return encoded filter topics for an event.

    :param event_abi: Event ABI.
    :param type: `ABIEvent`
    :param arguments: Arguments for filter topics to be encoded.
    :param type: `list[Any]` or `dict[str, Any]`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: Encoded filter topics for an event.
    :rtype: `HexStr`
    """
    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    if arguments is None:
        arguments = {}
    if isinstance(arguments, (list, tuple)):
        if len(arguments) != len(event_abi["inputs"]):
            raise ValueError(
                "When passing an argument list, the number of arguments must "
                "match the event constructor."
            )
        arguments = {
            arg["name"]: [arg_value]
            for arg, arg_value in zip(event_abi["inputs"], arguments)
        }

    normalized_args = {
        key: value if is_list_like(value) else [value]
        # type ignored b/c arguments is always a dict at this point
        for key, value in arguments.items()  # type: ignore
    }

    # typed dict cannot be used w/ a normal Dict
    # https://github.com/python/mypy/issues/4976
    event_topic = encode_hex(event_abi_to_log_topic(event_abi))  # type: ignore
    indexed_args = get_indexed_event_inputs(event_abi)
    zipped_abi_and_args = [
        (arg, normalized_args.get(arg["name"], [None])) for arg in indexed_args
    ]
    encoded_args = [
        [
            (
                None
                if option is None
                else encode_hex(abi_codec.encode([arg["type"]], [option]))
            )
            for option in arg_options
        ]
        for arg, arg_options in zipped_abi_and_args
    ]

    return list(normalize_topic_list(cons(to_hex(event_topic), encoded_args)))


def encode_event_arguments(
    event_abi: ABIEvent,
    arguments: Optional[Union[Sequence[Any], Dict[str, Any]]] = None,
    abi_codec: ABICodec = None,
) -> List[List[Optional[HexStr]]]:
    """
    Return encoded arguments for filter parameters.

    :param event_abi: Event ABI.
    :param type: `ABIEvent`
    :param arguments: Arguments list or dict to be encoded.
    :param type: `list[Any]` or `dict[str, Any]
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: List of encoded arguments for an event.
    :rtype: `list[list[HexStr]]`
    """
    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    if arguments is None:
        arguments = {}
    if isinstance(arguments, (list, tuple)):
        if len(arguments) != len(event_abi["inputs"]):
            raise ValueError(
                "When passing an argument list, the number of arguments must "
                "match the event constructor."
            )
        arguments = {
            arg["name"]: [arg_value]
            for arg, arg_value in zip(event_abi["inputs"], arguments)
        }

    normalized_args = {
        key: value if is_list_like(value) else [value]
        # type ignored b/c at this point arguments is always a dict
        for key, value in arguments.items()  # type: ignore
    }

    non_indexed_args = exclude_indexed_event_inputs(event_abi)
    zipped_abi_and_args = [
        (arg, normalized_args.get(arg["name"], [None])) for arg in non_indexed_args
    ]
    encoded_args = [
        [
            (
                None
                if option is None
                else encode_hex(abi_codec.encode([arg["type"]], [option]))
            )
            for option in arg_options
        ]
        for arg, arg_options in zipped_abi_and_args
    ]

    data = [
        list(permutation) if any(value is not None for value in permutation) else []
        for permutation in itertools.product(*encoded_args)
    ]
    return data


def decode_transaction_data_for_event(
    event_abi: ABIEvent,
    log: Optional[LogReceipt] = None,
    abi_codec: ABICodec = None,
) -> EventData:
    """
    Return decoded event data from a log in a transaction.

    :param event_abi: Event ABI.
    :param type: `ABIEvent`
    :param log: Log data from a transaction receipt.
    :param type: `LogReceipt`
    :param event_name: Find event log with matching event name.
    :param type: `str`
    :param argument_names: Find event log with matching arguments.
    :param type: `list[str]`
    :return: Decoded event data.
    :rtype: `EventData`
    """
    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    event_args = decode_event_args(event_abi, log["data"], log["topics"], abi_codec)
    event_data = EventData(
        args=event_args["args"],
        event=event_args["event"],
        logIndex=log["logIndex"],
        transactionIndex=log["transactionIndex"],
        transactionHash=log["transactionHash"],
        address=log["address"],
        blockHash=log["blockHash"],
        blockNumber=log["blockNumber"],
    )

    return event_data


def decode_data_for_transaction(
    function_abi: ABIFunction,
    log: Optional[LogReceipt] = None,
    abi_codec: ABICodec = None,
) -> TxParams:
    """
    Return decoded results from a transaction.

    :param function_abi: Function ABI.
    :param type: `ABIFunction`
    :param log: Log data from a transaction receipt.
    :param type: `LogReceipt`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: Decoded contract call parameters for a transaction.
    :rtype: `TxParams`
    """
    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    output_types = get_abi_output_types(function_abi)
    data_bytes = log_entry_data_to_bytes(log["data"])
    try:
        output_data = abi_codec.decode(output_types, data_bytes)
    except DecodingError as e:
        # Provide a more helpful error message than the one provided by
        # eth-abi-utils
        is_missing_code_error = (
            data_bytes in ACCEPTABLE_EMPTY_STRINGS
            and w3.eth.get_code(address) in ACCEPTABLE_EMPTY_STRINGS
        )
        if is_missing_code_error:
            msg = (
                "Could not transact with/call contract function, is contract "
                "deployed correctly and chain synced?"
            )
        else:
            msg = (
                f"Could not decode contract function call to {function_abi['name']} "
                f"with return data: {str(log['data'])}, output_types: {output_types}"
            )
        raise BadFunctionCallOutput(msg) from e

    normalized_data = map_abi_data(BASE_RETURN_NORMALIZERS, output_types, output_data)

    decoded = named_tree(function_abi["outputs"], normalized_data)
    normalized_data = recursive_dict_to_namedtuple(decoded)

    if len(normalized_data) == 1:
        return normalized_data[0]
    else:
        return normalized_data


def decode_event_args(
    event_abi: ABIEvent,
    data: HexBytes = None,
    topics: Optional[Sequence[HexBytes]] = None,
    abi_codec: Optional[ABICodec] = None,
) -> EventDataArgs:
    """
    Return the name and arguments of an event.

    Recommend using `web3.utils.decode_transaction_data_for_event` which takes a
    LogReceipt and returns all event data.

    :param event_abi: Event ABI.
    :param type: `ABIEvent`
    :param data: Transaction data from a `LogReceipt`.
    :param type: `HexBytes`
    :param topics: Transaction topics from a `LogReceipt`.
    :param type: `list[HexBytes]`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: Decoded event name and arguments.
    :rtype: `EventDataArgs`
    """
    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    if not data:
        raise MismatchedABI("Data is required for decoding an event transaction.")

    log_topics = get_event_log_topics(event_abi, topics)

    log_topics_bytes = [log_entry_data_to_bytes(topic) for topic in log_topics]
    log_topics_abi = get_indexed_event_inputs(event_abi)
    log_topic_normalized_inputs = normalize_event_input_types(log_topics_abi)
    log_topic_types = get_event_abi_types_for_decoding(log_topic_normalized_inputs)
    log_topic_names = get_abi_input_names(ABIEvent({"inputs": log_topics_abi}))

    if len(log_topics_bytes) != len(log_topic_types):
        raise LogTopicError(
            f"Expected {len(log_topic_types)} log topics.  Got {len(log_topics_bytes)}"
        )

    log_data = log_entry_data_to_bytes(data)
    log_data_abi = exclude_indexed_event_inputs(event_abi)
    log_data_normalized_inputs = normalize_event_input_types(log_data_abi)
    log_data_types = get_event_abi_types_for_decoding(log_data_normalized_inputs)
    log_data_names = get_abi_input_names(ABIEvent({"inputs": log_data_abi}))

    # sanity check that there are not name intersections between the topic
    # names and the data argument names.
    duplicate_names = set(log_topic_names).intersection(log_data_names)
    if duplicate_names:
        raise InvalidEventABI(
            "The following argument names are duplicated "
            f"between event inputs: '{', '.join(duplicate_names)}'"
        )

    decoded_log_data = abi_codec.decode(log_data_types, log_data)
    normalized_log_data = map_abi_data(
        BASE_RETURN_NORMALIZERS, log_data_types, decoded_log_data
    )
    named_log_data = named_tree(
        log_data_normalized_inputs,
        normalized_log_data,
    )

    decoded_topic_data = [
        abi_codec.decode([topic_type], topic_data)[0]
        for topic_type, topic_data in zip(log_topic_types, log_topics_bytes)
    ]
    normalized_topic_data = map_abi_data(
        BASE_RETURN_NORMALIZERS, log_topic_types, decoded_topic_data
    )

    event_args = dict(
        itertools.chain(
            zip(log_topic_names, normalized_topic_data),
            named_log_data.items(),
        )
    )

    event_data_args = EventDataArgs(
        args=event_args,
        event=event_abi["name"],
    )

    return event_data_args


def decode_function_outputs(
    function_abi: ABIFunction,
    data: HexStr,
    normalizers: Sequence[Callable[[TypeStr, Any], Tuple[TypeStr, Any]]] = None,
    abi_codec: ABICodec = None,
) -> Dict[str, Any]:
    """
    Return result inputs and outputs from a function.

    :param function_abi: Function ABI.
    :param type: `ABIFunction`
    :param data: Transaction data from a `LogReceipt`.
    :param type: `HexBytes`
    :param normalizers: Normalizers applied to the decoded data.
    :param type: `list[Callable[[str, Any], Tuple[str, Any]]]`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: Decoded function outputs keyed by argument name.
    :rtype: `dict[str, Any]`
    """
    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    data_bytes = log_entry_data_to_bytes(data)
    types = get_abi_input_types(function_abi)
    decoded = abi_codec.decode(types, data_bytes)
    if normalizers:
        decoded = map_abi_data(normalizers, types, decoded)
    return named_tree(function_abi["inputs"], decoded)


def get_all_event_abis(abi: ABI) -> ABIEvent:
    """
    Return interfaces for each event in the contract ABI.

    :param abi: Contract ABI.
    :param type: `ABI`
    :return: List of ABIs for each event interface.
    :rtype: `list[ABIEvent]`
    """
    return cast(ABIEvent, filter_by_type("event", abi))


def get_event_abi(
    abi: ABI,
    event_name: Optional[str] = None,
    argument_names: Optional[Sequence[str]] = None,
) -> ABIEvent:
    """
    Find the event interface with the given name and arguments.

    :param abi: Contract ABI.
    :param type: `ABI`
    :param event_name: Find an event abi with matching event name.
    :param type: `str`
    :param argument_names: Find an event abi with matching arguments.
    :param type: `list[str]`
    :return: ABI for the event interface.
    :rtype: `ABIEvent`
    """
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


def get_all_function_abis(abi: ABI) -> ABIFunction:
    """
    Return interfaces for each function in the contract ABI.

    :param abi: Contract ABI.
    :param type: `ABI`
    :return: List of ABIs for each function interface.
    :rtype: `list[ABIFunction]`
    """
    return cast(ABIFunction, filter_by_type("function", abi))


def get_function_abi(
    abi: ABI,
    function_identifier: Optional[Union[str, Type[FallbackFn], Type[ReceiveFn]]] = None,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
    abi_codec: ABICodec = None,
) -> ABIFunction:
    """
    Return the interface for a contract function.

    :param abi: Contract ABI.
    :param type: `ABI`
    :param function_identifier: Find a function ABI with matching identifier.
    :param type: `str` or `FallbackFn` or `ReceiveFn`
    :param args: Find a function ABI with matching args.
    :param type: `list[Any]`
    :param kwargs: Find a function ABI with matching kwargs.
    :param type: `Any`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: ABI for the function interface.
    :rtype: `ABIFunction`
    """
    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    args = args or tuple()
    kwargs = kwargs or dict()
    num_arguments = len(args) + len(kwargs)

    if function_identifier is FallbackFn:
        return get_fallback_func_abi(abi)

    if function_identifier is ReceiveFn:
        return get_receive_func_abi(abi)

    if not is_text(function_identifier):
        raise TypeError("Unsupported function identifier")

    name_filter = functools.partial(filter_by_name, function_identifier)
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
            f"\nCould not identify the intended function with name "
            f"`{function_identifier}`, positional arguments with type(s) "
            f"`{collapsed_args}` and keyword arguments with type(s) "
            f"`{collapsed_kwargs}`."
            f"\nFound {len(matching_identifiers)} function(s) with the name "
            f"`{function_identifier}`: {matching_function_signatures}{diagnosis}"
        )

        raise Web3ValidationError(message)


def get_function_info(
    abi: ABI,
    function_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]],
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
) -> ABIFunctionInfo:
    """
    Return the function ABI, selector and input arguments.

    :param abi: Contract ABI.
    :param type: `ABI`
    :param function_identifier: Find a function ABI with matching identifier.
    :param type: `str` or `FallbackFn` or `ReceiveFn`
    :param args: Find a function ABI with matching args.
    :param type: `list[Any]`
    :param kwargs: Find a function ABI with matching kwargs.
    :param type: `Any`
    :return: Function information including the ABI, selector and args.
    :rtype: `ABIFunctionInfo`
    """
    args = args or tuple()
    kwargs = kwargs or dict()

    fn_abi = get_function_abi(abi, function_identifier, args, kwargs)
    # typed dict cannot be used w/ a normal Dict
    # https://github.com/python/mypy/issues/4976
    fn_selector = encode_hex(function_abi_to_4byte_selector(fn_abi))  # type: ignore
    fn_arguments = merge_args_and_kwargs(fn_abi, args, kwargs)
    _, aligned_fn_arguments = get_aligned_abi_inputs(fn_abi, fn_arguments)

    return ABIFunctionInfo(
        abi=fn_abi, selector=fn_selector, arguments=aligned_fn_arguments
    )


def get_event_log_topics(
    event_abi: ABIEvent,
    topics: Optional[Sequence[HexBytes]] = None,
) -> Sequence[HexBytes]:
    """
    Return topics from an event ABI.

    :param event_abi: Event ABI.
    :param type: `ABIEvent`
    :param topics: Transaction topics from a `LogReceipt`.
    :param type: `list[HexBytes]`
    :return: Event topics from the event ABI.
    :rtype: `list[HexBytes]`
    """
    if event_abi["anonymous"]:
        return topics
    elif not topics:
        raise MismatchedABI("Expected non-anonymous event to have 1 or more topics")
    elif event_abi_to_log_topic(dict(event_abi)) != log_entry_data_to_bytes(topics[0]):
        raise MismatchedABI("The event signature did not match the provided ABI")
    else:
        return topics[1:]


def get_abi_input_names(abi_element: ABIElement) -> List[str]:
    """
    Return names for each input from the function or event ABI.

    :param abi_element: Function or Event ABI.
    :param type: `ABIFunction` or `ABIEvent`
    :return: Names for each input in the function or event ABI.
    :rtype: `List[str]`
    """
    return _get_abi_input_names(abi_element)


def get_abi_input_types(abi_element: ABIElement) -> List[str]:
    """
    Return types for each input from the function or event ABI.

    :param abi_element: Function or Event ABI.
    :param type: `ABIFunction` or `ABIEvent`
    :return: Types for each input in the function or event ABI.
    :rtype: `List[str]`
    """
    return _get_abi_input_types(abi_element)


def get_abi_output_names(function_abi: ABIFunction) -> List[str]:
    """
    Return names for each output from the function ABI.

    :param function_abi: Function ABI.
    :param type: `ABIFunction`
    :return: Names for each function output in the function ABI.
    :rtype: `List[str]`
    """
    return _get_abi_output_names(function_abi)


def get_abi_output_types(function_abi: ABIFunction) -> List[str]:
    """
    Return types for each output from the function ABI.

    :param function_abi: Function ABI.
    :param type: `ABIFunction`
    :return: Types for each function output in the function ABI.
    :rtype: `List[str]`
    """
    return _get_abi_output_types(function_abi)
