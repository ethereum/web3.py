from ..utils import encoding
from ..utils import utils
from ..utils import config
from iban import iban


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

    options["from"] = options.get("from") or config["defaultAccount"]

    if options.get("from"):
        options["from"] = inputAddressFormatter(options["from"])

    if options.get("to"):
        options["to"] = inputAddressFormatter(options["to"])

    for key in ["gasPrice", "gas", "value", "nonce"]:
        if key in options:
            options[key] = encoding.fromDecimal(options[key])

    return options


def inputTransactionFormatter(options):
    """
    Formats the input of a transaction and converts all values to HEX
    """
    options["from"] = options.get("from") or config["defaultAccount"]
    options["from"] = inputAddressFormatter(options["from"])

    if options.get("to"):
        options["to"] = inputAddressFormatter(options["to"])

    for key in ["gasPrice", "gas", "value", "nonce"]:
        if key in options:
            options[key] = encoding.fromDecimal(options[key])

    return options


def outputTransactionFormatter(tx):
    """
    Formats the output of a transaction to its proper values
    """
    if tx.get("blockNumber"):
        tx["blockNumber"] = int(tx["blockNumber"])
    if tx.get("transactionIndex"):
        tx["transactionIndex"] = int(tx["transactionIndex"])

    tx["nonce"] = int(tx["nonce"])
    tx["gas"] = int(tx["gas"])
    tx["gasPrice"] = long(tx["gasPrice"])
    tx["value"] = long(tx["value"])
    return tx


def outputTransactionReceiptFormatter(receipt):
    """
    Formats the output of a transaction receipt to its proper values
    """
    if receipt.get("blockNumber"):
        receipt["blockNumber"] = int(receipt["blockNumber"])
    if receipt.get("transactionIndex"):
        receipt["transactionIndex"] = int(receipt["transactionIndex"])
    receipt["cumulativeGasUsed"] = int(receipt["cumulativeGasUsed"])
    receipt["gasUsed"] = int(receipt["gasUsed"])

    if utils.isArray(receipt.get("logs")):
        receipt["logs"] = [outputLogFormatter(log) for log in receipt["logs"]]

    return receipt


def outputBlockFormatter(block):
    """
    Formats the output of a block to its proper values
    """

    # Transform to number
    block["gasLimit"] = int(block["gasLimit"])
    block["gasUsed"] = int(block["gasUsed"])
    block["size"] = int(block["size"])
    block["timestamp"] = int(block["timestamp"])

    if block.get("number"):
        block["number"] = int(block["number"])

    block["difficulty"] = int(block["difficulty"])
    block["totalDifficulty"] = int(block["totalDifficulty"])

    if utils.isArray(block.get("transactions")):
        for item in block["transactions"]:
            #WTF?!

    return block


def outputLogFormatter(log):
    """
    Formats the output of a log
    """
    if log.get("blockNumber"):
        log["blockNumber"] = int(log["blockNumber"])
    if log.get("transactionIndex"):
        log["transactionIndex"] = int(log["transactionIndex"])
    if log.get("logIndex"):
        log["logIndex"] = int(log["logIndex"])

    return log


def inputPostFormatter(post):
    """
    Formats the input of a whisper post and converts all values to HEX
    """

    post["ttl"] = int(post["ttl"])
    post["workToProve"] = int(post["workToProve"])
    post["priority"] = int(post["priority"])

    if not utils.isArray(post.get("topics")):
        post["topics"] = [post["topics"]] if post.get("topics") else []

    post["topics"] = [topic if topic.startswith("0x") else encoding.fromUtf8(topic)
                      for topic in post["topics"]]

    return post


def outputPostFormatter(post):
    """
    Formats the output of a received post message
    """

    post["expiry"] = int(post["expiry"])
    post["sent"] = int(post["sent"])
    post["ttl"] = int(post["ttl"])
    post["workProved"] = int(post["workProved"])

    if not post.get("topics"):
        post["topics"] = []

    post["topics"] = [encoding.toAscii(topic) for topic in post["topics"]]

    return post


def inputAddressFormatter(address):
    iban = Iban(address)
    if iban.isValid() and iban.isDirect():
        return "0x" + iban.address()
    elif address.isStrictAddress(address):
        return address
    elif address.isAddress(address):
        return "0x" + address

    raise Exception("invalid address")


def outputSyncingFormatter(result):
    result["startingBlock"] = int(result["startingBlock"])
    result["currentBlock"] = int(result["currentBlock"])
    result["highestBlock"] = int(result["highestBlock"])

    return result
