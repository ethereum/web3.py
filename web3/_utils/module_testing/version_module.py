from eth_utils import (
    is_string,
)


class VersionModuleTest:
    def test_eth_protocolVersion(self, web3):
        protocol_version = web3.version.ethereum

        assert is_string(protocol_version)
        assert protocol_version.isdigit()
