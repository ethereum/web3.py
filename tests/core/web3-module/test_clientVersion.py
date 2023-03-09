import pytest


def test_web3_clientVersion(web3):
    with pytest.warns(
        DeprecationWarning,
        match='clientVersion is deprecated in favor of client_version'
    ):
        assert web3.clientVersion.startswith("EthereumTester/")
