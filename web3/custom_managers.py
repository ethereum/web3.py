import datetime
import threading

from web3.manager import (
    RequestManager
)

'''
Introduce a custom manager, RankingRequestManager, allowing for provider ranking
by block height so that the freshest/most recent provider is selected for the rpc method
call.

RankingRequestManager is initiated via the regular Web3 entry point by adding two
parameters, provider_type and provider_strategy, to the Web3 signature.
    provider_type currently enumerates to 'default' and  'ranking_provider' and
    provider_strategy enumerates to 'default' and ''

The provider ranking is obtained by means of a threaded function call and ranking results are
cached up to five seconds.  RankingRequestManager exposes two properties via the ManagerMixin
class: toggle_provider_strategy and which_provider_strategy callable via the web3.manager handle.
The toggle_provider_strategy allows users to tun off/on the ranking functionality IF Web3 was
initiated accordingly, i.e., the RankingRequestManager needs to be the Web3 manager class object;
which_provider_strategy is a convenience property to verify whether the manager is actively
ranking providers.

Use Example:
    providers = [HTTPProvider('http://...'), ..., HTTPProvider('http://...')]
    web3 = Web3(providers, provider_type="", provider_straegy="")

    results in a web3.manager of type RankingRequestManager and

    web3.manager.toggle_provider_strategy  switches between active ranking or suspended ranking and
    web3.manager.which_provider_strategy   returns the active ranking strategy

Notes and Gottachas:
    providers need to be on the same network
    the manager needs to be initiated as a RankingRequestManager for the toggle
    and which properties to work
'''

# NOTE: Right now, i have made no provisions to check providers a user might add
# after Web3 initialization. For the most part, that's not a problem but the network
# uniformity. I don't really want to check that everytime, so a frozenset-like lock on
# the providers might make sense and then we only need to check for change in the list.
# typing out aloud ... a class attribute in Manager should work. e.g.,
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
    def _req_worker(p, method, params, results):
        try:
            res = p.make_request(method, params)
            results.append((res, True, ''))
        except Exception as e:
            results.append(('', False, '{}'.format(e)))

    assert len(providers) > 0

    method, params = 'net_version', []
    threads, results = [], []
    for p in providers:
        t = threading.Thread(target=_req_worker, args=(p, method, params, results))
        t.start()
        threads.append(t)
    print('threads: ', len(threads))
    [t.join() for t in threads]

    res = len(set([r[0]['result'] for r in results if r[1]]))
    print(res)
    print(results)
    if res == 0:
        vals = ([(str(r[0]), r[2]) for r in results])
        msg = 'Failed to connect for any of the given providers: {}'.format(*vals)
        raise Exception(msg)

    if res > 1:
        vals = ([(str(r[0]['result']), r[2]) for r in results if r[1]])
        msg = 'There seems to be a provider network mismatch: {}'.format(*vals)
        raise ValueError(msg)

    return True


def threaded_provider_ranking(providers):
    ''' sort client providers in-place by respective block height '''
    def _get_block_height(p, results):
        ''' fetch block height if possible and append result to results '''
        try:
            block_height = int(p.make_request(method, params)['result'], 16)
            results.append([p, True, block_height])
        except Exception as e:
            results.append((p, False, e))

    if len(providers) < 2:
        return True

    method, params = 'eth_blockNumber', []
    threads, results = [], []
    for p in providers:
        t = threading.Thread(target=_get_block_height, args=(p, results))
        t.start()
        threads.append(t)

    [t.join() for t in threads]

    # QUESTION: bubble up "bad" providers ?
    good_providers = sorted([r for r in results if r[1]], key=lambda x: x[2], reverse=True)
    bad_providers = [r for r in results if not r[1]]
    good_providers.extend(bad_providers)
    providers[:] = list(zip(*good_providers))[0]
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
        self.provider_strategy = []
        self._validate_provider_strategy(provider_strategy)
        self.provider_strategy.append(provider_strategy)
        self.provider_strategy.append(
            [s for s in ManagerMixin._provider_ranking_strategies if s != provider_strategy][0]
        )

    def _validate_provider_strategy(self, provider_strategy):
        if provider_strategy not in self._provider_ranking_strategies:
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


class RankingRequestManager(RequestManager, ManagerMixin):
    '''  '''
    def __init__(self, web3, providers, middleware=None, provider_strategy='default'):

        self.provider_strategy = provider_strategy

        super().__init__(web3, providers, middleware)
        super(RequestManager, self).__init__(provider_strategy)

    def _make_request(self, method, params):
        if self.provider_strategy[0] != 'default':
            if self._validate_polling_request:
                threaded_provider_ranking(self.providers)
                self._update_last_provider_polling()
        super._make_request(method, params)
