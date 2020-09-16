import os
import pytest

from requests.exceptions import (
    HTTPError,
)

from ethpm import (
    Package,
)
from ethpm.backends.http import (
    GithubOverHTTPSBackend,
)
from ethpm.constants import (
    GITHUB_API_AUTHORITY,
)


@pytest.mark.parametrize(
    "uri",
    (
        "https://api.github.com/repos/ethpm/ethpm-spec/git/blobs/899042f95ad624d5ecf0b96b0926c96cd682522d",  # noqa: E501
    ),
)
@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_github_over_https_backend_fetch_uri_contents(uri, owned_contract, w3):
    # these tests may occassionally fail CI as a result of their network requests
    backend = GithubOverHTTPSBackend()
    assert backend.base_uri == GITHUB_API_AUTHORITY
    # integration with Package.from_uri
    owned_package = Package.from_uri(uri, w3)
    assert owned_package.name == "owned"


@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_github_over_https_backend_raises_error_with_invalid_content_hash(w3):
    invalid_uri = "https://api.github.com/repos/ethpm/py-ethpm/git/blobs/a7232a93f1e9e75d606f6c1da18aa16037e03123"  # noqa: E501
    with pytest.raises(HTTPError):
        Package.from_uri(invalid_uri, w3)
