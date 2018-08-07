from eth_abi import (
    decode_abi,
    is_encodable,
)
from eth_abi.grammar import (
    parse as parse_type_string,
)
from eth_utils import (
    is_list_like,
    is_string,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.threads import (
    TimerClass,
)
from web3._utils.toolz import (
    curry,
)
from web3._utils.validation import (
    validate_address,
)

from .events import (
    construct_event_data_set,
    construct_event_topic_set,
)


def construct_event_filter_params(event_abi,
                                  contract_address=None,
                                  argument_filters=None,
                                  topics=None,
                                  fromBlock=None,
                                  toBlock=None,
                                  address=None):
    filter_params = {}
    topic_set = construct_event_topic_set(event_abi, argument_filters)

    if topics is not None:
        if len(topic_set) > 1:
            raise TypeError(
                "Merging the topics argument with topics generated "
                "from argument_filters is not supported.")
        topic_set = topics

    if len(topic_set) == 1 and is_list_like(topic_set[0]):
        filter_params['topics'] = topic_set[0]
    else:
        filter_params['topics'] = topic_set

    if address and contract_address:
        if is_list_like(address):
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

    if 'address' not in filter_params:
        pass
    elif is_list_like(filter_params['address']):
        for addr in filter_params['address']:
            validate_address(addr)
    else:
        validate_address(filter_params['address'])

    if fromBlock is not None:
        filter_params['fromBlock'] = fromBlock

    if toBlock is not None:
        filter_params['toBlock'] = toBlock

    data_filters_set = construct_event_data_set(event_abi, argument_filters)

    return data_filters_set, filter_params


class Filter:
    callbacks = None
    stopped = False
    poll_interval = None
    filter_id = None

    def __init__(self, web3, filter_id):
        self.web3 = web3
        self.filter_id = filter_id
        self.callbacks = []
        super().__init__()

    def __str__(self):
        return "Filter for {0}".format(self.filter_id)

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

    def _filter_valid_entries(self, entries):
        return filter(self.is_valid_entry, entries)

    def get_new_entries(self):
        log_entries = self._filter_valid_entries(self.web3.eth.getFilterChanges(self.filter_id))
        return self._format_log_entries(log_entries)

    def get_all_entries(self):
        log_entries = self._filter_valid_entries(self.web3.eth.getFilterLogs(self.filter_id))
        return self._format_log_entries(log_entries)

    def _format_log_entries(self, log_entries=None):
        if log_entries is None:
            return []

        formatted_log_entries = [
            self.format_entry(log_entry) for log_entry in log_entries
        ]
        return formatted_log_entries


class BlockFilter(Filter):
    pass


class TransactionFilter(Filter):
    pass


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
        super().__init__(*args, **kwargs)

    def format_entry(self, entry):
        if self.log_entry_formatter:
            return self.log_entry_formatter(entry)
        return entry

    def set_data_filters(self, data_filter_set):
        """(('uint256', [12345, 54321]), ('string', ('a-single-string',)))
        """
        self.data_filter_set = data_filter_set
        if any(data_filter_set):
            self.data_filter_set_function = match_fn(data_filter_set)

    def is_valid_entry(self, entry):
        if not self.data_filter_set:
            return True
        return bool(self.data_filter_set_function(entry['data']))


def normalize_data_values(type_string, data_value):
    _type = parse_type_string(type_string)
    if _type.base == "string":
        if _type.arrlist is not None:
            return tuple((bytes_to_str(value) for value in data_value))
        else:
            return bytes_to_str(data_value)
    return data_value


def bytes_to_str(value):
    return value.decode("utf-8")


@curry
def match_fn(match_values_and_abi, data):
    abi_types, all_match_values = zip(*match_values_and_abi)
    decoded_values = decode_abi(abi_types, HexBytes(data))
    for data_value, match_values, abi_type in zip(decoded_values, all_match_values, abi_types):
        if match_values is None:
            continue
        normalized_data = normalize_data_values(abi_type, data_value)
        for value in match_values:
            if not is_encodable(abi_type, value):
                raise ValueError(
                    "Value {0} is of the wrong abi type. "
                    "Expected {1} typed value.".format(value, abi_type))
            if value == normalized_data:
                break
        else:
            return False

    return True


class ShhFilter(Filter):
    def __init__(self, *args, **kwargs):
        self.poll_interval = kwargs.pop(
            'poll_interval',
            self.poll_interval,
        )
        super().__init__(*args, **kwargs)

    def get_new_entries(self):
        log_entries = self._filter_valid_entries(self.web3.shh.getMessages(self.filter_id))
        return self._format_log_entries(log_entries)

    def get_all_entries(self):
        raise NotImplementedError()

    def watch(self, callback):
        def callback_wrapper():
            entries = self.get_new_entries()

            if entries:
                callback(entries)

        timer = TimerClass(self.poll_interval, callback_wrapper)
        timer.daemon = True
        timer.start()
        return timer
