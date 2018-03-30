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
    pass


def test_threaded_provider_ranking():
    pass


# ManagerMixin tests

# __init__

# _setup

# _validate_provider_strategy

# _validate_polling_request

# _update_last_provider_polling

# toggle_provider_strategy

# which_provider_strategy

# RankingRequestManager
# __init__
# Mixin quick test
# Manager quick tests
# _make_requesst
