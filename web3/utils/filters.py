import re
import random
import gevent

from .types import (
    is_string,
    is_array,
)
from .events import (
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

    data_filters_set = construct_event_data_set(event_abi, argument_filters)

    return data_filters_set, filter_params


class Filter(gevent.Greenlet):
    callbacks = None
    running = None
    stopped = False
    poll_interval = None

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

        while self.running:
            changes = self.web3.eth.getFilterChanges(self.filter_id)
            if changes:
                for entry in changes:
                    for callback_fn in self.callbacks:
                        if self.is_valid_entry(entry):
                            callback_fn(self.format_entry(entry))
            if self.poll_interval is None:
                gevent.sleep(random.random())
            else:
                gevent.sleep(self.poll_interval)

    def format_entry(self, entry):
        """
        Hook for subclasses to change the format of the value that is passed
        into the callback functions.
        """
        return entry

    def is_valid_entry(self, entry):
        """
        Hook for subclasses to implement additional filtering layers.
        """
        return True

    def watch(self, *callbacks):
        if self.stopped:
            raise ValueError("Cannot watch on a filter that has been stopped")
        self.callbacks.extend(callbacks)

        if not self.running:
            self.start()
        gevent.sleep(0)

    def stop_watching(self, timeout=0):
        self.running = False
        self.stopped = True
        self.web3.eth.uninstallFilter(self.filter_id)
        self.join(timeout)

    stopWatching = stop_watching


class BlockFilter(Filter):
    pass


class TransactionFilter(Filter):
    pass


ZERO_32BYTES = '[a-f0-9]{64}'


def construct_data_filter_regex(data_filter_set):
    return re.compile((
        '^' +
        '|'.join((
            '0x' + ''.join(
                (ZERO_32BYTES if v is None else v[2:] for v in data_filter)
            )
            for data_filter in data_filter_set
        )) +
        '$'
    ))


class LogFilter(Filter):
    data_filter_set = None
    data_filter_set_regex = None
    log_entry_formatter = None

    def __init__(self, *args, **kwargs):
        self.log_entry_formatter = kwargs.pop(
            'log_entry_formatter',
            self.log_entry_formatter,
        )
        if 'data_filter_set' in kwargs:
            self.set_data_filters(kwargs.pop('data_filter_set'))
        super(LogFilter, self).__init__(*args, **kwargs)

    def get(self, only_changes=True):
        if self.running:
            raise ValueError(
                "Cannot call `get` on a filter object which is actively watching"
            )
        if only_changes:
            log_entries = self.web3.eth.getFilterChanges(self.filter_id)
        else:
            log_entries = self.web3.eth.getFilterLogs(self.filter_id)

        if log_entries is None:
            log_entries = []

        formatted_log_entries = [
            self.format_entry(log_entry) for log_entry in log_entries
        ]
        return formatted_log_entries

    def format_entry(self, entry):
        if self.log_entry_formatter:
            return self.log_entry_formatter(entry)
        return entry

    def set_data_filters(self, data_filter_set):
        self.data_filter_set = data_filter_set
        if any(data_filter_set):
            self.data_filter_set_regex = construct_data_filter_regex(
                data_filter_set,
            )

    def is_valid_entry(self, entry):
        if not self.data_filter_set_regex:
            return True
        return bool(self.data_filter_set_regex.match(entry['data']))


class PastLogFilter(LogFilter):
    def _run(self):
        if self.stopped:
            raise ValueError("Cannot restart a Filter")
        self.running = True

        previous_logs = self.web3.eth.getFilterLogs(self.filter_id)

        if previous_logs:
            for entry in previous_logs:
                for callback_fn in self.callbacks:
                    if self.is_valid_entry(entry):
                        callback_fn(self.format_entry(entry))

        self.running = False


class ShhFilter(Filter):
    def _run(self):
        if self.stopped:
            raise ValueError("Cannot restart a filter")
        self.running = True

        while self.running:
            changes = self.web3.shh.getFilterChanges(self.filter_id)
            if changes:
                for entry in changes:
                    for callback_fn in self.callbacks:
                        if self.is_valid_entry(entry):
                            callback_fn(self.format_entry(entry))
            if self.poll_interval is None:
                gevent.sleep(random.random())
            else:
                gevent.sleep(self.poll_interval)

    def stop_watching(self, timeout=0):
        self.running = False
        self.stopped = True
        self.web3.shh.uninstallFilter(self.filter_id)
        self.join(timeout)

    stopWatching = stop_watching
