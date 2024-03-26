import pytest

from tests.integration.common import (
    COINBASE,
)
from tests.utils import (
    get_open_port,
)


@pytest.fixture(scope="module")
def ws_port():
    return get_open_port()


@pytest.fixture(scope="module")
def endpoint_uri(ws_port):
    return f"ws://localhost:{ws_port}"


def _geth_command_arguments(ws_port, base_geth_command_arguments, geth_version):
    yield from base_geth_command_arguments
    if geth_version.major == 1:
        yield from (
            "--miner.etherbase",
            COINBASE[2:],
            "--ws",
            "--ws.port",
            ws_port,
            "--ws.api",
            "admin,eth,net,web3",
            "--ws.origins",
            "*",
            "--ipcdisable",
        )
        if geth_version.minor not in [13, 14]:
            raise AssertionError("Unsupported Geth version")
    else:
        raise AssertionError("Unsupported Geth version")


@pytest.fixture(scope="module")
def geth_command_arguments(
    geth_binary, get_geth_version, datadir, ws_port, base_geth_command_arguments
):
    return _geth_command_arguments(
        ws_port, base_geth_command_arguments, get_geth_version
    )
