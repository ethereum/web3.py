import pytest

from tests.integration.common import (
    COINBASE,
)


def _geth_command_arguments(base_geth_command_arguments, geth_version):
    yield from base_geth_command_arguments
    if geth_version.major == 1:
        yield from (
            "--miner.etherbase",
            COINBASE[2:],
            "--ws",
            "--ws.port",
            "0",
            "--ws.api",
            "admin,debug,eth,net,web3",
            "--ws.origins",
            "*",
            "--ipcdisable",
        )
        if geth_version.minor not in [13, 14, 15, 16]:
            # TODO: remove support for 13 + 14 in the next major release
            raise AssertionError("Unsupported Geth version")
    else:
        raise AssertionError("Unsupported Geth version")


@pytest.fixture
def geth_command_arguments(
    geth_binary, get_geth_version, datadir, base_geth_command_arguments
):
    return _geth_command_arguments(base_geth_command_arguments, get_geth_version)
