from contextlib import contextmanager
import os
import pytest

from web3.providers.auto import (
    load_provider_from_environment,
)
from web3.providers import (
    IPCProvider,
    HTTPProvider,
)


@contextmanager
def env(name, tempval):
    oldval = os.environ.get(name, None)
    os.environ[name] = tempval
    try:
        yield
    finally:
        if oldval is None:
            del os.environ[name]
        else:
            os.environ[name] = oldval


@pytest.mark.parametrize(
    'uri, expected_type, expected_attrs',
    (
        ('', type(None), {}),
        ('http://1.2.3.4:5678', HTTPProvider, {'endpoint_uri': 'http://1.2.3.4:5678'}),
        ('file:///root/path/to/file.ipc', IPCProvider, {'ipc_path': '/root/path/to/file.ipc'}),
    ),
)
def test_load_provider_from_env(uri, expected_type, expected_attrs):
    with env('WEB3_PROVIDER_URI', uri):
        provider = load_provider_from_environment()
        assert isinstance(provider, expected_type)
        for attr, val in expected_attrs.items():
            assert getattr(provider, attr) == val
