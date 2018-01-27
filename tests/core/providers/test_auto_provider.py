import pytest

from web3.providers import (
    HTTPProvider,
    IPCProvider,
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
    ),
)
def test_load_provider_from_env(monkeypatch, uri, expected_type, expected_attrs):
    monkeypatch.setenv('WEB3_PROVIDER_URI', uri)
    provider = load_provider_from_environment()
    assert isinstance(provider, expected_type)
    for attr, val in expected_attrs.items():
        assert getattr(provider, attr) == val
