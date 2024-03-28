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
from eth_abi.registry import (
    registry as default_registry,
)
from eth_typing import (
    HexStr,
    TypeStr,
)
from eth_utils import (
    encode_hex,
    event_abi_to_log_topic,
    function_abi_to_4byte_selector,
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
)
from web3._utils.events import (
    get_event_abi_types_for_decoding,
    log_entry_data_to_bytes,
)
from web3._utils.function_identifiers import (
    FallbackFn,
    ReceiveFn,
)
from web3._utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
)
from web3.exceptions import (
    InvalidEventABI,
    LogTopicError,
    MismatchedABI,
    Web3ValidationError,
)
from web3.types import (
    ABI,
    ABIElement,
    ABIEvent,
    ABIFunction,
    ABIFunctionInfo,
    EventData,
    EventDataArgs,
    LogReceipt,
)


def parse_transaction_for_event(
    event_abi: ABIEvent, log: Optional[LogReceipt] = None, strict: Optional[bool] = True
) -> EventData:
    """
    Return a decoded event from the given log.

    :param abi: Contract ABI.
    :param type: `ABI`
    :param log: Log data from a transaction receipt.
    :param type: `LogReceipt`
    :param event_name: Find event log with matching event name.
    :param type: `str`
    :param argument_names: Find event log with matching arguments.
    :param type: `list[str]`
    :return: Decoded event data.
    :rtype: `EventData`
    """
    event_args = decode_event_args(event_abi, log["data"], log["topics"], strict)
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


def decode_event_args(
    event_abi: ABIEvent,
    data: HexBytes = None,
    topics: Optional[Sequence[HexBytes]] = None,
    strict: Optional[bool] = True,
) -> EventDataArgs:
    """
    Return the name and arguments of an event.

    Recommend using `web3.utils.parse_log_for_event` which takes a LogReceipt and
    returns all event data.

    :param event_abi: Event ABI.
    :param type: `ABIEvent`
    :param data: Transaction data from a `LogReceipt`.
    :param type: `HexBytes`
    :param topics: Transaction topics from a `LogReceipt`.
    :param type: `list[HexBytes]`
    :return: Decoded event name and arguments.
    :rtype: `EventDataArgs`
    """
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

    decoded_log_data = abi_codec.decode(log_data_types, log_data, strict)
    normalized_log_data = map_abi_data(
        BASE_RETURN_NORMALIZERS, log_data_types, decoded_log_data
    )
    named_log_data = named_tree(
        log_data_normalized_inputs,
        normalized_log_data,
    )

    decoded_topic_data = [
        abi_codec.decode([topic_type], topic_data, strict)[0]
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
    strict: Optional[bool] = True,
) -> Dict[str, Any]:
    """
    Return result inputs and outputs from a function.

    :param event_abi: Event ABI.
    :param type: `ABIEvent`
    :param data: Transaction data from a `LogReceipt`.
    :param type: `HexBytes`
    :param topics: Transaction topics from a `LogReceipt`.
    :param type: `list[HexBytes]`
    :return: Decoded event name and arguments.
    :rtype: `EventDataArgs`
    """
    data_bytes = log_entry_data_to_bytes(data)
    types = get_abi_input_types(function_abi)
    abi_codec = ABICodec(default_registry)
    decoded = abi_codec.decode(types, data_bytes, strict)
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
) -> ABIFunction:
    """
    Return the interface for a contract function.

    :param abi: Contract ABI.
    :param type: `ABI`
    :param function_identifier: Find a function ABI with matching identifier.
    :param type: `str` or `FallbackFn` or `ReceiveFn`
    :kparam args: Find a function ABI with matching args.
    :param type: list[Any]
    :param kwargs: Find a function ABI with matching kwargs.
    :param type: Any
    :return: ABI for the function interface.
    :rtype: `ABIFunction`
    """
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
    :kparam args: Find a function ABI with matching args.
    :param type: list[Any]
    :param kwargs: Find a function ABI with matching kwargs.
    :param type: Any
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
    :return: Names for each input in the function or event ABI.
    :rtype: `List[str]`
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
