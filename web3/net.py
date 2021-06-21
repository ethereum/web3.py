from typing import (
    Callable,
    NoReturn,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    DeprecatedMethod,
    Method,
    default_root_munger,
)
from web3.module import (
    Module,
)


class BaseNet(Module):
    _listening: Method[Callable[[], bool]] = Method(
        RPC.net_listening,
        mungers=[default_root_munger],
    )

    _peer_count: Method[Callable[[], int]] = Method(
        RPC.net_peerCount,
        mungers=[default_root_munger],
    )

    _version: Method[Callable[[], str]] = Method(
        RPC.net_version,
        mungers=[default_root_munger],
    )

    @property
    def peer_count(self) -> int:
        return self._peer_count()

    @property
    def version(self) -> str:
        return self._version()

    @property
    def listening(self) -> bool:
        return self._listening()


class Net(BaseNet):
    @property
    def chainId(self) -> NoReturn:
        raise DeprecationWarning("This method has been deprecated in EIP 1474.")

    # @property
    # def listening(self) -> bool:
    #     return self._listening()

    # @property
    # def peer_count(self) -> int:
    #     return self._peer_count()

    # @property
    # def version(self) -> str:
    #     return self._version()

    #
    # Deprecated Methods
    #
    peerCount = DeprecatedMethod(BaseNet.peer_count, 'peerCount', 'peer_count')  # type: ignore


class AsyncNet(BaseNet):
    is_async = True

    # @property
    # def listening(self) -> bool:
    #     return self._listening()

    # @property
    # def peer_count(self) -> int:
    #     return self._peer_count()

    # @property
    # def version(self) -> str:
    #     return self._version()
