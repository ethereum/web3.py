from web3.method import (
    Method,
)


def content():
    return Method(
        "txpool_content",
        mungers=None,
    )


def inspect():
    return Method(
        "txpool_inspect",
        mungers=None,
    )


def status():
    return Method(
        "txpool_status",
        mungers=None,
    )
