import pytest
from typing import (
    TYPE_CHECKING,
)

from eth_utils import (
    is_string,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class VersionModuleTest:
    def test_eth_protocol_version(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            protocol_version = web3.eth.protocol_version

        assert is_string(protocol_version)
        assert protocol_version.isdigit()

    def test_eth_protocolVersion(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            protocol_version = web3.eth.protocolVersion

        assert is_string(protocol_version)
        assert protocol_version.isdigit()
