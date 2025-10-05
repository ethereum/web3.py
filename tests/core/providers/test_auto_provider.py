import pytest
import os
import sys
import tempfile

from faster_web3.providers import (
    HTTPProvider,
    IPCProvider,
    LegacyWebSocketProvider,
)
from faster_web3.providers.auto import (
    load_provider_from_environment,
)
from faster_web3.providers.ipc import (
    get_dev_ipc_path,
)

# Ugly hack to import infura now that API KEY is required
os.environ["WEB3_INFURA_PROJECT_ID"] = "test"


@pytest.fixture(autouse=True)
def delete_environment_variables(monkeypatch):
    monkeypatch.delenv("WEB3_INFURA_PROJECT_ID", raising=False)
    monkeypatch.delenv("WEB3_INFURA_API_SECRET", raising=False)
    monkeypatch.delenv("WEB3_INFURA_SCHEME", raising=False)


@pytest.mark.parametrize(
    "uri, expected_type, expected_attrs",
    (
        ("", type(None), {}),
        ("http://1.2.3.4:5678", HTTPProvider, {"endpoint_uri": "http://1.2.3.4:5678"}),
        (
            "https://node.ontheweb.com",
            HTTPProvider,
            {"endpoint_uri": "https://node.ontheweb.com"},
        ),
        (
            "file:///root/path/to/file.ipc",
            IPCProvider,
            {"ipc_path": "D:\\root\\path\\to\\file.ipc" if sys.platform.startswith("win") else "/root/path/to/file.ipc"},
        ),
        (
            "ws://1.2.3.4:5679",
            LegacyWebSocketProvider,
            {"endpoint_uri": "ws://1.2.3.4:5679"},
        ),
    ),
)
def test_load_provider_from_env(monkeypatch, uri, expected_type, expected_attrs):
    monkeypatch.setenv("WEB3_PROVIDER_URI", uri)
    provider = load_provider_from_environment()
    assert isinstance(provider, expected_type)
    for attr, val in expected_attrs.items():
        assert getattr(provider, attr) == val


def test_get_dev_ipc_path(monkeypatch, tmp_path):
    # test default path (portable)
    path = get_dev_ipc_path()
    expected = (
        "\\\\.\pipe\geth.ipc"
        if sys.platform.startswith("win")
        else os.path.join(tempfile.gettempdir(), "geth.ipc")
    )
    assert path == expected

    uri = str(tmp_path) + "/geth.ipc"

    # test setting the "TMPDIR" environment variable
    monkeypatch.setenv("TMPDIR", str(tmp_path))
    path = get_dev_ipc_path()
    assert path == uri
    monkeypatch.delenv("TMPDIR")  # reset

    # test with WEB3_PROVIDER_URI set
    monkeypatch.setenv("WEB3_PROVIDER_URI", uri)
    path = get_dev_ipc_path()
    assert path == uri
