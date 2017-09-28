import random

from eth_utils import (
    decode_hex,
    is_string,
)
from cytoolz import (
    curry,
    dissoc,
    merge,
    pipe,
)

import rlp
from rlp.sedes import (
    Binary,
    big_endian_int,
    binary,
)

from web3.utils.compat import (
    Timeout,
)
from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.formatters import (
    apply_formatter_if,
)


def serializable_unsigned_transaction(web3, transaction_dict):
    return pipe(
        transaction_dict,
        dict,
        format_transaction_values,
        fill_transaction_defaults(web3),
    )


def encode_transaction(unsigned_transaction, vrs):
    (v, r, s) = vrs
    chain_naive_transaction = dissoc(vars(unsigned_transaction), 'v', 'r', 's')
    signed_transaction = Transaction(v=v, r=r, s=s, **chain_naive_transaction)
    return rlp.encode(signed_transaction)


def coerce_to_decimal_excluding_unicode(val):
    if is_string(val):
        return to_decimal(hexstr=val)
    else:
        return to_decimal(val)


TRANSACTION_DEFAULTS = {
    'gasPrice': lambda web3: web3.eth.gasPrice,
    'value': lambda web3: 0,
    'data': lambda web3: b'',
    'chainId': lambda web3: 1,  # TODO implement default web3.eth.net.getId()
}

TRANSACTION_FORMATTERS = {
    'nonce': coerce_to_decimal_excluding_unicode,
    'gasPrice': coerce_to_decimal_excluding_unicode,
    'gas': coerce_to_decimal_excluding_unicode,
    'to': apply_formatter_if(decode_hex, is_string),
    'value': coerce_to_decimal_excluding_unicode,
    'data': apply_formatter_if(is_string, decode_hex),
    'v': coerce_to_decimal_excluding_unicode,
    'r': coerce_to_decimal_excluding_unicode,
    's': coerce_to_decimal_excluding_unicode,
}


def format_transaction_values(transaction_dict):
    # See EIP 155
    chain_id = transaction_dict.pop('chainId')
    chain_aware_txn = dict(transaction_dict, v=chain_id, r=0, s=0)

    return {
        key: TRANSACTION_FORMATTERS[key](val)
        for key, val
        in chain_aware_txn.items()
    }


@curry
def fill_transaction_defaults(web3, transaction):
    defaults = {}
    for key, default_func in TRANSACTION_DEFAULTS.items():
        if key not in transaction:
            defaults[key] = default_func(web3)
    full_txn = merge(defaults, transaction)
    return Transaction(**full_txn)


class Transaction(rlp.Serializable):
    fields = (
        ('nonce', big_endian_int),
        ('gasPrice', big_endian_int),
        ('gas', big_endian_int),
        ('to', Binary.fixed_length(20, allow_empty=True)),
        ('value', big_endian_int),
        ('data', binary),
        ('v', big_endian_int),
        ('r', big_endian_int),
        ('s', big_endian_int),
    )


def wait_for_transaction_receipt(web3, txn_hash, timeout=120):
    with Timeout(timeout) as _timeout:
        while True:
            txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
            if txn_receipt is not None:
                break
            _timeout.sleep(random.random())
    return txn_receipt


def get_block_gas_limit(web3, block_identifier=None):
    if block_identifier is None:
        block_identifier = web3.eth.blockNumber
    block = web3.eth.getBlock(block_identifier)
    return block['gasLimit']


def get_buffered_gas_estimate(web3, transaction, gas_buffer=100000):
    gas_estimate_transaction = dict(**transaction)

    gas_estimate = web3.eth.estimateGas(gas_estimate_transaction)

    gas_limit = get_block_gas_limit(web3)

    if gas_estimate > gas_limit:
        raise ValueError(
            "Contract does not appear to be deployable within the "
            "current network gas limits.  Estimated: {0}. Current gas "
            "limit: {1}".format(gas_estimate, gas_limit)
        )

    return min(gas_limit, gas_estimate + gas_buffer)
