import functools
from typing import (
    Any,
    List,
    Optional,
    Sequence,
    Union,
    cast,
)

from eth_typing import (
    ABIFunctionInfo,
)
from eth_utils.abi import (
    function_abi_to_4byte_selector,
    get_aligned_abi_inputs,
    get_normalized_abi_inputs,
)
from eth_utils.encoding import (
    get_default_codec,
)
from eth_utils.hexadecimal import (
    encode_hex,
)
from eth_utils.types import (
    is_text,
)

from web3._utils.abi import (
    abi_to_signature,
    filter_by_argument_count,
    filter_by_encodability,
    filter_by_name,
)
from web3._utils.contracts import (
    extract_argument_types,
)
from web3.exceptions import (
    MismatchedABI,
)
from web3.types import (
    ABI,
    ABIEvent,
    ABIFunction,
)

from .toolz import (
    pipe,
)


def get_abi_input_names(abi: Union[ABIFunction, ABIEvent]) -> List[str]:
    if "inputs" not in abi and abi["type"] == "fallback":
        return []
    return [arg["name"] for arg in abi["inputs"]]


def get_abi_output_names(abi: Union[ABIFunction]) -> List[str]:
    if "outputs" not in abi and abi["type"] == "fallback":
        return []
    return [arg["name"] for arg in abi["outputs"]]


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
        abi_codec = get_default_codec()

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
