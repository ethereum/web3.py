from typing import (
    NoReturn,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    Method,
)
from web3.module import (
    Module,
    ModuleV2,
)


class BaseVersion(ModuleV2):
    retrieve_caller_fn = None

    _get_node_version = Method(RPC.web3_clientVersion)
    _get_protocol_version = Method(RPC.eth_protocolVersion)

    @property
    def api(self) -> str:
        from web3 import __version__
        return __version__


class AsyncVersion(BaseVersion):
    is_async = True

    @property
    async def node(self) -> str:
        return await self._get_node_version()

    @property
    async def ethereum(self) -> int:
        return await self._get_protocol_version()


class BlockingVersion(BaseVersion):
    @property
    def node(self) -> str:
        return self._get_node_version()

    @property
    def ethereum(self) -> int:
        return self._get_protocol_version()


class Version(Module):
    @property
    def api(self) -> NoReturn:
        raise DeprecationWarning(
            "This method has been deprecated ... Please use web3.api instead."
        )

    @property
    def node(self) -> NoReturn:
        raise DeprecationWarning(
            "This method has been deprecated ... Please use web3.clientVersion instead."
        )

    @property
    def ethereum(self) -> NoReturn:
        raise DeprecationWarning(
            "This method has been deprecated ... Please use web3.eth.protocolVersion instead."
        )
