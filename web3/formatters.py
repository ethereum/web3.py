from __future__ import absolute_import

import functools

from web3.iban import Iban

from web3.utils.string import (
    force_text,
    coerce_args_to_text,
    coerce_return_to_text,
)
from web3.utils.address import (
    is_address,
    is_strict_address,
)
from web3.utils.types import (
    is_array,
    is_string,
)
from web3.utils.formatting import (
    is_0x_prefixed,
)
from web3.utils.encoding import (
    to_hex,
    encode_hex,
    decode_hex,
    from_decimal,
    to_decimal,
)
from web3.utils.functional import (
    identity,
    compose,
)
import web3.utils.config as config


def isPredefinedBlockNumber(blockNumber):
    if not is_string(blockNumber):
        return False
    return force_text(blockNumber) in {"latest", "pending", "earliest"}


def inputDefaultBlockNumberFormatter(blockNumber=None):
    if not blockNumber:
        return config.defaultBlock

    return inputBlockNumberFormatter(blockNumber)


def inputBlockNumberFormatter(blockNumber):
    if not blockNumber:
        return None
    elif isPredefinedBlockNumber(blockNumber):
        return blockNumber
    return to_hex(blockNumber)


@coerce_args_to_text
@coerce_return_to_text
def input_call_formatter(eth, txn):
    defaults = {
        'from': eth.defaultAccount,
    }
    formatters = {
        'from': input_address_formatter,
        'to': input_address_formatter,
    }
    return {
        key: formatters.get(key, identity)(txn.get(key, defaults.get(key)))
        for key in set(tuple(txn.keys()) + tuple(defaults.keys()))
    }


@coerce_args_to_text
@coerce_return_to_text
def input_transaction_formatter(eth, txn):
    defaults = {
        'from': eth.defaultAccount,
    }
    formatters = {
        'from': input_address_formatter,
        'to': input_address_formatter,
    }
    return {
        key: formatters.get(key, identity)(txn.get(key, defaults.get(key)))
        for key in set(tuple(txn.keys()) + tuple(defaults.keys()))
    }


@coerce_args_to_text
@coerce_return_to_text
def output_transaction_formatter(txn):
    formatters = {
        'blockNumber': lambda v: None if v is None else to_decimal(v),
        'transactionIndex': lambda v: None if v is None else to_decimal(v),
        'nonce': to_decimal,
        'gas': to_decimal,
        'gasPrice': to_decimal,
        'value': to_decimal,
    }

    return {
        key: formatters.get(key, identity)(value)
        for key, value in txn.items()
    }


@coerce_args_to_text
@coerce_return_to_text
def output_transaction_receipt_formatter(receipt):
    """
    Formats the output of a transaction receipt to its proper values
    """
    if receipt is None:
        return None

    logs_formatter = compose(functools.partial(map, outputLogFormatter), list)

    formatters = {
        'blockNumber': to_decimal,
        'transactionIndex': to_decimal,
        'cumulativeGasUsed': to_decimal,
        'gasUsed': to_decimal,
        'logs': lambda l: logs_formatter(l) if is_array(l) else l,
    }

    return {
        key: formatters.get(key, identity)(value)
        for key, value in receipt.items()
    }


@coerce_return_to_text
def outputBlockFormatter(block):
    """
    Formats the output of a block to its proper values
    """

    # Transform to number
    block["gasLimit"] = to_decimal(block["gasLimit"])
    block["gasUsed"] = to_decimal(block["gasUsed"])
    block["size"] = to_decimal(block["size"])
    block["timestamp"] = to_decimal(block["timestamp"])

    if block.get("number"):
        block["number"] = to_decimal(block["number"])

    block["difficulty"] = to_decimal(block["difficulty"])
    block["totalDifficulty"] = to_decimal(block["totalDifficulty"])

    if is_array(block.get("transactions")):
        for item in block["transactions"]:
            if not is_string(item):
                item = output_transaction_formatter(item)

    return block


@coerce_return_to_text
def outputLogFormatter(log):
    """
    Formats the output of a log
    """
    if log.get("blockNumber"):
        log["blockNumber"] = to_decimal(log["blockNumber"])
    if log.get("transactionIndex"):
        log["transactionIndex"] = to_decimal(log["transactionIndex"])
    if log.get("logIndex"):
        log["logIndex"] = to_decimal(log["logIndex"])

    return log


@coerce_return_to_text
def inputPostFormatter(post):
    """
    Formats the input of a whisper post and converts all values to HEX
    """

    post["ttl"] = from_decimal(post["ttl"])
    post["workToProve"] = from_decimal(post.get("workToProve", 0))
    post["priority"] = from_decimal(post["priority"])

    if not is_array(post.get("topics")):
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
        return "0x" + iban.address()
    elif is_strict_address(addr):
        return addr
    elif is_address(addr):
        return "0x" + addr

    raise ValueError("invalid address")


def outputSyncingFormatter(result):
    result["startingBlock"] = to_decimal(result["startingBlock"])
    result["currentBlock"] = to_decimal(result["currentBlock"])
    result["highestBlock"] = to_decimal(result["highestBlock"])

    return result


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
    return transaction_pool_formatter(value, identity)


def syncing_formatter(value):
    if not value:
        return value

    formatters = {
        'startingBlock': to_decimal,
        'currentBlock': to_decimal,
        'highestBlock': to_decimal,
    }

    return {
        key: formatters.get(key, identity)(value)
        for key, value in value.items()
    }
