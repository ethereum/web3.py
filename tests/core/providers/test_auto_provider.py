import pytest

from web3.auto.infura import (
    INFURA_MAINNET_HTTP_URL,
    w3,
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


def test_web3_auto_infura():
    assert isinstance(w3.providers[0], HTTPProvider)
    assert getattr(w3.providers[0], 'endpoint_uri') == INFURA_MAINNET_HTTP_URL
