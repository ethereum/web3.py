import importlib
import os
import pytest

from eth_utils import (
    ValidationError,
)

from web3.exceptions import (
    InfuraProjectIdNotFound,
)
from web3.providers import (
    HTTPProvider,
    IPCProvider,
    WebsocketProvider,
)
from web3.providers.auto import (
    load_provider_from_environment,
)
from web3.providers.ipc import (
    get_dev_ipc_path,
)

# Ugly hack to import infura now that API KEY is required
os.environ["WEB3_INFURA_PROJECT_ID"] = "test"
from web3.auto import (  # noqa E402 isort:skip
    infura,
)


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
            {"ipc_path": "/root/path/to/file.ipc"},
        ),
        ("ws://1.2.3.4:5679", WebsocketProvider, {"endpoint_uri": "ws://1.2.3.4:5679"}),
    ),
)
def test_load_provider_from_env(monkeypatch, uri, expected_type, expected_attrs):
    monkeypatch.setenv("WEB3_PROVIDER_URI", uri)
    provider = load_provider_from_environment()
    assert isinstance(provider, expected_type)
    for attr, val in expected_attrs.items():
        assert getattr(provider, attr) == val


def test_get_dev_ipc_path(monkeypatch, tmp_path):
    uri = str(tmp_path)
    monkeypatch.setenv("WEB3_PROVIDER_URI", uri)
    path = get_dev_ipc_path()
    assert path == uri


def test_web3_auto_infura_empty_key(monkeypatch):
    monkeypatch.setenv("WEB3_INFURA_SCHEME", "https")
    monkeypatch.setenv("WEB3_INFURA_PROJECT_ID", "")

    with pytest.raises(InfuraProjectIdNotFound):
        importlib.reload(infura)


def test_web3_auto_infura_deleted_key(monkeypatch):
    monkeypatch.setenv("WEB3_INFURA_SCHEME", "https")

    monkeypatch.delenv("WEB3_INFURA_PROJECT_ID", raising=False)

    with pytest.raises(InfuraProjectIdNotFound):
        importlib.reload(infura)


def test_web3_auto_infura_websocket_empty_key(monkeypatch):
    monkeypatch.setenv("WEB3_INFURA_PROJECT_ID", "")

    with pytest.raises(InfuraProjectIdNotFound):
        importlib.reload(infura)


def test_web3_auto_infura_websocket_deleted_key(monkeypatch):
    monkeypatch.delenv("WEB3_INFURA_PROJECT_ID", raising=False)

    with pytest.raises(InfuraProjectIdNotFound):
        importlib.reload(infura)


def test_web3_auto_infura(monkeypatch, caplog):
    monkeypatch.setenv("WEB3_INFURA_SCHEME", "https")
    API_KEY = "aoeuhtns"

    monkeypatch.setenv("WEB3_INFURA_PROJECT_ID", API_KEY)

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 0

    w3 = infura.w3
    assert isinstance(w3.provider, HTTPProvider)
    expected_url = f"https://{infura.INFURA_MAINNET_DOMAIN}/v3/{API_KEY}"
    assert getattr(w3.provider, "endpoint_uri") == expected_url


def test_web3_auto_infura_websocket_default(monkeypatch, caplog):
    monkeypatch.setenv("WEB3_INFURA_SCHEME", "wss")
    API_KEY = "aoeuhtns"
    monkeypatch.setenv("WEB3_INFURA_PROJECT_ID", API_KEY)
    expected_url = f"wss://{infura.INFURA_MAINNET_DOMAIN}/ws/v3/{API_KEY}"

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 0

    w3 = infura.w3
    assert isinstance(w3.provider, WebsocketProvider)
    assert getattr(w3.provider, "endpoint_uri") == expected_url


def test_web3_auto_infura_raises_error_with_nonexistent_scheme(monkeypatch):
    monkeypatch.setenv("WEB3_INFURA_PROJECT_ID", "test")
    monkeypatch.setenv("WEB3_INFURA_SCHEME", "not-a-scheme")

    error_msg = "Cannot connect to Infura with scheme 'not-a-scheme'"
    with pytest.raises(ValidationError, match=error_msg):
        importlib.reload(infura)


def test_web3_auto_infura_websocket_with_secret(monkeypatch):
    monkeypatch.setenv("WEB3_INFURA_PROJECT_ID", "test")
    monkeypatch.setenv("WEB3_INFURA_API_SECRET", "secret")

    importlib.reload(infura)

    w3 = infura.w3
    assert isinstance(w3.provider, WebsocketProvider)
    expected_url = f"wss://:secret@{infura.INFURA_MAINNET_DOMAIN}/ws/v3/test"
    assert getattr(w3.provider, "endpoint_uri") == expected_url


def test_web3_auto_infura_with_secret(monkeypatch):
    monkeypatch.setenv("WEB3_INFURA_SCHEME", "https")
    monkeypatch.setenv("WEB3_INFURA_PROJECT_ID", "test")
    monkeypatch.setenv("WEB3_INFURA_API_SECRET", "secret")

    importlib.reload(infura)

    w3 = infura.w3
    assert isinstance(w3.provider, HTTPProvider)
    expected_url = f"https://{infura.INFURA_MAINNET_DOMAIN}/v3/test"
    expected_auth_value = ("", "secret")
    assert getattr(w3.provider, "endpoint_uri") == expected_url
    assert w3.provider.get_request_kwargs()["auth"] == expected_auth_value
