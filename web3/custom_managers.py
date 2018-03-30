import datetime
import threading

from web3.manager import (
    RequestManager,
)

'''
both code and documentation text -- to be split and moved

Functionality:
    ...

Opinionated Implementation Aspects:
    ...

User Invocation/API:
    Users invoke the custom manager functionality by providing TWO extra parameters to
    the Web3 initialiation:
    providers = [HTTPProvider('http://...'), ..., HTTPProvider('http://...')]
    Web3(providers, provider_strategy)
    where the default, i.e., not per-reqeust provider ranking, and the ...is "by_block_height"
    providers = [HTTPProvider('http://...'), ..., HTTPProvider('http://...')]
    Web3(providers, provider_ranking_strategy='by_block_height')


'''

# NOTE: Right now, i have made no provisions to check providers a user might add
# after Web3 initialization. For the most part, that's not a problem but the network
# uniformity. I don't really want to check that everytime, so a frozenset-like lock on
# the prvides might make sense and then check only if a change occurs.
# typing out aloud ... a class attribute in Manager shoudl work. e.g.,
# _frozen_providers = set()
# in __init__:
# if not frozen_provider: [frozen_providers.add(p) for p in providers]
# and then check:
# if set(providers) != ManagerMixin._frozen_providers:
#     do check for network id

# QUESTION: do you have use for "check_unique_provider" and especially
# "verify_provider_network" in the main code base? if one uses port fowarding on the
# server nodes and then ssh portfowarding to get there, like-minded scatterbrains such as
# the royal me, would greatly, and repeatedly, benefit especially from latter.


def check_unique_providers(providers):
    '''
        make sure we only have unique providers
        in-place list update, returns None
    '''
    # QUESTION: this is pretty silent. might be better to raise
    s = set()
    providers[:] = [p for p in providers if p.endpoint_uri not in s and
                    (s.add(p.endpoint_uri) or True)]


def verify_provider_network(providers):
    '''
        make sure all providers are on the same network
    '''
    assert len(providers) > 0
    method = 'net_version'
    params = []
    results = threaded_provider_ranking(providers, method, params)

    res = len(set([r[2] for r in results if r[1]]))
    if res == 0:
        vals = ([(str(r[0]), r[2]) for r in results])
        msg = 'Failed to connect for any of the given providers: {}'.format(*vals)
        raise Exception(msg)

    if res > 1:
        vals = ([(str(r[0]), r[2]) for r in results if r[1]])
        msg = 'There seems to be a provider network mismatch: {}'.format(*vals)
        raise ValueError(msg)

    return True  # could make that provider or network id


def threaded_provider_ranking(providers):
    ''' sort provider list by individual provider block height '''
    def t_get_block_height(p, results: list) -> None:
        ''' append block height as int to results list '''
        try:
            block_height = int(p.make_request('eth_blockNumber', [])['result'], 16)
            results.append((p, True, block_height))
        except Exception as e:
            results.append((p, False, e))

    if len(providers) < 2:
        return providers

    threads = []
    results = []
    for i in range(len(providers)):
        t = threading.Thread(target=t_get_block_height, args=(results,))
        t.start()
        threads.append(t)

    [t.join() for t in threads]

    # QUESTION: bubble up "bad" providers ?
    good_providers = sorted([(t[0], t[2]) for t in results if t[1]], key=lambda t: t[1])
    bad_providers = [(t[0], t[2]) for t in results if t[1]]

    providers = good_providers.extend(bad_providers)
    return True


class ManagerMixin:
    '''
        support class for custom request managers exposing control functionality
        to the user.

        property toogle_provider_strategy
            allows for the activation/suspension of the per-request provider ranking
        strategy.

        property which_provider_strategy
            allows for the querying of which strategy is active

        currrently, we allow for only one rankign strategy: provider ranking by
        block height which equates to 'active' per-request provider ranking, whereas
        the defautl strategy does not engage in per-request provider ranking, which
        equetes to inactive/suspended.

    '''
    _provider_ranking_strategies = ['by_highest_block', 'default']
    _last_provider_polling = None
    _polling_timeout = 5.0

    def __init__(self, provider_strategy='default'):
        self.provider_strategy = ['default', 'default']
        self._setup(provider_strategy)

    def _setup(self, provider_strategy):
        if provider_strategy != 'default':
            if self._validate_provider_strategy(provider_strategy):
                self.provider_strategy[0] = provider_strategy

    def _validate_provider_strategy(self, provider_strategy):
        if provider_strategy not in self._provider_rank_strategies:
            vals = (provider_strategy, ManagerMixin._provider_ranking_strategies)
            msg = '{} is not a valid provider strategy. Only {} are valid choices.'
            raise ValueError(msg.format(*vals))
        return True

    @property
    def _validate_polling_request(self):
        '''  '''
        if ManagerMixin._last_provider_polling is None:
            return True
        dt = datetime.datetime.utcnow()
        td = dt - ManagerMixin._last_provider_polling
        if td.total_seconds() <= ManagerMixin._polling_timeout:
            return True
        return False

    @property
    def _update_last_provider_polling(self):
        ManagerMixin._last_provider_polling = datetime.datetime.utcnow()

    @property
    def toggle_provider_strategy(self):
        ''' property toggles the list items '''
        self.provider_strategy.reverse()
        return self.provider_strategy[0]

    @property
    def which_provider_strategy(self):
        ''' convenience property returns dicts as str '''
        # msg = 'the active provider strategy is {}'.format(self.provider_strategy[0])
        # return msg
        return self.provider_strategy[0]
