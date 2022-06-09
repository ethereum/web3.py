import logging
from typing import (
    Generator,
    Type,
)

from eth_typing import (
    URI,
)
from eth_utils import (
    to_tuple,
)
from ipfshttpclient.exceptions import (
    ConnectionError,
)

from ethpm.backends.base import (
    BaseURIBackend,
)
from ethpm.backends.http import (
    GithubOverHTTPSBackend,
)
from ethpm.backends.ipfs import (
    DummyIPFSBackend,
    InfuraIPFSBackend,
    LocalIPFSBackend,
    get_ipfs_backend_class,
)
from ethpm.backends.registry import (
    RegistryURIBackend,
)

logger = logging.getLogger("ethpm.utils.backend")

ALL_URI_BACKENDS = [
    InfuraIPFSBackend,
    DummyIPFSBackend,
    LocalIPFSBackend,
    GithubOverHTTPSBackend,
    RegistryURIBackend,
]


@to_tuple
def get_translatable_backends_for_uri(
    uri: URI,
) -> Generator[Type[BaseURIBackend], None, None]:
    # type ignored because of conflict with instantiating BaseURIBackend
    for backend in ALL_URI_BACKENDS:
        try:
            if backend().can_translate_uri(uri):  # type: ignore
                yield backend
        except ConnectionError:
            logger.debug("No local IPFS node available on port 5001.", exc_info=True)


@to_tuple
def get_resolvable_backends_for_uri(
    uri: URI,
) -> Generator[Type[BaseURIBackend], None, None]:
    # special case the default IPFS backend to the first slot.
    default_ipfs = get_ipfs_backend_class()
    if default_ipfs in ALL_URI_BACKENDS and default_ipfs().can_resolve_uri(uri):
        yield default_ipfs
    else:
        for backend_class in ALL_URI_BACKENDS:
            if backend_class is default_ipfs:
                continue
            # type ignored because of conflict with instantiating BaseURIBackend
            else:
                try:
                    if backend_class().can_resolve_uri(uri):  # type: ignore
                        yield backend_class
                except ConnectionError:
                    logger.debug(
                        "No local IPFS node available on port 5001.", exc_info=True
                    )
