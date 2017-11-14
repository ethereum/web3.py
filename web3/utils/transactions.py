import itertools
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

from web3.utils.threads import (
    Timeout,
)
from web3.utils.encoding import (
    ExtendedRLP,
    hexstr_if_str,
    to_int,
)
from web3.utils.formatters import (
    apply_formatter_if,
    apply_formatters_to_dict,
)


def serializable_unsigned_transaction_from_dict(web3, transaction_dict):
    '''
    if web3 is None, fill out transaction as much as possible without calling client
    '''
    filled_transaction = pipe(
        transaction_dict,
        dict,
        fill_transaction_defaults(web3),
        chain_id_to_v,
        apply_formatters_to_dict(TRANSACTION_FORMATTERS),
    )
    if 'v' in filled_transaction:
        serializer = Transaction
    else:
        serializer = UnsignedTransaction
    return serializer.from_dict(filled_transaction)


def encode_transaction(unsigned_transaction, vrs):
    (v, r, s) = vrs
    chain_naive_transaction = dissoc(vars(unsigned_transaction), 'v', 'r', 's')
    signed_transaction = Transaction(v=v, r=r, s=s, **chain_naive_transaction)
    return rlp.encode(signed_transaction)


TRANSACTION_DEFAULTS = {
    'gasPrice': lambda web3: web3.eth.gasPrice,
    'value': 0,
    'data': b'',
    'chainId': lambda web3: int(web3.net.version),
}

TRANSACTION_FORMATTERS = {
    'nonce': hexstr_if_str(to_int),
    'gasPrice': hexstr_if_str(to_int),
    'gas': hexstr_if_str(to_int),
    'to': apply_formatter_if(is_string, decode_hex),
    'value': hexstr_if_str(to_int),
    'data': apply_formatter_if(is_string, decode_hex),
    'v': hexstr_if_str(to_int),
    'r': hexstr_if_str(to_int),
    's': hexstr_if_str(to_int),
}


def chain_id_to_v(transaction_dict):
    # See EIP 155
    chain_id = transaction_dict.pop('chainId')
    if chain_id is None:
        return transaction_dict
    else:
        return dict(transaction_dict, v=chain_id, r=0, s=0)


@curry
def fill_transaction_defaults(web3, transaction):
    '''
    if web3 is None, fill as much as possible while offline
    '''
    defaults = {}
    for key, default_getter in TRANSACTION_DEFAULTS.items():
        if key not in transaction:
            if callable(default_getter):
                if web3 is not None:
                    default_val = default_getter(web3)
                else:
                    raise ValueError("You must specify %s in the transaction" % key)
            else:
                default_val = default_getter
            defaults[key] = default_val
    return merge(defaults, transaction)


class Transaction(ExtendedRLP):
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


UnsignedTransaction = Transaction.exclude(['v', 'r', 's'])


ChainAwareUnsignedTransaction = Transaction


def strip_signature(txn):
    unsigned_parts = itertools.islice(txn, len(UnsignedTransaction.fields))
    return list(unsigned_parts)


def vrs_from(transaction):
    return (getattr(transaction, part) for part in 'vrs')


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
