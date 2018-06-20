import pytest

from web3.auto.gethdev import (
    w3 as w3_gethdev,
)
from web3.auto.infura import (
    w3 as w3_infura,
)
from web3.providers import (
    HTTPProvider,
    IPCProvider,
    WebsocketProvider,
)
from web3.providers.auto import (
    INFURA_MAINNET_HTTP_URL,
    load_gethdev_ipc_provider,
    load_infura_mainnet_http_provider,
    load_provider_from_environment,
)


@pytest.mark.parametrize(
    'uri, expected_type, expected_attrs',
    (
        ('', type(None), {}),
        ('http://1.2.3.4:5678', HTTPProvider, {'endpoint_uri': 'http://1.2.3.4:5678'}),
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


def test_load_infura_provider():
    provider = load_infura_mainnet_http_provider()
    assert isinstance(provider, HTTPProvider)
    assert getattr(provider, 'endpoint_uri') == INFURA_MAINNET_HTTP_URL


def test_load_gethdev_provider():
    provider = load_gethdev_ipc_provider()
    assert isinstance(provider, IPCProvider)


def test_web3_auto_infura():
    assert isinstance(w3_infura.providers[0], HTTPProvider)
    assert getattr(w3_infura.providers[0], 'endpoint_uri') == INFURA_MAINNET_HTTP_URL


def test_web3_auto_gethdev():
    assert isinstance(w3_gethdev.providers[0], IPCProvider)
