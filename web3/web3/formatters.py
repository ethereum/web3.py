import web3.utils.address as address
import web3.utils.encoding as encoding
import web3.utils.utils as utils
import web3.utils.config as config
from web3.web3.iban import Iban

fromDecimal = encoding.fromDecimal
toDecimal = encoding.toDecimal


def isPredefinedBlockNumber(blockNumber):
    return blockNumber in ["latest", "pending", "earliest"]


def inputDefaultBlockNumberFormatter(blockNumber=None):
    if not blockNumber:
        return config.defaultBlock

    return inputBlockNumberFormatter(blockNumber)


def inputBlockNumberFormatter(blockNumber):
    if not blockNumber:
        return None
    elif isPredefinedBlockNumber(blockNumber):
        return blockNumber
    return encoding.toHex(blockNumber)


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
            options[key] = encoding.fromDecimal(options[key])

    return options


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
            options[key] = encoding.fromDecimal(options[key])

    return options


def outputTransactionFormatter(tx):
    """
    Formats the output of a transaction to its proper values
    """
    if tx.get("blockNumber"):
        tx["blockNumber"] = toDecimal(tx["blockNumber"])
    if tx.get("transactionIndex"):
        tx["transactionIndex"] = toDecimal(tx["transactionIndex"])

    tx["nonce"] = toDecimal(tx["nonce"])
    tx["gas"] = toDecimal(tx["gas"])
    tx["gasPrice"] = toDecimal(tx["gasPrice"])
    tx["value"] = toDecimal(tx["value"])
    return tx


def outputTransactionReceiptFormatter(receipt):
    """
    Formats the output of a transaction receipt to its proper values
    """
    if receipt is None:
        return None

    if receipt.get("blockNumber"):
        receipt["blockNumber"] = toDecimal(receipt["blockNumber"])
    if receipt.get("transactionIndex"):
        receipt["transactionIndex"] = toDecimal(receipt["transactionIndex"])
    receipt["cumulativeGasUsed"] = toDecimal(receipt["cumulativeGasUsed"])
    receipt["gasUsed"] = toDecimal(receipt["gasUsed"])

    if utils.isArray(receipt.get("logs")):
        receipt["logs"] = [outputLogFormatter(log) for log in receipt["logs"]]

    return receipt


def outputBlockFormatter(block):
    """
    Formats the output of a block to its proper values
    """

    # Transform to number
    block["gasLimit"] = toDecimal(block["gasLimit"])
    block["gasUsed"] = toDecimal(block["gasUsed"])
    block["size"] = toDecimal(block["size"])
    block["timestamp"] = toDecimal(block["timestamp"])

    if block.get("number"):
        block["number"] = toDecimal(block["number"])

    block["difficulty"] = toDecimal(block["difficulty"])
    block["totalDifficulty"] = toDecimal(block["totalDifficulty"])

    if utils.isArray(block.get("transactions")):
        for item in block["transactions"]:
            if not utils.isString(item):
                item = outputTransactionFormatter(item)

    return block


def outputLogFormatter(log):
    """
    Formats the output of a log
    """
    if log.get("blockNumber"):
        log["blockNumber"] = toDecimal(log["blockNumber"])
    if log.get("transactionIndex"):
        log["transactionIndex"] = toDecimal(log["transactionIndex"])
    if log.get("logIndex"):
        log["logIndex"] = toDecimal(log["logIndex"])

    return log


def inputPostFormatter(post):
    """
    Formats the input of a whisper post and converts all values to HEX
    """

    post["ttl"] = fromDecimal(post["ttl"])
    post["workToProve"] = fromDecimal(post.get("workToProve", 0))
    post["priority"] = fromDecimal(post["priority"])

    if not utils.isArray(post.get("topics")):
        post["topics"] = [post["topics"]] if post.get("topics") else []

    post["topics"] = [topic if topic.startswith("0x") else encoding.fromUtf8(topic)
                      for topic in post["topics"]]

    return post


def outputPostFormatter(post):
    """
    Formats the output of a received post message
    """

    post["expiry"] = toDecimal(post["expiry"])
    post["sent"] = toDecimal(post["sent"])
    post["ttl"] = toDecimal(post["ttl"])
    post["workProved"] = toDecimal(post["workProved"])

    if not post.get("topics"):
        post["topics"] = []

    post["topics"] = [encoding.toAscii(topic) for topic in post["topics"]]

    return post


def inputAddressFormatter(addr):
    iban = Iban(addr)
    if iban.isValid() and iban.isDirect():
        return "0x" + iban.address()
    elif address.isStrictAddress(addr):
        return addr
    elif address.isAddress(addr):
        return "0x" + addr

    raise ValueError("invalid address")


def outputSyncingFormatter(result):
    result["startingBlock"] = toDecimal(result["startingBlock"])
    result["currentBlock"] = toDecimal(result["currentBlock"])
    result["highestBlock"] = toDecimal(result["highestBlock"])

    return result
