import argparse
import asyncio
from collections import (
    defaultdict,
)
import logging
import sys
import timeit
from typing import (
    Any,
    Callable,
    Dict,
    Union,
)

from eth_typing import (
    ChecksumAddress,
)

from web3 import (
    AsyncHTTPProvider,
    HTTPProvider,
    Web3,
)
from web3.eth import (
    AsyncEth,
    Eth,
)
from web3.middleware import (
    async_buffered_gas_estimate_middleware,
    async_gas_price_strategy_middleware,
    buffered_gas_estimate_middleware,
    gas_price_strategy_middleware,
)
from web3.tools.benchmark.node import (
    GethBenchmarkFixture,
)
from web3.tools.benchmark.reporting import (
    print_entry,
    print_footer,
    print_header,
)
from web3.tools.benchmark.utils import (
    wait_for_aiohttp,
    wait_for_http,
)
from web3.types import (
    Wei,
)

KEYFILE_PW = 'web3py-test'

parser = argparse.ArgumentParser()
parser.add_argument(
    "--num-calls", type=int, default=10, help="The number of RPC calls to make",
)

# TODO - layers to test:
# contract.functions.method(...).call()
# w3.eth.call(...)
# HTTPProvider.make_request(...)


def build_web3_http(endpoint_uri: str) -> Web3:
    wait_for_http(endpoint_uri)
    _web3 = Web3(
        HTTPProvider(endpoint_uri),
        middlewares=[gas_price_strategy_middleware, buffered_gas_estimate_middleware]
    )
    return _web3


async def build_async_w3_http(endpoint_uri: str) -> Web3:
    await wait_for_aiohttp(endpoint_uri)
    _web3 = Web3(
        AsyncHTTPProvider(endpoint_uri),  # type: ignore
        middlewares=[async_gas_price_strategy_middleware, async_buffered_gas_estimate_middleware],
        modules={"eth": (AsyncEth,)},
    )
    return _web3


def sync_benchmark(func: Callable[..., Any], n: int) -> Union[float, str]:
    try:
        starttime = timeit.default_timer()
        for _ in range(n):
            func()
        endtime = timeit.default_timer()
        execution_time = endtime - starttime
        return execution_time
    except Exception:
        return "N/A"


async def async_benchmark(func: Callable[..., Any], n: int) -> Union[float, str]:
    try:
        starttime = timeit.default_timer()
        for result in asyncio.as_completed([func() for _ in range(n)]):
            await result
        execution_time = timeit.default_timer() - starttime
        return execution_time
    except Exception:
        return "N/A"


def unlocked_account(w3: "Web3") -> ChecksumAddress:
    w3.geth.personal.unlock_account(w3.eth.coinbase, KEYFILE_PW)
    return w3.eth.coinbase


async def async_unlocked_account(w3: Web3, w3_eth: Eth) -> ChecksumAddress:
    # change w3_eth type to w3_eth: AsyncEth once AsyncEth reflects Eth
    coinbase = await w3_eth.coinbase  # type: ignore
    w3.geth.personal.unlock_account(coinbase, KEYFILE_PW)
    return coinbase


def main(logger: logging.Logger, num_calls: int) -> None:
    fixture = GethBenchmarkFixture()
    for built_fixture in fixture.build():
        for process in built_fixture:
            w3_http = build_web3_http(fixture.endpoint_uri)
            loop = asyncio.get_event_loop()
            async_w3_http = loop.run_until_complete(build_async_w3_http(fixture.endpoint_uri))
            # TODO: swap out w3_http for the async_w3_http once GethPersonal module is async
            async_unlocked_acct = loop.run_until_complete(
                async_unlocked_account(w3_http, async_w3_http.eth)
            )

            methods = [
                {
                    "name": "eth_gasPrice",
                    "params": {},
                    "exec": lambda: w3_http.eth.gas_price,
                    "async_exec": lambda: async_w3_http.eth.gas_price,
                },
                {
                    "name": "eth_sendTransaction",
                    "params": {},
                    "exec": lambda: w3_http.eth.send_transaction({
                        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
                        'from': unlocked_account(w3_http),
                        'value': Wei(12345),
                    }),
                    "async_exec": lambda: async_w3_http.eth.send_transaction({
                        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
                        'from': async_unlocked_acct,
                        'value': Wei(12345)
                    }),
                },
                {
                    "name": "eth_blockNumber",
                    "params": {},
                    "exec": lambda: w3_http.eth.block_number,
                    "async_exec": lambda: async_w3_http.eth.block_number,
                },
                {
                    "name": "eth_getBlock",
                    "params": {},
                    "exec": lambda: w3_http.eth.get_block(1),
                    "async_exec": lambda: async_w3_http.eth.get_block(1),
                },
            ]

            def benchmark(method: Dict[str, Any]) -> None:
                outcomes: Dict[str, Union[str, float]] = defaultdict(lambda: "N/A")
                outcomes["name"] = method["name"]
                outcomes["HTTPProvider"] = sync_benchmark(method["exec"], num_calls,)
                outcomes["AsyncHTTPProvider"] = loop.run_until_complete(
                    async_benchmark(method["async_exec"], num_calls)
                )
                print_entry(logger, outcomes)

            print_header(logger, num_calls)

            for method in methods:
                benchmark(method)

            print_footer(logger)


if __name__ == "__main__":
    args = parser.parse_args()

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(sys.stdout))

    main(logger, args.num_calls)
