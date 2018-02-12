from eth_utils import (
    is_string,
)


class VersionModuleTest:
    def test_net_version(self, web3):
        version = web3.version.network

        assert is_string(version)
        assert version.isdigit()

    def test_eth_protocolVersion(self, web3):
        protocol_version = web3.version.ethereum

        assert is_string(protocol_version)
        assert protocol_version.isdigit()
