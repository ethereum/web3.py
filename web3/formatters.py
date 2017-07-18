from __future__ import absolute_import

import warnings
import functools
import operator

from eth_utils import (
    coerce_args_to_text,
    coerce_return_to_text,
    is_address,
    is_string,
    is_integer,
    is_null,
    is_dict,
    is_0x_prefixed,
    add_0x_prefix,
    encode_hex,
    decode_hex,
    compose,
    is_list_like,
    to_normalized_address,
)

from web3.iban import Iban

from web3.utils.datastructures import (
    AttributeDict,
)
from web3.utils.empty import (
    empty,
)
from web3.utils.encoding import (
    from_decimal,
    to_decimal,
)
from web3.utils.blocks import (
    is_predefined_block_number,
)


def noop(value):
    return value


def apply_if_passes_test(test_fn):
    """
    Constructs a decorator that will cause the underlying function to only be
    applied to the given value if the `test_fn` returns true for that value.
    """
    def outer_fn(fn):
        @functools.wraps(fn)
        def inner(value):
            if test_fn(value):
                return fn(value)
            return value
        return inner
    return outer_fn


apply_if_not_null = apply_if_passes_test(compose(is_null, operator.not_))
apply_if_string = apply_if_passes_test(is_string)
apply_if_array = apply_if_passes_test(is_list_like)
apply_if_dict = apply_if_passes_test(is_dict)
apply_if_integer = apply_if_passes_test(is_integer)


def apply_to_array(formatter_fn):
    return compose(
        functools.partial(map, formatter_fn),
        list,
    )


def wrap_with(wrapper):
    def wrap_return(fn):
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            return wrapper(fn(*args, **kwargs))
        return wrapped
    return wrap_return


@coerce_args_to_text
@coerce_return_to_text
def input_block_identifier_formatter(block_identifier):
    if is_predefined_block_number(block_identifier):
        return block_identifier
    elif is_integer(block_identifier):
        return hex(block_identifier)
    else:
        return block_identifier


@coerce_args_to_text
@coerce_return_to_text
def input_filter_params_formatter(filter_params):
    formatters = {
        'fromBlock': apply_if_integer(from_decimal),
        'toBlock': apply_if_integer(from_decimal),
    }

    return {
        key: formatters.get(key, noop)(value)
        for key, value in filter_params.items()
    }


@coerce_args_to_text
@coerce_return_to_text
def input_transaction_formatter(eth, txn):
    if 'from' not in txn and eth.defaultAccount is empty:
        warnings.warn(DeprecationWarning(
            "web3.py will no longer default the `from` address to the coinbase "
            "account.  Please update your code to either explicitely provide a "
            "`from` address or to explicitely populate the `eth.defaultAccount` "
            "address."
        ))
        defaults = {
            'from': eth.coinbase,
        }
    elif eth.defaultAccount is not empty:
        defaults = {
            'from': eth.defaultAccount,
        }
    else:
        defaults = {}

    formatters = {
        'from': input_address_formatter,
        'to': input_address_formatter,
        'value': from_decimal,
        'gas': from_decimal,
        'gasPrice': from_decimal,
        'nonce': from_decimal,
    }
    return {
        key: formatters.get(key, noop)(txn.get(key, defaults.get(key)))
        for key in set(tuple(txn.keys()) + tuple(defaults.keys()))
    }


@apply_if_not_null
@wrap_with(AttributeDict)
@coerce_args_to_text
@coerce_return_to_text
def output_transaction_formatter(txn):
    formatters = {
        'blockNumber': apply_if_not_null(to_decimal),
        'transactionIndex': apply_if_not_null(to_decimal),
        'nonce': to_decimal,
        'gas': to_decimal,
        'gasPrice': to_decimal,
        'value': to_decimal,
    }

    return {
        key: formatters.get(key, noop)(value)
        for key, value in txn.items()
    }


@wrap_with(AttributeDict)
@coerce_return_to_text
def output_log_formatter(log):
    """
    Formats the output of a log
    """
    formatters = {
        'blockNumber': apply_if_not_null(to_decimal),
        'transactionIndex': apply_if_not_null(to_decimal),
        'logIndex': apply_if_not_null(to_decimal),
        'address': to_normalized_address,
    }

    return {
        key: formatters.get(key, noop)(value)
        for key, value in log.items()
    }


log_array_formatter = apply_if_not_null(apply_to_array(apply_if_dict(
    output_log_formatter
)))


@apply_if_not_null
@wrap_with(AttributeDict)
@coerce_args_to_text
@coerce_return_to_text
def output_transaction_receipt_formatter(receipt):
    """
    Formats the output of a transaction receipt to its proper values
    """
    formatters = {
        'blockNumber': apply_if_not_null(to_decimal),
        'transactionIndex': to_decimal,
        'cumulativeGasUsed': to_decimal,
        'gasUsed': to_decimal,
        'logs': log_array_formatter,
    }

    return {
        key: formatters.get(key, noop)(value)
        for key, value in receipt.items()
    }


@wrap_with(AttributeDict)
@coerce_return_to_text
def output_block_formatter(block):
    """
    Formats the output of a block to its proper values
    """
    formatters = {
        'gasLimit': to_decimal,
        'gasUsed': to_decimal,
        'size': to_decimal,
        'timestamp': to_decimal,
        'number': apply_if_not_null(to_decimal),
        'difficulty': to_decimal,
        'totalDifficulty': to_decimal,
        'transactions': apply_if_array(apply_to_array(apply_if_dict(
            output_transaction_formatter,
        ))),
    }

    return {
        key: formatters.get(key, noop)(value)
        for key, value in block.items()
    }


@coerce_return_to_text
def inputPostFormatter(post):
    """
    Formats the input of a whisper post and converts all values to HEX
    """

    post["ttl"] = from_decimal(post["ttl"])
    post["workToProve"] = from_decimal(post.get("workToProve", 0))
    post["priority"] = from_decimal(post["priority"])

    if not is_list_like(post.get("topics")):
        post["topics"] = [post["topics"]] if post.get("topics") else []

    post["topics"] = [topic if is_0x_prefixed(topic) else encode_hex(topic)
                      for topic in post["topics"]]

    return post


@coerce_return_to_text
def outputPostFormatter(post):
    """
    Formats the output of a received post message
    """

    post["expiry"] = to_decimal(post["expiry"])
    post["sent"] = to_decimal(post["sent"])
    post["ttl"] = to_decimal(post["ttl"])
    post["workProved"] = to_decimal(post["workProved"])

    if not post.get("topics"):
        post["topics"] = []

    post["topics"] = [decode_hex(topic) for topic in post["topics"]]

    return post


def input_address_formatter(addr):
    iban = Iban(addr)
    if iban.isValid() and iban.isDirect():
        return add_0x_prefix(iban.address())
    elif is_address(addr):
        return to_normalized_address(addr)

    raise ValueError("invalid address")


def transaction_pool_formatter(value, txn_formatter):
    return {
        'pending': {
            sender: {
                to_decimal(nonce): [txn_formatter(txn) for txn in txns]
                for nonce, txns in txns_by_sender.items()
            } for sender, txns_by_sender in value.get('pending', {}).items()
        },
        'queued': {
            sender: {
                to_decimal(nonce): [txn_formatter(txn) for txn in txns]
                for nonce, txns in txns_by_sender.items()
            } for sender, txns_by_sender in value.get('queued', {}).items()
        },
    }


def transaction_pool_content_formatter(value):
    return transaction_pool_formatter(value, output_transaction_formatter)


def transaction_pool_inspect_formatter(value):
    return transaction_pool_formatter(value, noop)


@apply_if_not_null
@wrap_with(AttributeDict)
def syncing_formatter(value):
    if not value:
        return value

    formatters = {
        'startingBlock': to_decimal,
        'currentBlock': to_decimal,
        'highestBlock': to_decimal,
        'knownStates': to_decimal,
        'pulledStates': to_decimal,
    }

    return {
        key: formatters.get(key, noop)(value)
        for key, value in value.items()
    }
