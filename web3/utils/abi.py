import functools
from typing import (
    Any,
    Optional,
    Sequence,
    Union,
    cast,
)

from eth_abi.abi import (
    ABICodec,
)
from eth_abi.registry import (
    registry as default_registry,
)
from eth_typing import (
    HexStr,
    Primitives,
)
from eth_typing.abi import (
    ABI,
    ABIEvent,
    ABIFunction,
    ABIFunctionInfo,
)
from eth_utils.abi import (
    event_abi_to_log_topic,
    function_abi_to_4byte_selector,
    get_aligned_abi_inputs,
    get_normalized_abi_inputs,
)
from eth_utils.conversions import (
    hexstr_if_str,
    to_bytes,
)
from eth_utils.hexadecimal import (
    encode_hex,
)
from eth_utils.toolz import (
    pipe,
)
from eth_utils.types import (
    is_text,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    abi_to_signature,
    filter_by_argument_count,
    filter_by_argument_name,
    filter_by_encodability,
    filter_by_name,
    filter_by_type,
)
from web3._utils.contracts import (
    extract_argument_types,
)
from web3.exceptions import (
    MismatchedABI,
    Web3ValidationError,
)

from eth_utils import (  # NOQA
    get_abi_input_names,
    get_abi_output_names,
)


def _get_default_codec() -> "ABICodec":
    return ABICodec(default_registry)


def get_function_info(
    abi: ABI,
    function_identifier: str,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
    abi_codec: Optional[Any] = None,
) -> ABIFunctionInfo:
    """
    Information about the function ABI, selector and input arguments.

    Returns the ABI which matches the provided identifier, named arguments (``args``)
    and keyword args (``kwargs``).

    :param abi: Contract ABI.
    :type abi: `ABI`
    :param function_identifier: Find a function ABI with matching identifier.
    :type function_identifier: `str`
    :param args: Find a function ABI with matching args.
    :type args: `list[Any]`
    :param kwargs: Find a function ABI with matching kwargs.
    :type kwargs: `Any`
    :return: Function information including the ABI, selector and args.
    :rtype: `ABIFunctionInfo`
    """
    args = args or tuple()
    kwargs = kwargs or dict()

    fn_abi = get_function_abi(
        abi, function_identifier, args, kwargs, abi_codec=abi_codec
    )
    fn_selector = encode_hex(function_abi_to_4byte_selector(fn_abi))
    fn_inputs = get_normalized_abi_inputs(fn_abi, args, kwargs)
    _, aligned_fn_inputs = get_aligned_abi_inputs(fn_abi, fn_inputs)

    return ABIFunctionInfo(
        abi=fn_abi, selector=fn_selector, arguments=aligned_fn_inputs
    )


def get_function_abi(
    abi: ABI,
    function_identifier: str,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
    abi_codec: Optional[Any] = None,
) -> ABIFunction:
    """
    Return the interface for an ``ABIFunction`` which matches the provided identifier
    and arguments.

    The ABI which matches the provided identifier, named arguments (``args``) and
    keyword args (``kwargs``) will be returned.

    The `abi_codec` may be overridden if custom encoding and decoding is required. The
    default is used if no codec is provided. More details about customizations are in
    the `eth-abi Codecs Doc <https://eth-abi.readthedocs.io/en/latest/codecs.html>`__.

    :param abi: Contract ABI.
    :type abi: `ABI`
    :param function_identifier: Find a function ABI with matching name.
    :type function_identifier: `str`
    :param args: Find a function ABI with matching args.
    :type args: `list[Any]`
    :param kwargs: Find a function ABI with matching kwargs.
    :type kwargs: `Any`
    :param abi_codec: Codec used for encoding and decoding. Default with \
    `strict_bytes_type_checking` enabled.
    :type abi_codec: `Any`

    :return: ABI for the function interface.
    :rtype: `ABIFunction`
    """
    if function_identifier is None or not is_text(function_identifier):
        raise TypeError("Unsupported function identifier")

    if abi_codec is None:
        abi_codec = _get_default_codec()

    args = args or tuple()
    kwargs = kwargs or dict()
    num_arguments = len(args) + len(kwargs)

    name_filter = functools.partial(filter_by_name, function_identifier)
    arg_count_filter = functools.partial(filter_by_argument_count, num_arguments)
    encoding_filter = functools.partial(filter_by_encodability, abi_codec, args, kwargs)

    function_candidates = cast(
        Sequence[ABIFunction], pipe(abi, name_filter, arg_count_filter, encoding_filter)
    )

    if len(function_candidates) != 1:
        matching_identifiers = name_filter(abi)
        matching_function_signatures = [
            abi_to_signature(func) for func in matching_identifiers
        ]

        arg_count_matches = len(arg_count_filter(matching_identifiers))
        encoding_matches = len(encoding_filter(matching_identifiers))

        error_diagnosis = _mismatched_abi_error_diagnosis(
            function_identifier,
            matching_function_signatures,
            arg_count_matches,
            encoding_matches,
            args,
            kwargs,
        )

        raise MismatchedABI(error_diagnosis)

    return function_candidates[0]


def _mismatched_abi_error_diagnosis(
    function_identifier: str,
    matching_function_signatures: Sequence[str],
    arg_count_matches: int,
    encoding_matches: int,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
) -> str:
    """
    Raise a ``MismatchedABI`` when a function ABI lookup results in an error.

    An error may result from multiple functions matching the provided signature and
    arguments or no functions are identified.
    """
    diagnosis = "\n"
    if arg_count_matches == 0:
        diagnosis += "Function invocation failed due to improper number of arguments."
    elif encoding_matches == 0:
        diagnosis += "Function invocation failed due to no matching argument types."
    elif encoding_matches > 1:
        diagnosis += (
            "Ambiguous argument encoding. "
            "Provided arguments can be encoded to multiple functions "
            "matching this call."
        )

    if args is not None:
        collapsed_args = extract_argument_types(args)
    else:
        collapsed_args = ""

    if kwargs is not None:
        collapsed_kwargs = dict(
            {(k, extract_argument_types([v])) for k, v in kwargs.items()}
        )
    else:
        collapsed_kwargs = {}

    return (
        f"\nCould not identify the intended function with name "
        f"`{function_identifier}`, positional arguments with type(s) "
        f"`{collapsed_args}` and keyword arguments with type(s) "
        f"`{collapsed_kwargs}`."
        f"\nFound {len(matching_function_signatures)} function(s) with the name "
        f"`{function_identifier}`: {matching_function_signatures}{diagnosis}"
    )


def get_event_abi(
    abi: ABI,
    event_name: str,
    argument_names: Optional[Sequence[str]] = None,
) -> ABIEvent:
    """
    Find the event interface with the given name and/or arguments.

    :param abi: Contract ABI.
    :type abi: `ABI`
    :param event_name: Find an event abi with matching event name.
    :type event_name: `str`
    :param argument_names: Find an event abi with matching arguments.
    :type argument_names: `list[str]`
    :return: ABI for the event interface.
    :rtype: `ABIEvent`

    .. doctest::

        >>> from eth_utils import get_event_abi
        >>> abi = [
        ...   {"type": "function", "name": "myFunction", "inputs": [], "outputs": []},
        ...   {"type": "function", "name": "myFunction2", "inputs": [], "outputs": []},
        ...   {"type": "event", "name": "MyEvent", "inputs": []}
        ... ]
        >>> get_event_abi(abi, 'MyEvent')
        {'type': 'event', 'name': 'MyEvent', 'inputs': []}
    """
    filters = [
        functools.partial(filter_by_type, "event"),
    ]

    if event_name is None or event_name == "":
        raise Web3ValidationError(
            "event_name is required in order to match an event ABI."
        )

    filters.append(functools.partial(filter_by_name, event_name))

    if argument_names is not None:
        filters.append(functools.partial(filter_by_argument_name, argument_names))

    event_abi_candidates = cast(Sequence[ABIEvent], pipe(abi, *filters))

    if len(event_abi_candidates) == 1:
        return event_abi_candidates[0]
    elif len(event_abi_candidates) == 0:
        raise ValueError("No matching events found")
    else:
        raise ValueError("Multiple events found")


def get_event_log_topics(
    event_abi: ABIEvent,
    topics: Optional[Sequence[HexBytes]] = None,
) -> Sequence[HexBytes]:
    r"""
    Return topics for an event ABI.

    :param event_abi: Event ABI.
    :type event_abi: `ABIEvent`
    :param topics: Transaction topics from a `LogReceipt`.
    :type topics: `list[HexBytes]`
    :return: Event topics for the event ABI.
    :rtype: `list[HexBytes]`

    .. doctest::

        >>> from eth_utils import get_event_log_topics
        >>> abi = {
        ...   'type': 'event',
        ...   'anonymous': False,
        ...   'name': 'MyEvent',
        ...   'inputs': [
        ...     {
        ...       'name': 's',
        ...       'type': 'uint256'
        ...     }
        ...   ]
        ... }
        >>> keccak_signature = b'l+Ff\xba\x8d\xa5\xa9W\x17b\x1d\x87\x9aw\xder_=\x81g\t\xb9\xcb\xe9\xf0Y\xb8\xf8u\xe2\x84'  # noqa: E501
        >>> get_event_log_topics(abi, [keccak_signature, '0x1', '0x2'])
        ['0x1', '0x2']
    """
    if topics is None:
        topics = []

    if event_abi["anonymous"]:
        return topics
    elif len(topics) == 0:
        raise MismatchedABI("Expected non-anonymous event to have 1 or more topics")
    elif event_abi_to_log_topic(event_abi) != log_topic_to_bytes(topics[0]):
        raise MismatchedABI("The event signature did not match the provided ABI")
    else:
        return topics[1:]


def log_topic_to_bytes(
    log_topic: Union[Primitives, HexStr, str],
) -> bytes:
    """
    Return topic signature as bytes.

    :param log_topic: Event topic from a `LogReceipt`.
    :type log_topic: `Primitive`, `HexStr` or `str`
    """
    return hexstr_if_str(to_bytes, log_topic)
