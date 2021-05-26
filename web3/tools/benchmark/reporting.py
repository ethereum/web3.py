from logging import (
    Logger,
)
from typing import (
    Any,
    Dict,
)


def print_header(logger: Logger, num_calls: int) -> None:
    logger.info(
        "|{:^26}|{:^20}|{:^20}|{:^20}|{:^20}|".format(
            f"Method ({num_calls} calls)",
            "HTTPProvider",
            "AsyncHTTProvider",
            "IPCProvider",
            "WebsocketProvider",
        )
    )
    logger.info("-" * 112)


def print_entry(logger: Logger, method_benchmarks: Dict[str, Any],) -> None:
    logger.info(
        "|{:^26}|{:^20.10}|{:^20.10}|{:^20.10}|{:^20.10}|".format(
            method_benchmarks["name"],
            method_benchmarks["HTTPProvider"],
            method_benchmarks["AsyncHTTPProvider"],
            method_benchmarks["IPCProvider"],
            method_benchmarks["WebsocketProvider"],
        )
    )


def print_footer(logger: Logger) -> None:
    logger.info("-" * 112)
