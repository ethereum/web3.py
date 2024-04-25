from typing import (
    Callable,
)

from eth_typing import (
    ChecksumAddress,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    DeprecatedMethod,
    Method,
    default_root_munger,
)
from web3.types import (
    BlockNumber,
    Wei,
)

#
# The Geth client deprecated the miner namespace.
#

_make_dag: Method[Callable[[BlockNumber], bool]] = Method(
    RPC.miner_makeDag,
    mungers=[default_root_munger],
)

make_dag = DeprecatedMethod(_make_dag, msg="All mining methods have been deprecated")

_set_extra: Method[Callable[[str], bool]] = Method(
    RPC.miner_setExtra,
    mungers=[default_root_munger],
)

set_extra = DeprecatedMethod(_set_extra, msg="All mining methods have been deprecated")

_set_etherbase: Method[Callable[[ChecksumAddress], bool]] = Method(
    RPC.miner_setEtherbase,
    mungers=[default_root_munger],
)

set_etherbase = DeprecatedMethod(
    _set_etherbase, msg="All mining methods have been deprecated"
)

_set_gas_price: Method[Callable[[Wei], bool]] = Method(
    RPC.miner_setGasPrice,
    mungers=[default_root_munger],
)

set_gas_price = DeprecatedMethod(
    _set_gas_price, msg="All mining methods have been deprecated"
)

_start: Method[Callable[[int], bool]] = Method(
    RPC.miner_start,
    mungers=[default_root_munger],
)

start = DeprecatedMethod(_start, msg="All mining methods have been deprecated")

_stop: Method[Callable[[], bool]] = Method(
    RPC.miner_stop,
    is_property=True,
)

stop = DeprecatedMethod(_stop, msg="All mining methods have been deprecated")

_start_auto_dag: Method[Callable[[], bool]] = Method(
    RPC.miner_startAutoDag,
    is_property=True,
)

start_auto_dag = DeprecatedMethod(
    _start_auto_dag, msg="All mining methods have been deprecated"
)

_stop_auto_dag: Method[Callable[[], bool]] = Method(
    RPC.miner_stopAutoDag,
    is_property=True,
)

stop_auto_dag = DeprecatedMethod(
    _stop_auto_dag, msg="All mining methods have been deprecated"
)
