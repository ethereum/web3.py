import importlib
import logging
import pytest
import sys
from tempfile import (
    gettempdir,
)

from web3.auto import (
    infura,
)
from web3.providers import (
    HTTPProvider,
    IPCProvider,
    WebsocketProvider,
)
from web3.providers.auto import (
    load_provider_from_environment,
)

TEMP_DIR = gettempdir()


@pytest.mark.parametrize(
    'uri, expected_type, expected_attrs',
    (
        ('', type(None), {}),
        ('http://1.2.3.4:5678', HTTPProvider, {'endpoint_uri': 'http://1.2.3.4:5678'}),
        ('https://node.ontheweb.com', HTTPProvider, {'endpoint_uri': 'https://node.ontheweb.com'}),
        pytest.param(
            *('file://%s/file.ipc' % TEMP_DIR, IPCProvider, {'ipc_path': '%s/file.ipc' % TEMP_DIR}),
            marks=pytest.mark.skipif(sys.version_info < (3, 6), reason="path must exist in py3.5"),
        ),
        ('ws://1.2.3.4:5679', WebsocketProvider, {'endpoint_uri': 'ws://1.2.3.4:5679'})
    ),
)
def test_load_provider_from_env(monkeypatch, uri, expected_type, expected_attrs):
    monkeypatch.setenv('WEB3_PROVIDER_URI', uri)
    provider = load_provider_from_environment()
    assert isinstance(provider, expected_type)
    for attr, val in expected_attrs.items():
        assert getattr(provider, attr) == val


@pytest.mark.parametrize('environ_name', ['INFURA_API_KEY', 'WEB3_INFURA_API_KEY'])
def test_web3_auto_infura_empty_key(monkeypatch, caplog, environ_name):
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'https')
    monkeypatch.setenv(environ_name, '')

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 1
    logger, level, msg = caplog.record_tuples[0]
    assert 'WEB3_INFURA_API_KEY' in msg
    assert level == logging.WARNING

    w3 = infura.w3
    assert isinstance(w3.providers[0], HTTPProvider)
    assert getattr(w3.providers[0], 'endpoint_uri') == 'https://mainnet.infura.io/'


@pytest.mark.parametrize('environ_name', ['INFURA_API_KEY', 'WEB3_INFURA_API_KEY'])
def test_web3_auto_infura_deleted_key(monkeypatch, caplog, environ_name):
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'https')
    monkeypatch.delenv(environ_name, raising=False)

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 1
    logger, level, msg = caplog.record_tuples[0]
    assert 'WEB3_INFURA_API_KEY' in msg
    assert level == logging.WARNING

    w3 = infura.w3
    assert isinstance(w3.providers[0], HTTPProvider)
    assert getattr(w3.providers[0], 'endpoint_uri') == 'https://mainnet.infura.io/'


@pytest.mark.parametrize('environ_name', ['INFURA_API_KEY', 'WEB3_INFURA_API_KEY'])
def test_web3_auto_infura(monkeypatch, caplog, environ_name):
    monkeypatch.setenv('WEB3_INFURA_SCHEME', 'https')
    API_KEY = 'aoeuhtns'
    monkeypatch.setenv(environ_name, API_KEY)
    expected_url = 'https://%s/%s' % (infura.INFURA_MAINNET_DOMAIN, API_KEY)

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 0

    w3 = infura.w3
    assert isinstance(w3.providers[0], HTTPProvider)
    assert getattr(w3.providers[0], 'endpoint_uri') == expected_url


def test_web3_auto_infura_websocket_default(caplog):
    importlib.reload(infura)
    assert len(caplog.record_tuples) == 0

    w3 = infura.w3
    assert isinstance(w3.providers[0], WebsocketProvider)
    assert getattr(w3.providers[0], 'endpoint_uri') == 'wss://mainnet.infura.io/ws'
