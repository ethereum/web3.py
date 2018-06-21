import importlib
import logging
import pytest

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


def test_web3_auto_infura_empty_key(monkeypatch, caplog):
    monkeypatch.setenv('INFURA_API_KEY', '')

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 1
    logger, level, msg = caplog.record_tuples[0]
    assert 'INFURA_API_KEY' in msg
    assert level == logging.WARNING

    w3 = infura.w3
    assert isinstance(w3.providers[0], HTTPProvider)
    assert getattr(w3.providers[0], 'endpoint_uri') == infura.INFURA_MAINNET_BASE_URL


def test_web3_auto_infura_missing_key(monkeypatch, caplog):
    monkeypatch.delenv('INFURA_API_KEY', raising=False)

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 1
    logger, level, msg = caplog.record_tuples[0]
    assert 'INFURA_API_KEY' in msg
    assert level == logging.WARNING

    w3 = infura.w3
    assert isinstance(w3.providers[0], HTTPProvider)
    assert getattr(w3.providers[0], 'endpoint_uri') == infura.INFURA_MAINNET_BASE_URL


def test_web3_auto_infura(monkeypatch, caplog):
    API_KEY = 'aoeuhtns'
    monkeypatch.setenv('INFURA_API_KEY', API_KEY)
    expected_url = '%s/%s' % (infura.INFURA_MAINNET_BASE_URL, API_KEY)

    importlib.reload(infura)
    assert len(caplog.record_tuples) == 0

    w3 = infura.w3
    assert isinstance(w3.providers[0], HTTPProvider)
    assert getattr(w3.providers[0], 'endpoint_uri') == expected_url
