import pytest

VALID_MANIFEST = {
    'package_name': 'foo',
    'manifest_version': '2',
    'version': '1.0.0',
}


# Returns web3 instance with `pm` module attached
@pytest.fixture
def web3():
    try:
        from web3.pm import PM
    except ModuleNotFoundError as exc:
        assert False, "eth-pm import failed because: %s" % exc
    PM.attach(web3, 'pm')
    return web3


@pytest.mark.xfail(reason="eth-pm will not installed by default until it is stable")
def test_pm_init_with_minimal_manifest(web3):
    pm = web3.pm.get_package_from_manifest(VALID_MANIFEST)
    assert pm.name == 'foo'
