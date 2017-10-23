import pytest

from eth_utils import (
    force_text,
)

from web3.utils.compat import subprocess


def test_admin_setSolc(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    try:
        solc_path = subprocess.check_output(['which', 'solc']).strip()
    except subprocess.CalledProcessError:
        pytest.skip('solc binary not found')
    solc_version = subprocess.check_output(['solc', '--version']).strip()

    actual = web3.admin.setSolc(solc_path)
    assert force_text(solc_version) in actual
    assert force_text(solc_path) in actual
