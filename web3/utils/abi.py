import functools
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Sequence,
    Union,
    cast,
)

from eth_abi import (
    codec,
)
from eth_abi.codec import (
    ABICodec,
)
from eth_abi.registry import (
    registry as default_registry,
)
from eth_typing import (
    ABIElement,
    ABIError,
    ABIEvent,
    ABIFallback,
    ABIReceive,
)
from eth_typing.abi import (
    ABI,
    ABIFunction,
    ABIFunctionInfo,
)
from eth_utils.abi import (
    filter_by_type,
)
from eth_utils.address import (
    is_binary_address,
    is_checksum_address,
)
from eth_utils.hexadecimal import (
    encode_hex,
)
from eth_utils.toolz import (
    pipe,
)
from eth_utils.types import (
    is_list_like,
    is_text,
)

from web3._utils.function_identifiers import (
    FallbackFn,
    ReceiveFn,
)
from web3.exceptions import (
    FallbackNotFound,
    MismatchedABI,
)
from web3.types import (
    FunctionIdentifier,
)

from eth_utils.abi import (  # noqa
    abi_to_signature,
    event_abi_to_log_topic,
    event_signature_to_log_topic,
    function_abi_to_4byte_selector,
    function_signature_to_4byte_selector,
    get_abi_input_names,
    get_abi_input_types,
    get_abi_output_names,
    get_abi_output_types,
    get_aligned_abi_inputs,
    get_all_event_abis,
    get_all_function_abis,
    get_normalized_abi_arg_type,
    get_normalized_abi_inputs,
)


def _filter_by_argument_count(
    num_arguments: int, contract_abi: ABI
) -> List[ABIElement]:
    return [
        abi
        for abi in contract_abi
        if abi["type"] != "fallback"
        and abi["type"] != "receive"
        and len(abi["inputs"]) == num_arguments
    ]


def _filter_by_encodability(
    abi_codec: codec.ABIEncoder,
    args: Sequence[Any],
    kwargs: Dict[str, Any],
    contract_abi: ABI,
) -> List[ABIFunction]:
    return [
        cast(ABIFunction, function_abi)
        for function_abi in contract_abi
        if check_if_arguments_can_be_encoded(
            cast(ABIFunction, function_abi), abi_codec, args, kwargs
        )
    ]


def _mismatched_abi_error_diagnosis(
    function_identifier: FunctionIdentifier,
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
        collapsed_args = _extract_argument_types(args)
    else:
        collapsed_args = ""

    if kwargs is not None:
        collapsed_kwargs = dict(
            {(k, _extract_argument_types([v])) for k, v in kwargs.items()}
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


def _extract_argument_types(*args: Sequence[Any]) -> str:
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
                    collapsed_nested.append(f"({_extract_argument_types(nested)})")
                else:
                    collapsed_nested.append(_get_argument_readable_type(nested))
            collapsed_args.append(",".join(collapsed_nested))
        else:
            collapsed_args.append(_get_argument_readable_type(arg))

    return ",".join(collapsed_args)


def _get_argument_readable_type(arg: Any) -> str:
    if is_checksum_address(arg) or is_binary_address(arg):
        return "address"

    return arg.__class__.__name__


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

    .. doctest

        >>> from web3.utils.abi import get_function_info
        >>> abi = [
        ...     {
        ...         "constant": False,
        ...         "inputs": [
        ...             {"name": "a", "type": "uint256"},
        ...             {"name": "b", "type": "uint256"},
        ...         ],
        ...         "name": "multiply",
        ...         "outputs": [{"name": "result", "type": "uint256"}],
        ...         "payable": False,
        ...         "stateMutability": "nonpayable",
        ...         "type": "function",
        ...     }
        ... ]
        >>> fn_info = get_function_info(abi, "multiply", [7, 3])
        >>> fn_info.abi
        {'constant': False, 'inputs': [{'name': 'a', 'type': 'uint256'}, {\
'name': 'b', 'type': 'uint256'}], 'name': 'multiply', 'outputs': [{\
'name': 'result', 'type': 'uint256'}], 'payable': False, \
'stateMutability': 'nonpayable', 'type': 'function'}
        >>> fn_info.selector
        '0x12345678'
        >>> fn_info.arguments
        [{'name': 'a', 'type': 'uint256', 'value': 7}, {\
'name': 'b', 'type': 'uint256', 'value': 3}]
    """
    args = args or tuple()
    kwargs = kwargs or dict()

    fn_abi = get_function_abi(
        abi, function_identifier, args, kwargs, abi_codec=abi_codec
    )
    fn_selector = encode_hex(function_abi_to_4byte_selector(fn_abi))

    if fn_abi["type"] == "fallback" or fn_abi["type"] == "receive":
        return ABIFunctionInfo(abi=fn_abi, selector=fn_selector, arguments=tuple())
    else:
        fn_inputs = get_normalized_abi_inputs(fn_abi, args, kwargs)
        _, aligned_fn_inputs = get_aligned_abi_inputs(fn_abi, fn_inputs)

        return ABIFunctionInfo(
            abi=fn_abi, selector=fn_selector, arguments=aligned_fn_inputs
        )


def get_function_abi(
    abi: ABI,
    function_identifier: FunctionIdentifier,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
    abi_codec: Optional[Any] = None,
) -> Union[ABIFunction, ABIError, ABIFallback, ABIReceive]:
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
    :type function_identifier: `FunctionIdentifier`
    :param args: Find a function ABI with matching args.
    :type args: `list[Any]`
    :param kwargs: Find a function ABI with matching kwargs.
    :type kwargs: `Any`
    :param abi_codec: Codec used for encoding and decoding. Default with \
    `strict_bytes_type_checking` enabled.
    :type abi_codec: `Any`
    :return: ABI for the function interface.
    :rtype: `ABIFunction`

    .. doctest

        >>> from web3.utils.abi import get_function_abi
        >>> abi = [
        ...     {
        ...         "constant": False,
        ...         "inputs": [
        ...             {"name": "a", "type": "uint256"},
        ...             {"name": "b", "type": "uint256"},
        ...         ],
        ...         "name": "multiply",
        ...         "outputs": [{"name": "result", "type": "uint256"}],
        ...         "payable": False,
        ...         "stateMutability": "nonpayable",
        ...         "type": "function",
        ...     }
        ... ]
        >>> get_function_abi(abi, "multiply", [7, 3])
        {'constant': False, 'inputs': [{'name': 'a', 'type': 'uint256'}, {\
'name': 'b', 'type': 'uint256'}], 'name': 'multiply', 'outputs': [{'name': 'result', \
'type': 'uint256'}], 'payable': False, 'stateMutability': 'nonpayable', \
'type': 'function'}
    """
    if function_identifier is FallbackFn:
        return get_fallback_function_abi(abi)

    if function_identifier is ReceiveFn:
        return get_receive_function_abi(abi)

    if function_identifier is None or not is_text(function_identifier):
        raise TypeError("Unsupported function identifier")

    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    args = args or tuple()
    kwargs = kwargs or dict()
    num_arguments = len(args) + len(kwargs)

    name_filter = functools.partial(filter_abi_by_name, function_identifier)
    arg_count_filter = functools.partial(_filter_by_argument_count, num_arguments)
    encoding_filter = functools.partial(
        _filter_by_encodability, abi_codec, args, kwargs
    )

    function_matches = pipe(abi, name_filter, arg_count_filter, encoding_filter)
    function_candidates: List[Union[ABIFunction, ABIError]] = []
    for fn in function_matches:
        if fn["type"] == "error":
            function_candidates.append(cast(ABIError, fn))
        elif fn["type"] == "function":
            function_candidates.append(cast(ABIFunction, fn))

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


def get_receive_function_abi(contract_abi: ABI) -> ABIReceive:
    receive_abis = filter_by_type("receive", contract_abi)
    if receive_abis and receive_abis[0]["type"] == "receive":
        return cast(ABIReceive, receive_abis[0])
    else:
        raise FallbackNotFound("No receive function was found in the contract ABI.")


def get_fallback_function_abi(contract_abi: ABI) -> ABIFallback:
    fallback_abis = filter_by_type("fallback", contract_abi)
    if fallback_abis and fallback_abis[0]["type"] == "fallback":
        return cast(ABIFallback, fallback_abis[0])
    else:
        raise FallbackNotFound("No fallback function was found in the contract ABI.")


def filter_abi_by_name(
    name: str, contract_abi: ABI
) -> List[Union[ABIFunction, ABIEvent, ABIError]]:
    """
    Get one or more function and event ABIs by name.

    :param name: Name of the function or event.
    :type name: `str`
    :param contract_abi: Contract ABI.
    :type contract_abi: `ABI`
    :return: Function or event ABIs with matching name.
    :rtype: `List[ABIElement]`

    .. doctest

            >>> from web3.utils.abi import filter_abi_by_name
            >>> abi = [
            ...     {
            ...         "constant": False,
            ...         "inputs": [],
            ...         "name": "func_1",
            ...         "outputs": [],
            ...         "type": "function",
            ...     },
            ...     {
            ...         "constant": False,
            ...         "inputs": [
            ...             {"name": "a", "type": "uint256"},
            ...         ],
            ...         "name": "func_2",
            ...         "outputs": [],
            ...         "type": "function",
            ...     },
            ...     {
            ...         "constant": False,
            ...         "inputs": [
            ...             {"name": "a", "type": "uint256"},
            ...             {"name": "b", "type": "uint256"},
            ...         ],
            ...         "name": "func_3",
            ...         "outputs": [],
            ...         "type": "function",
            ...     },
            ...     {
            ...         "constant": False,
            ...         "inputs": [
            ...             {"name": "a", "type": "uint256"},
            ...             {"name": "b", "type": "uint256"},
            ...             {"name": "c", "type": "uint256"},
            ...         ],
            ...         "name": "func_4",
            ...         "outputs": [],
            ...         "type": "function",
            ...     },
            ... ]
            >>> filter_abi_by_name("func_1", abi)
            [{'constant': False, 'inputs': [], 'name': 'func_1', 'outputs': [], \
'type': 'function'}]
    """
    return [
        abi
        for abi in contract_abi
        if (
            (
                abi["type"] == "function"
                or abi["type"] == "event"
                or abi["type"] == "error"
            )
            and abi["name"] == name
        )
    ]


def check_if_arguments_can_be_encoded(
    function_abi: ABIFunction,
    abi_codec: codec.ABIEncoder,
    args: Sequence[Any],
    kwargs: Dict[str, Any],
) -> bool:
    """
    Check if the provided arguments can be encoded with the function ABI.

    :param function_abi: Function ABI.
    :type function_abi: `ABIFunction`
    :param abi_codec: Codec used for encoding and decoding.
    :type abi_codec: `ABIEncoder`
    :param args: Positional arguments.
    :type args: `list[Any]`
    :param kwargs: Keyword arguments.
    :type kwargs: `Any`

    .. doctest

            >>> from web3.utils.abi import check_if_arguments_can_be_encoded
            >>> abi = {
            ...     "constant": False,
            ...     "inputs": [
            ...         {"name": "a", "type": "uint256"},
            ...         {"name": "b", "type": "uint256"},
            ...     ],
            ...     "name": "multiply",
            ...     "outputs": [{"name": "result", "type": "uint256"}],
            ...     "payable": False,
            ...     "stateMutability": "nonpayable",
            ...     "type": "function",
            ... }
            >>> check_if_arguments_can_be_encoded(abi, [7, 3])
            True
    """
    try:
        arguments = get_normalized_abi_inputs(function_abi, args, kwargs)
    except TypeError:
        return False

    if len(function_abi.get("inputs", [])) != len(arguments):
        return False

    try:
        types, aligned_args = get_aligned_abi_inputs(function_abi, arguments)
    except TypeError:
        return False

    return all(
        abi_codec.is_encodable(_type, arg) for _type, arg in zip(types, aligned_args)
    )
