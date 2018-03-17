#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sys
import threading
# from copy import deepcopy

from web3 import Web3, HTTPProvider
"""
    dummy feature/functionality implementation to kick off custom provider ranking
    and method routing features for manager.

    03/16/2018
    v: pre-pre-alpha
"""


"""
i dumped everything into a single namespace, which is to be split into a provider
and broadcast class. finalized bindings to manager are missing. repeat: missing. yet.


should make for a semi-decent namespace and property/method access but a rpc-style
interface may also work:
    dC = DummyCls(....)
    in parent obj:
    def provider_handler(self,method,params):
        if hasattr(ds,method):
            return getattr(ds,method)(params)
        return '{} is not a valid method'.format(method)
"""


# this might be a candidate for the "base" manager also
def check_unique_providers(providers):
    ''' make sure we only have unique providers
        but at this point, we'll miss localhost and possible 127.*,192.*, etc. dupes

        in-place list update, returns None
    '''
    # we don't want dupes and should check right at the top of the manager init
    # not a big fan of decorator pollution but this might be a candidate.
    s = set()
    providers[:] = [p for p in providers if p.endpoint_uri not in s and
                    (s.add(p.endpoint_uri) or True)]


def threaded_providers_call(providers, method, params, t_timeout=1.0):
    ''' rpc calls for each provider
        returns list of tuples
            (p: provider,
            call_state: bool,
            result: Union[call result: dict, error msg: str]
            )
        pretty easily updated to async especially if we're working off a
        self contained loop.
        lest it be overlooked, this function IS blocking. maybe renaming it
        is in order ... blocking_providers_call ?
    '''
    def rpc_call(provider, method, params, results):
        if params is None:
            params = []
        try:
            data = provider.make_request(method, params)
            results.append((provider, True, data['result']))
        except Exception as e:
            results.append((provider, False, '{}'.format(e)))

    assert providers
    assert isinstance(providers, list)

    results = []  # easy tiger, append is threadsafe
    threads = []
    for p in providers:
        t = threading.Thread(target=rpc_call, args=(p, method, params, results))
        threads.append(t)

    [t.start() for t in threads]

    for t in threads:
        try:
            t.join(timeout=t_timeout)
        except RuntimeError:
            results.append(t._args[0], False, 'connection attempt timeout.')

    return results


def sequential_providers_call(providers, method, params):
    ''' could do that for, say, len(providers) < 3 ?? although with higher timeout values,
        the threaded version pretty much always will win on a worst-case scenario basis.
    '''
    raise NotImplementedError('use threaded version instead.')


def verify_provider_networks(providers):
    ''' make sure all providers are on the same network '''
    method = 'net_version'
    params = []
    results = threaded_providers_call(providers, method, params)

    res = len(set([r[2] for r in results if r[1]]))
    if res == 0:
        vals = ([(str(r[0]), r[2]) for r in results])
        msg = 'Failed to connect for any of the given providers: {}'.format(*vals)
        raise Exception(msg)

    if res != 1:
        vals = ([(str(r[0]), r[2]) for r in results if r[1]])
        msg = 'There seems to be a provider network mismatch: {}'.format(*vals)
        raise ValueError(msg)

    return providers


class DummyCls:
    '''
        beginning documentation/examples:

        provider rank strategies:

        In case multiple providers are specified, the "default" rule selects the
        first available provider. In addition to the default option, users can specify
        provider selection "by_highest_block" or "by_block". The "by highest block" rule
        checks each provider by block height and stops as soon as a provider >= highest block
        is found; "by_block", on the other hand, exhaustively ranks all specified providers
        by their respective block height.

        The provider rank strategy is currently only supported at Web3 instantiation, e.g.

            provider_local = HTTPProvider('http://127.0.0.1:8545')
            provider_infura = HTTPProvider('https://ropsten.infura.io:8545')
            provider_my_node = HTTPProvider('http://my.node.io:8545')
            my_providers = [provider_local, provider_infura, provider_my_node]

            Web3(my_providers,rank_strategy="by_block")

        note the use of the rank_strategy param in the signature <"default",...>

        Please note that any strategy other than "default" incurs additional (approx k)
        calls for EACH network method call, where k is the number of providers. This MAY result
        in a significant performance penalty.

        In order to manage performance, users can use the
            toggle_provider_strategy property
        to switch between the default and custom provider selection properties. The
            which_provider_strategy property
        returns the active provider ranking strategy.
    '''

    _provider_rank_strategies = ['by_block', 'by_highest_block', 'default']
    _provider_rank_strategy = ("default", "default")

    '''
        beginning documentation/examples:
        method broadcast strategies:

        Not all methods are created equal. Hence, users can specify broadcast strategies
        on a per method basis. The default strategy ...

        "all": braodcast method to all available providers
        "highest": broadcast to the provider with the highest block
        "local": broadcasts to the local provider, if available or the provider with the
        highest block.

        method broadcast strategires may be used with or without provider rank strategies.

        Again, users ought to be cognizant of the added overhead and potential performance
        penalties.

        NOTE: custom provider ranking and braodcasting are fundementally independent of
        each other, although the results of a provider rank strategy maybe be reused for
        custom method broadcasting.
        # TODO: this ¶ sucks. try again.

    '''

    _broadcast_strategies = ['all', 'highest', 'local', 'default']
    _broadcast_strategy = ['all', 'highest', 'local']
    _disabled_broadcast_registry = []
    _broadcast_registry = []

    def __init__(self, provider_strategy='default', broadcast_strategies=[]):
        ''' dummy init so we can test a few things before we move to the real thing '''
        self._setup(provider_strategy, broadcast_strategies)

    def _setup(self, provider_strategy, broadcast_strategies):
        if provider_strategy != 'default':
            if provider_strategy not in self._provider_rank_strategies:
                msg = '{} is not a valid provider strategy.'.format(provider_strategy)
                raise ValueError(msg)

            self._provider_rank_strategy[0] = provider_strategy

        if broadcast_strategies:
            # TODO: add uniq check on method-strategy tuple. set() should do.
            if isinstance(broadcast_strategies, dict):
                broadcast_strategies = [broadcast_strategies]

            for d in broadcast_strategies:
                err_msg = ''
                for k, v in broadcast_strategies.items():
                    # if k not in ?? valid_methods:
                    #    pass
                    # TODO: get method look up
                    if v not in self._broadcast_strategies:
                        err_msg += 'strategy {} for method {} is not valid.'.format(v.k)
            if err_msg:
                raise ValueError(err_msg)

            self._broadcast_registry = broadcast_strategies

    @staticmethod
    def _rlodip(some_list, key):
        ''' reduce list of dicts in place by key name '''
        some_list[:] = [d for d in some_list if d.get(key) is not None]

    def _validate_provider_strategy(self, rule_name):
        if rule_name not in self._provider_rank_strategies:
            msg = '{} is not a valid rule.'.format(rule_name)
            raise ValueError(msg)
        return True

    def _validate_broadcast_strategy(self, rule_name):
        if rule_name not in self._broadcast_strategies:
            msg = '{} is not a valid strategy.'.format(rule_name)
            raise ValueError(msg)
        return True

    @property
    def toggle_provider_strategy(self):
        ''' convenience property toggles the two list items '''
        assert isinstance(self._provider_rank_strategy, list)
        assert len(self._provider_rank_strategy, 2)

        self._provider_rank_strategy.reverse()
        return self._provider_rank_strategy[0]

    @property
    def which_provider_strategy(self):
        ''' convenience property returns dicts as str '''
        assert isinstance(self._provider_rank_strategy, list)
        msg = 'the active provider strategy is {}'.format(self._provider_rank_strategy[0])
        return msg

    @property
    def toggle_breodcast_strategies(self):
        ''' convenience property toggles between active and paused registries'''
        _ = self._broadcast_registry
        self._broadcast_registry = self._disabled_broadcast_registry
        self._disabled_broadcast_registry = _
        return self._broadcast_registry

    @property
    def which_broadcast_strategy(self):
        ''' convenience method '''
        vals = (', '.join([str(d) for d in self._broadcast_registry]))
        msg = 'active broadcast routing in place for {}'.format(*vals)
        if self._disabled_broadcast_registry:
            vals = (', '.join([str(d) for d in self._disabled_broadcast_registry]))
            msg += '\ncustom broadcasting is paused for {}'.format(*vals)
        return msg

    def deregister_broadcast_strategy(self, m_name):
        ''' '''
        assert m_name
        # the any() maybe superfluous unless we log a warning
        if any(m_name in d for d in self._broadcast_registry):
            self._rliodip(self._broadcast_registry, m_name)
        if any(m_name in d for d in self._disabled_broadcast_registry):
            self._rliodip(self._disabled_broadcast_registry, m_name)

    def register_broadcast_strategy(self, m_name, strategy_name):
        ''' in flight brodacast strategy add '''
        # TODO: finalize the checks
        if not self._valid_method(m_name) and self._valid_method_rule(strategy_name):
            vals = (m_name, strategy_name)
            msg = '{}:{} is not a valid specification. maybe a spelling issue?'.format(*vals)
            raise ValueError(msg)

        if any(m_name in d for d in self._disabled_broadcast_registry):
            self._rliodip(self._disabled_broadcast_registry, m_name)

        if any(m_name in d for d in self._broadcast_registry):
            self._rliodip(self._broadcast_registry, m_name)

        self._broadcast_registry.append({m_name: strategy_name})

    def toggle_broadcast_strategy(self, m_name):
        ''' toggle strategy by method name between active and inactive '''
        if any(m_name in d for d in self._disabled_broadcast_registry):
            d = [d for d in self._disabled_broadcast_registry]
            self._rliodip(self._disabled_broadcast_registry, m_name)
            self._rliodip(self._broadcast_registry, m_name)
            self._broadcast_registry.append(d)
            msg = '{} is now active'.format(d)
            return msg
        elif any(m_name in d for d in self._broadcast_registry):
            d = [d for d in self._broadcast_registry]
            self._rliodip(self._disabled_broadcast_registry, m_name)
            self._rliodip(self._broadcast_registry, m_name)
            self._disabled_broadcast_registry.append(d)
            msg = '{} is now inactive'.format(d)
            return msg
        else:
            msg = 'no straegy for {} registered and no action was taken.'.format(m_name)
            return msg

    def _rank_providers(providers, rank_rule='default'):
        # can easily break that out

        # TODO: finalize and use the threaded_providers_call function

        def get_syn_status(p, bh_diff=5):
            ''' if block height diff < X, keep it, else mark provider out '''
            data = p.make_request('is_syncing', [])
            hb = int(data['result']['highestBlock'], 16)
            cb = int(data['result']['currentBlock'], 16)
            if abs(hb - cb) < abs(bh_diff):
                return True
            return False

        def get_block_height(p, results):
            ''' get current block height as int '''
            # return int(p.make_request('eth_blockNumber',[])['result'],16)
            try:
                bh = int(p.make_request('eth_blockNumber', [])['result'], 16)
                results.append((p, True, bh))
            except Exception as e:
                results.append(p, False, e)

        if len(providers) < 2:
            return providers

        good_providers, bad_providers = [], [], []

        rr = rank_rule.lower()
        if rr == 'default':
            return providers

        elif rr == 'by_highest_block':
            msg = 'note to self: rank_providers "highest_block" needs to be done.'
            msg += ' feasible to call out to etherscan api and get max height for 1,3,42 ?'
            raise NotImplementedError(msg)

        elif rr == 'by_block_height':
            ts, results = [], []
            for p in set(providers):
                ts.append(threading.Thread(target=get_block_height, args=(p, results)))
            [t.start() for t in ts]

            for t in ts:
                try:
                    t.join(timeout=1.0)
                except RuntimeError as e:
                    results.append((p, False, e))

            # process results
            good_providers = sorted([(t[0], t[2]) for t in results if t[1]], key=lambda t: t[1])
            bad_providers = [(t[0], t[2]) for t in results if t[1]]

            # TODO: log bad providers

            return good_providers

        else:
            msg = 'ouch. {} is invalid and should not have gotten that far.'.format(rr)
            raise Exception(msg)

        return providers


def lame_test_misc():
    ''' test util and cleanign functions '''
    import pytest

    my_providers = ['https://ropsten.infura.io',
                    'https://kovan.infura.io',
                    'https://mainnet.infura.io']
    web3 = Web3([HTTPProvider(p) for p in my_providers])
    assert web3.isConnected()

    # test and make unique provider list
    dupe_providers = ['https://ropsten.infura.io',
                      'https://ropsten.infura.io',
                      'https://ropsten.infura.io']
    uniq_providers = ['https://ropsten.infura.io',
                      'https://kovan.infura.io',
                      'https://mainnet.infura.io']
    for my_providers in [dupe_providers, uniq_providers]:
        web3 = Web3([HTTPProvider(p) for p in my_providers])
        check_unique_providers(web3.manager.providers)
        assert len(web3.manager.providers) == len(set(my_providers))

    # check threaded rpc caller
    my_providers = ['https://ropsten.infura.io',
                    'https://kovan.infura.io',
                    'https://mainnet.infura.io']
    web3 = Web3([HTTPProvider(p) for p in my_providers])
    results = threaded_providers_call(web3.manager.providers, 'net_version', [])
    # TODO: probably should chnage that soemthign slight less fragile
    assert sum([r[1] for r in results]) == len(my_providers)

    # raise connection and timeout exceptions
    # TODO: better failure addresses
    my_providers = ['https://ropsten.infura.io',
                    'https://127.0.0.1:8001',
                    'https://ethereum.infura.io']
    web3 = Web3([HTTPProvider(p) for p in my_providers])
    results = threaded_providers_call(web3.manager.providers, 'net_version', [])

    sys.stdout.write('{}\n'.format(results))
    # TODO: ... assert the error msg

    # verify provider network congruence
    my_providers = ['https://ropsten.infura.io',
                    'https://kovan.infura.io',
                    'https://mainnet.infura.io']
    web3 = Web3([HTTPProvider(p) for p in my_providers])
    with pytest.raises(ValueError):
        verify_provider_networks(web3.manager.providers)

    # TODO: add test for common networks within pytest framework already in place.


def lame_test_interface():
    ''' test user contraol properties & methods '''
    import pytest
    pass


def lame_test_strategies():
    ''' test provider and method strategies routing '''
    import pytest
    pass


if __name__ == '__main__':
    # main_testers()
    pass
