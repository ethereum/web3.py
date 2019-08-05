import pytest

from ens.main import (
    UnauthorizedError,
)


@pytest.mark.parametrize(
    'name, content',
    [
        (
            'tester.eth',
            {'type': 'ipfs-ns', 'hash': 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'},
        ),
        (
            'TESTER.eth',
            {'type': 'ipfs-ns', 'hash': 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'},
        ),
        # handles alternative dot separators
        (
            'tester．eth',
            {'type': 'ipfs-ns', 'hash': 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'},
        ),
        (
            'tester。eth',
            {'type': 'ipfs-ns', 'hash': 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'},
        ),
        (
            'tester｡eth',
            {'type': 'ipfs-ns', 'hash': 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'},
        ),
        # confirm that set-owner works
        (
            'lots.of.subdomains.tester.eth',
            {'type': 'ipfs-ns', 'hash': 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'},
        ),
    ],
)
def test_setup_content(ens, name, content, TEST_ADDRESS):
    assert ens.content(name) is None

    ens.setup_content(name, content)
    assert ens.content(name) == content

    normal_name = ens.nameprep(name)
    assert ens.content(normal_name) == content

    ens.setup_content(name, None)
    assert ens.address(name) is None


@pytest.mark.parametrize(
    'content',
    [
        {'type': 'ipfs-ns', 'hash': 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'},  # noqa: E501
        {'type': 'swarm-ns', 'hash': 'd1de9994b4d039f6548d191eb26786769f580809256b4685ef316805265ea162'},  # noqa: E501
        {'type': 'onion', 'hash': 'zqktlwi4fecvo6ri'},  # noqa: E501
        {'type': 'zeronet', 'hash': '1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D'},  # noqa: E501
        None,
        {},
    ],
)
def test_setup_content_noop(ens, content):
    eth = ens.web3.eth
    owner = ens.owner('tester.eth')

    ens.setup_content('noop.tester.eth', content)
    starting_transactions = eth.getTransactionCount(owner)

    # do not issue transaction if address is already set
    ens.setup_content('noop.tester.eth', content)
    assert eth.getTransactionCount(owner) == starting_transactions


def test_set_address_unauthorized(ens, TEST_ADDRESS):
    with pytest.raises(UnauthorizedError):
        ens.setup_content('eth', {'type': 'ipfs-ns', 'hash': 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'})  # noqa: E501
