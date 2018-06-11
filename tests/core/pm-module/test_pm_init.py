from web3 import Web3

VALID_MANIFEST = {
    'package_name': 'foo',
    'manifest_version': '2',
    'version': '1.0.0',
}


def test_pm_init_with_minimal_manifest():
    w3 = Web3(Web3.EthereumTesterProvider(), pm=True)
    pm = w3.pm.get_package(VALID_MANIFEST)
    assert pm.name == 'foo'
