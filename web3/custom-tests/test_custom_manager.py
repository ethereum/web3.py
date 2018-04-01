#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
    dev tests for ranked-provider manager -- to be moved after dev.
'''
import pytest

from web3 import (
    Web3, HTTPProvider
)

from web3.custom_managers import (
    check_unique_providers,
    verify_provider_network,
    threaded_provider_ranking,
    ManagerMixin,
    RankingRequestManager
)


def test_check_unique_providers():
    ''' '''
    uris = ['http://127.0.0.1:8545',
            'http://52.0.0.1:8545',
            'http://192.0.0.1:8545',
            'http://ropsten.infura,io'
            ]
    providers = [HTTPProvider(uri) for uri in uris]
    web3 = Web3(providers)
    check_unique_providers(web3.providers)
    assert len(uris) == len(web3.providers)

    uris_2 = uris * 2
    providers = [HTTPProvider(uri) for uri in uris_2]
    web3 = Web3(providers)
    assert len(uris_2) == len(web3.providers)
    check_unique_providers(web3.providers)
    assert len(uris_2) == len(web3.providers) * 2


def test_verify_provider_network():
    uris = ['https://ropsten.infura.io',
            'https://kovan.infura.io',
            ]

    # check for the AssertionError if empty providers list
    with pytest.raises(AssertionError):
        verify_provider_network([])

    # check for no connection
    uris = ['https://ropsten.infura.io_bad',
            'https://kovan.infura.io_bad',
            ]
    providers = [HTTPProvider(uri) for uri in uris]
    with pytest.raises(Exception):
        verify_provider_network(providers)

    # check for network mismatch
    uris = ['https://ropsten.infura.io',
            'https://kovan.infura.io',
            ]
    providers = [HTTPProvider(uri) for uri in uris]
    with pytest.raises(ValueError):
        verify_provider_network(providers)

    # QUESTION: an other reliable public node matching one of the
    # infura connections?
    # check for network mismatch
    """
    uris = ['https://ropsten.infura.io',
            'https://kovan.infura.io',
            ]
    providers = [HTTPProvider(uri) for uri in uris]
    assert verify_provider_network(providers)
    """


def test_threaded_provider_ranking():
    '''  '''
    from copy import deepcopy
    # save to assume that block heit ethereum ? ropsten > kovan
    uris = ['https://ropsten.infura.io',
            'https://kovan.infura.io',
            'https://rinkeby.infura.io',
            'https://mainnet.infura.io',
            ]

    # test empty and len one provoiders cases
    providers = []
    threaded_provider_ranking([])
    assert providers == []

    providers = [HTTPProvider(uris[0])]
    reference_providers = deepcopy(providers)
    threaded_provider_ranking(providers)
    assert len(providers) == len(reference_providers)
    assert providers[0].endpoint_uri == reference_providers[0].endpoint_uri

    # going for the marbles
    # expected ranking based on uris order: kovan > mainnet > ropsten > rinkeby

    # QUESTION: this ranking may not hold forever. pull reference block heights
    # from ethercan?

    providers = [HTTPProvider(uri) for uri in uris]
    expected_ranking = [1, 3, 0, 2]
    threaded_provider_ranking(providers)
    assert len(providers) == len(uris)
    for i, p in enumerate(providers):
        assert p.endpoint_uri == uris[expected_ranking[i]]

    # let's mess up one of the uri's which should push it to the end of the
    # providers list and so we kill ... paper, scissor, kovan:
    uris[1] = 'https://eth.infura.io'
    providers = [HTTPProvider(uri) for uri in uris]
    expected_ranking = [3, 0, 2, 1]
    threaded_provider_ranking(providers)
    assert len(providers) == len(uris)
    for i, p in enumerate(providers):
        assert p.endpoint_uri == uris[expected_ranking[i]]


def test_ManagerMixin():
    valid_strategies = ['default', 'by_highest_block']

    # test init, strategy validation
    with pytest.raises(ValueError):
        ManagerMixin(provider_strategy="boo yah")

    for vs in valid_strategies:
        mM = ManagerMixin(provider_strategy=vs)
        assert mM
        assert mM.provider_strategy[0] == vs

    # test toggle and ehich_strategy
    for vs in valid_strategies:
        mM = ManagerMixin(provider_strategy=vs)
        assert mM.provider_strategy[0] == vs
        assert mM.provider_strategy[1] == [s for s in valid_strategies if s != vs][0]
        assert mM.which_provider_strategy == vs
        mM.toggle_provider_strategy
        assert mM.provider_strategy[0] == [s for s in valid_strategies if s != vs][0]
        assert mM.provider_strategy[1] == vs
        assert mM.which_provider_strategy == [s for s in valid_strategies if s != vs][0]

    # TODO: _validate_polling_request

    # TODO: _update_last_provider_polling


def test_RankingRequestManager():
    '''  '''
    uris = ['https://ropsten.infura.io',
            'https://kovan.infura.io',
            'https://rinkeby.infura.io',
            'https://mainnet.infura.io',
            ]

    valid_strategies = ['default', 'by_highest_block']

    # test __init__
    providers = [HTTPProvider(uri) for uri in uris[:1]]
    web3 = Web3(providers)
    with pytest.raises(ValueError):
        RankingRequestManager(web3, providers)

    providers = [HTTPProvider(uri) for uri in uris]
    web3 = Web3(providers)
    assert RankingRequestManager(web3, providers)

    for vs in valid_strategies:
        assert RankingRequestManager(web3, providers, provider_strategy=vs)

    # TODO: maybe add a few more tests for the inheritence/mixin

    # TODO: test which, toggle


def test_main():
    '''  '''
    uris = ['https://ropsten.infura.io',
            'https://kovan.infura.io',
            'https://rinkeby.infura.io',
            'https://mainnet.infura.io',
            ]

    # test original code


    # test new code
