import functools

from eth_abi import (
    encode_abi as eth_abi_encode_abi,
)
from eth_abi.exceptions import (
    EncodingError,
)
from eth_utils import (
    add_0x_prefix,
    encode_hex,
    function_abi_to_4byte_selector,
    is_text,
)
from hexbytes import (
    HexBytes,
)

from web3.exceptions import (
    ValidationError,
)
from web3.utils.abi import (
    abi_to_signature,
    check_if_arguments_can_be_encoded,
    filter_by_argument_count,
    filter_by_argument_name,
    filter_by_encodability,
    filter_by_name,
    filter_by_type,
    get_abi_input_types,
    get_fallback_func_abi,
    map_abi_data,
    merge_args_and_kwargs,
)
from web3.utils.encoding import (
    to_hex,
)
from web3.utils.function_identifiers import (
    FallbackFn,
)
from web3.utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_bytes,
    abi_ens_resolver,
    abi_string_to_text,
)
from web3.utils.toolz import (
    pipe,
    valmap,
)


def find_matching_event_abi(abi, event_name=None, argument_names=None):

    filters = [
        functools.partial(filter_by_type, 'event'),
    ]

    if event_name is not None:
        filters.append(functools.partial(filter_by_name, event_name))

    if argument_names is not None:
        filters.append(
            functools.partial(filter_by_argument_name, argument_names)
        )

    event_abi_candidates = pipe(abi, *filters)

    if len(event_abi_candidates) == 1:
        return event_abi_candidates[0]
    elif not event_abi_candidates:
        raise ValueError("No matching events found")
    else:
        raise ValueError("Multiple events found")


def find_matching_fn_abi(abi, fn_identifier=None, args=None, kwargs=None):
    args = args or tuple()
    kwargs = kwargs or dict()
    filters = []
    num_arguments = len(args) + len(kwargs)

    if fn_identifier is FallbackFn:
        return get_fallback_func_abi(abi)

    if not is_text(fn_identifier):
        raise TypeError("Unsupported function identifier")

    name_filter = functools.partial(filter_by_name, fn_identifier)
    arg_count_filter = functools.partial(filter_by_argument_count, num_arguments)
    encoding_filter = functools.partial(filter_by_encodability, args, kwargs)
    filters.extend([
        name_filter,
        arg_count_filter,
        encoding_filter,
    ])
    function_candidates = pipe(abi, *filters)
    if len(function_candidates) == 1:
        return function_candidates[0]
    else:
        matching_identifiers = name_filter(abi)
        matching_function_signatures = [abi_to_signature(func) for func in matching_identifiers]
        arg_count_matches = len(arg_count_filter(matching_identifiers))
        encoding_matches = len(encoding_filter(matching_identifiers))
        if arg_count_matches == 0:
            diagnosis = "\nFunction invocation failed due to improper number of arguments."
        elif encoding_matches == 0:
            diagnosis = "\nFunction invocation failed due to no matching argument types."
        elif encoding_matches > 1:
            diagnosis = (
                "\nAmbiguous argument encoding. "
                "Provided arguments can be encoded to multiple functions matching this call."
            )
        message = (
            "\nCould not identify the intended function with name `{name}`, "
            "positional argument(s) of type `{arg_types}` and "
            "keyword argument(s) of type `{kwarg_types}`."
            "\nFound {num_candidates} function(s) with the name `{name}`: {candidates}"
            "{diagnosis}"
        ).format(
            name=fn_identifier,
            arg_types=tuple(map(type, args)),
            kwarg_types=valmap(type, kwargs),
            num_candidates=len(matching_identifiers),
            candidates=matching_function_signatures,
            diagnosis=diagnosis,
        )
        raise ValidationError(message)


def encode_abi(web3, abi, arguments, data=None):
    argument_types = get_abi_input_types(abi)

    if not check_if_arguments_can_be_encoded(abi, arguments, {}):
        raise TypeError(
            "One or more arguments could not be encoded to the necessary "
            "ABI type.  Expected types are: {0}".format(
                ', '.join(argument_types),
            )
        )

    try:
        normalizers = [
            abi_ens_resolver(web3),
            abi_address_to_hex,
            abi_bytes_to_bytes,
            abi_string_to_text,
        ]
        normalized_arguments = map_abi_data(
            normalizers,
            argument_types,
            arguments,
        )
        encoded_arguments = eth_abi_encode_abi(
            argument_types,
            normalized_arguments,
        )
    except EncodingError as e:
        raise TypeError(
            "One or more arguments could not be encoded to the necessary "
            "ABI type: {0}".format(str(e))
        )

    if data:
        return to_hex(HexBytes(data) + encoded_arguments)
    else:
        return encode_hex(encoded_arguments)


def prepare_transaction(
        address,
        web3,
        fn_identifier,
        contract_abi=None,
        fn_abi=None,
        transaction=None,
        fn_args=None,
        fn_kwargs=None):
    """
    :parameter `is_function_abi` is used to distinguish  function abi from contract abi
    Returns a dictionary of the transaction that could be used to call this
    TODO: make this a public API
    TODO: add new prepare_deploy_transaction API
    """
    if transaction is None:
        prepared_transaction = {}
    else:
        prepared_transaction = dict(**transaction)

    if 'data' in prepared_transaction:
        raise ValueError("Transaction parameter may not contain a 'data' key")

    if address:
        prepared_transaction.setdefault('to', address)

    prepared_transaction['data'] = encode_transaction_data(
        web3,
        fn_identifier,
        contract_abi,
        fn_abi,
        fn_args,
        fn_kwargs,
    )
    return prepared_transaction


def encode_transaction_data(
        web3,
        fn_identifier,
        contract_abi=None,
        fn_abi=None,
        args=None,
        kwargs=None):
    if fn_identifier is FallbackFn:
        fn_abi, fn_selector, fn_arguments = get_fallback_function_info(contract_abi, fn_abi)
    elif is_text(fn_identifier):
        fn_abi, fn_selector, fn_arguments = get_function_info(
            fn_identifier, contract_abi, fn_abi, args, kwargs,
        )
    else:
        raise TypeError("Unsupported function identifier")

    return add_0x_prefix(encode_abi(web3, fn_abi, fn_arguments, fn_selector))


def get_fallback_function_info(contract_abi=None, fn_abi=None):
    if fn_abi is None:
        fn_abi = get_fallback_func_abi(contract_abi)
    fn_selector = encode_hex(b'')
    fn_arguments = tuple()
    return fn_abi, fn_selector, fn_arguments


def get_function_info(fn_name, contract_abi=None, fn_abi=None, args=None, kwargs=None):
    if args is None:
        args = tuple()
    if kwargs is None:
        kwargs = {}

    if fn_abi is None:
        fn_abi = find_matching_fn_abi(contract_abi, fn_name, args, kwargs)

    fn_selector = encode_hex(function_abi_to_4byte_selector(fn_abi))

    fn_arguments = merge_args_and_kwargs(fn_abi, args, kwargs)

    return fn_abi, fn_selector, fn_arguments
