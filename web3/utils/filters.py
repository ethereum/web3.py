import random
import gevent

from .types import (
    is_string,
    is_array,
)
from .abi import (
    construct_event_topic_set,
    construct_event_data_set,
)


def construct_event_filter_params(event_abi,
                                  contract_address=None,
                                  argument_filters=None,
                                  topics=None,
                                  fromBlock=None,
                                  toBlock=None,
                                  address=None):
    filter_params = {}

    if topics is None:
        topic_set = construct_event_topic_set(event_abi, argument_filters)
    else:
        topic_set = [topics] + construct_event_topic_set(event_abi, argument_filters)

    if len(topic_set) == 1 and is_array(topic_set[0]):
        filter_params['topics'] = topic_set[0]
    else:
        filter_params['topics'] = topic_set

    if address and contract_address:
        if is_array(address):
            filter_params['address'] = address + [contract_address]
        elif is_string(address):
            filter_params['address'] = [address, contract_address]
        else:
            raise ValueError(
                "Unsupported type for `address` parameter: {0}".format(type(address))
            )
    elif address:
        filter_params['address'] = address
    elif contract_address:
        filter_params['address'] = contract_address

    if fromBlock is not None:
        filter_params['fromBlock'] = fromBlock

    if toBlock is not None:
        filter_params['toBlock'] = toBlock

    return filter_params


class BaseFilter(gevent.Greenlet):
    callbacks = None
    running = None
    stopped = False

    def __init__(self, web3, filter_id):
        self.web3 = web3
        self.filter_id = filter_id
        self.callbacks = []
        gevent.Greenlet.__init__(self)

    def __str__(self):
        return "Filter for {0}".format(self.filter_id)

    def _run(self):
        if self.stopped:
            raise ValueError("Cannot restart a Filter")
        self.running = True

        previous_logs = self.web3.eth.getFilterLogs(self.filter_id)
        if previous_logs:
            for log in previous_logs:
                for callback_fn in self.callbacks:
                    callback_fn(log)

        while self.running:
            changes = self.web3.eth.getFilterChanges(self.filter_id)
            if changes:
                for log in changes:
                    for callback_fn in self.callbacks:
                        callback_fn(log)
            gevent.sleep(random.random())

    def watch(self, *callbacks):
        if self.stopped:
            raise ValueError("Cannot watch on a filter that has been stopped")
        self.callbacks.extend(callbacks)

        if not self.running:
            self.start()

    def stop_watching(self, timeout=0):
        self.running = False
        self.stopped = True
        self.web3.eth.uninstallFilter(self.filter_id)
        self.join(timeout)

    stopWatching = stop_watching


class BlockFilter(BaseFilter):
    pass


class TransactionFilter(BaseFilter):
    pass


class LogFilter(BaseFilter):
    def get(self, only_changes=True):
        if self.running:
            raise ValueError(
                "Cannot call `get` on a filter object which is actively watching"
            )
        if only_changes:
            return self.web3.eth.getFilterChanges(self.filter_id)
        else:
            return self.web3.eth.getFilterChanges(self.filter_id)
