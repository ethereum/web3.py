import base64
import json
from typing import (
    Tuple,
)
from urllib import (
    parse,
)

from eth_typing import (
    URI,
)
from eth_utils import (
    is_text,
)
import requests

from ethpm.backends.base import (
    BaseURIBackend,
)
from ethpm.constants import (
    GITHUB_API_AUTHORITY,
)
from ethpm.exceptions import (
    CannotHandleURI,
)
from ethpm.validation.uri import (
    validate_blob_uri_contents,
)


class GithubOverHTTPSBackend(BaseURIBackend):
    """
    Base class for all URIs pointing to a content-addressed Github URI.
    """

    def can_resolve_uri(self, uri: URI) -> bool:
        return is_valid_content_addressed_github_uri(uri)

    def can_translate_uri(self, uri: URI) -> bool:
        """
        GithubOverHTTPSBackend uri's must resolve to a valid manifest,
        and cannot translate to another content-addressed URI.
        """
        return False

    def fetch_uri_contents(self, uri: URI) -> bytes:
        if not self.can_resolve_uri(uri):
            raise CannotHandleURI(f"GithubOverHTTPSBackend cannot resolve {uri}.")

        response = requests.get(uri)
        response.raise_for_status()
        contents = json.loads(response.content)
        if contents["encoding"] != "base64":
            raise CannotHandleURI(
                "Expected contents returned from Github to be base64 encoded, "
                f"instead received {contents['encoding']}."
            )
        decoded_contents = base64.b64decode(contents["content"])
        validate_blob_uri_contents(decoded_contents, uri)
        return decoded_contents

    @property
    def base_uri(self) -> str:
        return GITHUB_API_AUTHORITY


def is_valid_content_addressed_github_uri(uri: URI) -> bool:
    """
    Returns a bool indicating whether the given uri conforms to this scheme.
    https://api.github.com/repos/:owner/:repo/git/blobs/:file_sha
    """
    return is_valid_github_uri(uri, ("/repos/", "/git/", "/blobs/"))


def is_valid_api_github_uri(uri: URI) -> bool:
    """
    Returns a bool indicating whether the given uri conforms to this scheme.
    https://api.github.com/repos/:owner/:repo/contents/:path/:to/:file
    """
    return is_valid_github_uri(uri, ("/repos/", "/contents/"))


def is_valid_github_uri(uri: URI, expected_path_terms: Tuple[str, ...]) -> bool:
    """
    Return a bool indicating whether or not the URI fulfills the following specs
    Valid Github URIs *must*:
    - Have 'https' scheme
    - Have 'api.github.com' authority
    - Have a path that contains all "expected_path_terms"
    """
    if not is_text(uri):
        return False

    parsed = parse.urlparse(uri)
    path, scheme, authority = parsed.path, parsed.scheme, parsed.netloc
    if not all((path, scheme, authority)):
        return False

    if any(term for term in expected_path_terms if term not in path):
        return False

    if scheme != "https":
        return False

    if authority != GITHUB_API_AUTHORITY:
        return False
    return True
