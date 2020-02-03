import importlib
import os
import pytest

from eth_utils import (
    ValidationError,
)

from web3.exceptions import (
    InfuraKeyNotFound,
)
from web3.providers import (
    HTTPProvider,
    IPCProvider,
    WebsocketProvider,
)
from web3.providers.auto import (
    load_provider_from_environment,
)

# Ugly hack to import infura now that API KEY is required
os.environ['WEB3_INFURA_API_KEY'] = 'test'
from web3.auto import (  # noqa E402 isort:skip
    infura,
)


@pytest.fixture(autouse=True)
def delete_environment_variables(monkeypatch):
    monkeypatch.delenv('WEB3_INFURA_PROJECT_ID', raising=False)
    monkeypatch.delenv('WEB3_INFURA_API_KEY', raising=False)
    monkeypatch.delenv('WEB3_INFURA_API_SECRET', raising=False)
    monkeypatch.delenv('WEB3_INFURA_SCHEME', raising=False)


@pytest.mark.parametrize(
    'uri, expected_type, expected_attrs',
    (
        ('', type(None), {}),
        ('http://1.2.3.4:5678', HTTPProvider, {'endpoint_uri': 'http://1.2.3.4:5678'}),
        ('https://node.ontheweb.com', HTTPProvider, {'endpoint_uri': 'https://node.ontheweb.com'}),
        ('file:///root/path/to/file.ipc', IPCProvider, {'ipc_path': '/root/path/to/file.ipc'}),
        ('ws://1.2.3.4:5679', WebsocketProvider, {'endpoint_uri': 'ws://1.2.3.4:5679'})
    ),
)
def test_load_provider_from_env(monkeypatch, uri, expected_type, expected_attrs):
    monkeypatch.setenv('WEB3_PROVIDER_URI', uri)
    provider = load_provider_from_environment()
    assert isinstance(provider, expected_type)
    for attr, val in expected_attrs.items():
        assert getattr(provider, attr) == val


@pytest.mark.parametrize('environ_name', ['WEB3_INFURA_API_KEY', 'WEB3_INFURA_PROJECT_ID'])
def test_web3_auto_infura_empty_key(monkeypatch, caplog, environ_name):
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'https')
    monkeypatch.setenv(environ_name, '')

    with pytest.raises(InfuraKeyNotFound):
        importlib.reload(infura)


@pytest.mark.parametrize('environ_name', ['WEB3_INFURA_API_KEY', 'WEB3_INFURA_PROJECT_ID'])
def test_web3_auto_infura_deleted_key(monkeypatch, caplog, environ_name):
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'https')

    monkeypatch.delenv(environ_name, raising=False)

    with pytest.raises(InfuraKeyNotFound):
        importlib.reload(infura)


@pytest.mark.parametrize('environ_name', ['WEB3_INFURA_API_KEY', 'WEB3_INFURA_PROJECT_ID'])
def test_web3_auto_infura_websocket_empty_key(monkeypatch, caplog, environ_name):
    monkeypatch.setenv(environ_name, '')

    with pytest.raises(InfuraKeyNotFound):
        importlib.reload(infura)


@pytest.mark.parametrize('environ_name', ['WEB3_INFURA_API_KEY', 'WEB3_INFURA_PROJECT_ID'])
def test_web3_auto_infura_websocket_deleted_key(monkeypatch, caplog, environ_name):
    monkeypatch.delenv(environ_name, raising=False)

    with pytest.raises(InfuraKeyNotFound):
        importlib.reload(infura)


@pytest.mark.parametrize('environ_name', ['WEB3_INFURA_API_KEY', 'WEB3_INFURA_PROJECT_ID'])
def test_web3_auto_infura(monkeypatch, caplog, environ_name):
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'https')
    API_KEY = 'aoeuhtns'

    monkeypatch.setenv(environ_name, API_KEY)

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 0

    w3 = infura.w3
    assert isinstance(w3.provider, HTTPProvider)
    expected_url = 'https://%s/v3/%s' % (infura.INFURA_MAINNET_DOMAIN, API_KEY)
    assert getattr(w3.provider, 'endpoint_uri') == expected_url


@pytest.mark.parametrize('environ_name', ['WEB3_INFURA_API_KEY', 'WEB3_INFURA_PROJECT_ID'])
def test_web3_auto_infura_websocket_default(monkeypatch, caplog, environ_name):
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'wss')
    API_KEY = 'aoeuhtns'
    monkeypatch.setenv(environ_name, API_KEY)
    expected_url = 'wss://%s/ws/v3/%s' % (infura.INFURA_MAINNET_DOMAIN, API_KEY)

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 0

    w3 = infura.w3
    assert isinstance(w3.provider, WebsocketProvider)
    assert getattr(w3.provider, 'endpoint_uri') == expected_url


def test_web3_auto_infura_raises_error_with_nonexistent_scheme(monkeypatch):
    monkeypatch.setenv('WEB3_INFURA_API_KEY', 'test')
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'not-a-scheme')

    error_msg = "Cannot connect to Infura with scheme 'not-a-scheme'"
    with pytest.raises(ValidationError, match=error_msg):
        importlib.reload(infura)


@pytest.mark.parametrize('environ_name', ['WEB3_INFURA_API_KEY', 'WEB3_INFURA_PROJECT_ID'])
def test_web3_auto_infura_websocket_with_secret(monkeypatch, caplog, environ_name):
    monkeypatch.setenv(environ_name, 'test')
    monkeypatch.setenv('WEB3_INFURA_API_SECRET', 'secret')

    importlib.reload(infura)

    w3 = infura.w3
    assert isinstance(w3.provider, WebsocketProvider)
    expected_url = 'wss://:secret@%s/ws/v3/test' % (infura.INFURA_MAINNET_DOMAIN)
    assert getattr(w3.provider, 'endpoint_uri') == expected_url


@pytest.mark.parametrize('environ_name', ['WEB3_INFURA_API_KEY', 'WEB3_INFURA_PROJECT_ID'])
def test_web3_auto_infura_with_secret(monkeypatch, caplog, environ_name):
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'https')
    monkeypatch.setenv(environ_name, 'test')
    monkeypatch.setenv('WEB3_INFURA_API_SECRET', 'secret')

    importlib.reload(infura)

    w3 = infura.w3
    assert isinstance(w3.provider, HTTPProvider)
    expected_url = 'https://%s/v3/test' % (infura.INFURA_MAINNET_DOMAIN)
    expected_auth_value = ('', 'secret')
    assert getattr(w3.provider, 'endpoint_uri') == expected_url
    assert w3.provider.get_request_kwargs()['auth'] == expected_auth_value
