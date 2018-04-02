#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
    dev tests for ranked-provider manager -- to be moved after dev.
'''
import pytest

from web3 import (
    Web3, HTTPProvider
)

from web3.manager import (
    RequestManager
)

from web3.custom_managers import (
    RankingRequestManager
)


def test_web3_entry():
    ''' tests for revised Web3 entry '''
    providers = [HTTPProvider('https://ropsten.infura.io')]

    # original Web3 entry without extended signature calling on original manager
    web3 = Web3(providers)
    assert web3
    assert web3.isConnected()

    # original Web3 entry with extended signature defaulting to original manager
    # straight pass through
    provider_strategy = 'default'
    ranking_strategy = 'default'
    web3 = Web3(providers)
    assert web3
    assert web3.isConnected()
    assert isinstance(web3.manager, RequestManager)

    # main raise ValueError
    provider_strategy = 'boo hoo'
    ranking_strategy = 'default'
    with pytest.raises(ValueError):
        web3 = Web3(providers, provider_type=provider_strategy, provider_strategy=ranking_strategy)

    # custom manager invalid ranking strategy ignored
    provider_strategy = 'default'
    ranking_strategy = 'boo yah'
    web3 = Web3(providers, provider_type=provider_strategy, provider_strategy=ranking_strategy)
    assert web3
    assert isinstance(web3.manager, RequestManager)

    # ranked-provider Web3 entry calling on new manager with default ranking_strategy
    provider_strategy = 'ranking_provider'
    ranking_strategy = 'default'
    web3 = Web3(providers, provider_type=provider_strategy, provider_strategy=ranking_strategy)
    assert web3

    # finally, call on the custom manager
    providers = [HTTPProvider('https://ropsten.infura.io')] * 5
    provider_strategy = 'ranking_provider'
    ranking_strategy = 'by_highest_block'
    web3 = Web3(providers, provider_type=provider_strategy, provider_strategy=ranking_strategy)
    assert web3
    assert isinstance(web3.manager, RankingRequestManager)
    assert web3.isConnected()
    assert web3.manager.which_provider_strategy == ranking_strategy
