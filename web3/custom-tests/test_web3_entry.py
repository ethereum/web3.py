#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
    dev tests for ranked-provider manager -- to be moved after dev.
'''
import pytest

from web3 import (

    Web3, HTTPProvider

)


def test_web3_entry():
    ''' tests for revised Web3 entry '''

    # original Web3 entry without extended signature calling on original manager
    web3 = Web3(HTTPProvider('https://ropsten.infura.io'))
    assert web3

    # original Web3 entry with extended signature defaulting to original manager
    provider_strategy = 'default'
    ranking_strategy = 'default'
    web3 = Web3(HTTPProvider('https://ropsten.infura.io'))
    assert web3

    provider_strategy = 'boo hoo'
    ranking_strategy = 'default'
    web3 = Web3(HTTPProvider('https://ropsten.infura.io'), provider_strategy, ranking_strategy)
    # assert web3

    provider_strategy = 'default'
    ranking_strategy = 'boo yah'
    web3 = Web3(HTTPProvider('https://ropsten.infura.io'), provider_strategy, ranking_strategy)
    # assert web3

    # ranked-provider Web3 entry calling on new manager
    provider_strategy = 'ranking_provider'
    ranking_strategy = 'default'
    web3 = Web3(HTTPProvider('https://ropsten.infura.io'), provider_strategy, ranking_strategy)
    # assert web3

    provider_strategy = 'ranking_provider'
    ranking_strategy = 'by_highest_block'
    web3 = Web3(HTTPProvider('https://ropsten.infura.io'), provider_strategy, ranking_strategy)
    # assert web3
