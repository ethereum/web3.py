import pytest

from web3.pm import (
    PM,
)

VALID_MANIFEST = {
    'package_name': 'foo',
    'manifest_version': '2',
    'version': '1.0.0',
}


# Returns web3 instance with `pm` module attached
@pytest.fixture
def web3():
    PM.attach(web3, 'pm')
    return web3


@pytest.mark.skip(reason='Skipped until `ethpm` dependency is stabilized.')
def test_pm_init_with_minimal_manifest(web3):
    pm = web3.pm.get_package_from_manifest(VALID_MANIFEST)
    assert pm.name == 'foo'
