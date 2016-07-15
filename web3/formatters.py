from __future__ import absolute_import

from web3.iban import Iban

from web3.utils.string import (
    force_text,
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


@coerce_return_to_text
def inputCallFormatter(options):
    """
    Formats the input of a transaction and converts all values to HEX
    """

    options.setdefault("from", config.defaultAccount)

    if options.get("from"):
        options["from"] = inputAddressFormatter(options["from"])

    if options.get("to"):
        options["to"] = inputAddressFormatter(options["to"])

    for key in ("gasPrice", "gas", "value", "nonce"):
        if key in options:
            options[key] = from_decimal(options[key])

    return options


@coerce_return_to_text
def inputTransactionFormatter(options):
    """
    Formats the input of a transaction and converts all values to HEX
    """
    options.setdefault("from", config.defaultAccount)
    options["from"] = inputAddressFormatter(options["from"])

    if options.get("to"):
        options["to"] = inputAddressFormatter(options["to"])

    for key in ("gasPrice", "gas", "value", "nonce"):
        if key in options:
            options[key] = from_decimal(options[key])

    return options


@coerce_return_to_text
def outputTransactionFormatter(tx):
    """
    Formats the output of a transaction to its proper values
    """
    if tx.get("blockNumber"):
        tx["blockNumber"] = to_decimal(tx["blockNumber"])
    if tx.get("transactionIndex"):
        tx["transactionIndex"] = to_decimal(tx["transactionIndex"])

    tx["nonce"] = to_decimal(tx["nonce"])
    tx["gas"] = to_decimal(tx["gas"])
    tx["gasPrice"] = to_decimal(tx["gasPrice"])
    tx["value"] = to_decimal(tx["value"])
    return tx


@coerce_return_to_text
def outputTransactionReceiptFormatter(receipt):
    """
    Formats the output of a transaction receipt to its proper values
    """
    if receipt is None:
        return None

    if receipt.get("blockNumber"):
        receipt["blockNumber"] = to_decimal(receipt["blockNumber"])
    if receipt.get("transactionIndex"):
        receipt["transactionIndex"] = to_decimal(receipt["transactionIndex"])
    receipt["cumulativeGasUsed"] = to_decimal(receipt["cumulativeGasUsed"])
    receipt["gasUsed"] = to_decimal(receipt["gasUsed"])

    if is_array(receipt.get("logs")):
        receipt["logs"] = [outputLogFormatter(log) for log in receipt["logs"]]

    return receipt


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
                item = outputTransactionFormatter(item)

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


def inputAddressFormatter(addr):
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
