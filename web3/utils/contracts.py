import functools

from cytoolz import (
    pipe,
)
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
)
from hexbytes import (
    HexBytes,
)

from web3.utils.abi import (
    check_if_arguments_can_be_encoded,
    filter_by_argument_count,
    filter_by_argument_name,
    filter_by_encodability,
    filter_by_name,
    filter_by_type,
    get_abi_input_types,
    map_abi_data,
    merge_args_and_kwargs,
)
from web3.utils.encoding import (
    to_hex,
)
from web3.utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_hex,
    abi_ens_resolver,
    abi_string_to_hex,
    hexstrs_to_bytes,
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


def find_matching_fn_abi(abi, fn_name=None, args=None, kwargs=None):
    filters = []

    if fn_name:
        filters.append(functools.partial(filter_by_name, fn_name))

    if args is not None or kwargs is not None:
        if args is None:
            args = tuple()
        if kwargs is None:
            kwargs = {}

        num_arguments = len(args) + len(kwargs)
        filters.extend([
            functools.partial(filter_by_argument_count, num_arguments),
            functools.partial(filter_by_encodability, args, kwargs),
        ])

    function_candidates = filter_by_type('function', abi)

    function_candidates = pipe(abi, *filters)

    if len(function_candidates) == 1:
        return function_candidates[0]
    if not function_candidates:
        raise ValueError("No matching functions found")
    else:
        raise ValueError("Multiple functions found")


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
            abi_bytes_to_hex,
            abi_string_to_hex,
            hexstrs_to_bytes,
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


def prepare_transaction(abi,
                        address,
                        web3,
                        fn_name,
                        fn_args=None,
                        fn_kwargs=None,
                        transaction=None):
    """
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
        abi,
        web3,
        fn_name,
        fn_args,
        fn_kwargs,
    )
    return prepared_transaction


def encode_transaction_data(abi, web3, fn_name, args=None, kwargs=None):
    fn_abi, fn_selector, fn_arguments = get_function_info(
        abi, fn_name, args, kwargs,
    )
    return add_0x_prefix(encode_abi(web3, fn_abi, fn_arguments, fn_selector))


def get_function_info(abi, fn_name, args=None, kwargs=None):
    if args is None:
        args = tuple()
    if kwargs is None:
        kwargs = {}

    fn_abi = find_matching_fn_abi(abi, fn_name, args, kwargs)
    fn_selector = encode_hex(function_abi_to_4byte_selector(fn_abi))

    fn_arguments = merge_args_and_kwargs(fn_abi, args, kwargs)

    return fn_abi, fn_selector, fn_arguments
