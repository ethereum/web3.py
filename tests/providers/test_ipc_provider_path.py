# tests/providers/test_ipc_provider_path.py
from pathlib import Path
import pytest
from web3.providers.ipc import IPCProvider

@pytest.mark.parametrize("as_str", [False, True])
def test_ipcprovider_accepts_str_and_path(tmp_path, as_str):
    p = tmp_path / "dummy.ipc"
    arg = str(p) if as_str else p  # Test both str and Path inputs
    provider = IPCProvider(ipc_path=arg)
    assert isinstance(provider, IPCProvider)


def test_ipcprovider_accepts_path_object(tmp_path):
    # Test both str and Path inputs
    dummy = tmp_path / "dummy.ipc"

    provider1 = IPCProvider(ipc_path=dummy)        # Path object
    provider2 = IPCProvider(ipc_path=str(dummy))   # str

    assert isinstance(provider1, IPCProvider)
    assert isinstance(provider2, IPCProvider)
