import pytest

from ethpm import ASSETS_DIR, Package
from ethpm.exceptions import CannotHandleURI


@pytest.mark.parametrize(
    "uri",
    (
        "erc111://packages.zeppelin.os/owned",
        "bzz://da6adeeb4589d8652bbe5679aae6b6409ec85a20e92a8823c7c99e25dba9493d",
    ),
)
def test_package_init_with_unsupported_uris_raises_exception(uri, w3):
    with pytest.raises(CannotHandleURI):
        Package.from_uri(uri, w3)
