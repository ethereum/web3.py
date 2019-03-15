from abc import (
    ABC,
    abstractmethod,
)
import itertools

from eth_abi import (
    decode_abi,
    decode_single,
    encode_single,
    grammar,
)
from eth_typing import (
    TypeStr,
)
from eth_utils import (
    encode_hex,
    event_abi_to_log_topic,
    is_list_like,
    keccak,
    to_dict,
    to_hex,
    to_tuple,
)

import web3
from web3._utils.encoding import (
    encode_single_packed,
    hexstr_if_str,
    to_bytes,
)
from web3._utils.formatters import (
    apply_formatter_if,
)
from web3._utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
)
from web3._utils.toolz import (
    complement,
    compose,
    cons,
    curry,
    valfilter,
)
from web3.datastructures import (
    AttributeDict,
)
from web3.exceptions import (
    MismatchedABI,
)

from .abi import (
    exclude_indexed_event_inputs,
    get_abi_input_names,
    get_indexed_event_inputs,
    map_abi_data,
    normalize_event_input_types,
)


def construct_event_topic_set(event_abi, arguments=None):
    if arguments is None:
        arguments = {}
    if isinstance(arguments, (list, tuple)):
        if len(arguments) != len(event_abi['inputs']):
            raise ValueError(
                "When passing an argument list, the number of arguments must "
                "match the event constructor."
            )
        arguments = {
            arg['name']: [arg_value]
            for arg, arg_value
            in zip(event_abi['inputs'], arguments)
        }

    normalized_args = {
        key: value if is_list_like(value) else [value]
        for key, value in arguments.items()
    }

    event_topic = encode_hex(event_abi_to_log_topic(event_abi))
    indexed_args = get_indexed_event_inputs(event_abi)
    zipped_abi_and_args = [
        (arg, normalized_args.get(arg['name'], [None]))
        for arg in indexed_args
    ]
    encoded_args = [
        [
            None if option is None else encode_hex(encode_single(arg['type'], option))
            for option in arg_options]
        for arg, arg_options in zipped_abi_and_args
    ]

    topics = list(normalize_topic_list([event_topic] + encoded_args))
    return topics


def construct_event_data_set(event_abi, arguments=None):
    if arguments is None:
        arguments = {}
    if isinstance(arguments, (list, tuple)):
        if len(arguments) != len(event_abi['inputs']):
            raise ValueError(
                "When passing an argument list, the number of arguments must "
                "match the event constructor."
            )
        arguments = {
            arg['name']: [arg_value]
            for arg, arg_value
            in zip(event_abi['inputs'], arguments)
        }

    normalized_args = {
        key: value if is_list_like(value) else [value]
        for key, value in arguments.items()
    }

    non_indexed_args = exclude_indexed_event_inputs(event_abi)
    zipped_abi_and_args = [
        (arg, normalized_args.get(arg['name'], [None]))
        for arg in non_indexed_args
    ]
    encoded_args = [
        [
            None if option is None else encode_hex(encode_single(arg['type'], option))
            for option in arg_options]
        for arg, arg_options in zipped_abi_and_args
    ]

    data = [
        list(permutation)
        if any(value is not None for value in permutation)
        else []
        for permutation in itertools.product(*encoded_args)
    ]
    return data


def is_dynamic_sized_type(type_str: TypeStr) -> bool:
    abi_type = grammar.parse(type_str)
    return abi_type.is_dynamic


@to_tuple
def get_event_abi_types_for_decoding(event_inputs):
    """
    Event logs use the `keccak(value)` for indexed inputs of type `bytes` or
    `string`.  Because of this we need to modify the types so that we can
    decode the log entries using the correct types.
    """
    for input_abi in event_inputs:
        if input_abi['indexed'] and is_dynamic_sized_type(input_abi['type']):
            yield 'bytes32'
        else:
            yield input_abi['type']


@curry
def get_event_data(event_abi, log_entry):
    """
    Given an event ABI and a log entry for that event, return the decoded
    event data
    """
    if event_abi['anonymous']:
        log_topics = log_entry['topics']
    elif not log_entry['topics']:
        raise MismatchedABI("Expected non-anonymous event to have 1 or more topics")
    elif event_abi_to_log_topic(event_abi) != log_entry['topics'][0]:
        raise MismatchedABI("The event signature did not match the provided ABI")
    else:
        log_topics = log_entry['topics'][1:]

    log_topics_abi = get_indexed_event_inputs(event_abi)
    log_topic_normalized_inputs = normalize_event_input_types(log_topics_abi)
    log_topic_types = get_event_abi_types_for_decoding(log_topic_normalized_inputs)
    log_topic_names = get_abi_input_names({'inputs': log_topics_abi})

    if len(log_topics) != len(log_topic_types):
        raise ValueError("Expected {0} log topics.  Got {1}".format(
            len(log_topic_types),
            len(log_topics),
        ))

    log_data = hexstr_if_str(to_bytes, log_entry['data'])
    log_data_abi = exclude_indexed_event_inputs(event_abi)
    log_data_normalized_inputs = normalize_event_input_types(log_data_abi)
    log_data_types = get_event_abi_types_for_decoding(log_data_normalized_inputs)
    log_data_names = get_abi_input_names({'inputs': log_data_abi})

    # sanity check that there are not name intersections between the topic
    # names and the data argument names.
    duplicate_names = set(log_topic_names).intersection(log_data_names)
    if duplicate_names:
        raise ValueError(
            "Invalid Event ABI:  The following argument names are duplicated "
            "between event inputs: '{0}'".format(', '.join(duplicate_names))
        )

    decoded_log_data = decode_abi(log_data_types, log_data)
    normalized_log_data = map_abi_data(
        BASE_RETURN_NORMALIZERS,
        log_data_types,
        decoded_log_data
    )

    decoded_topic_data = [
        decode_single(topic_type, topic_data)
        for topic_type, topic_data
        in zip(log_topic_types, log_topics)
    ]
    normalized_topic_data = map_abi_data(
        BASE_RETURN_NORMALIZERS,
        log_topic_types,
        decoded_topic_data
    )

    event_args = dict(itertools.chain(
        zip(log_topic_names, normalized_topic_data),
        zip(log_data_names, normalized_log_data),
    ))

    event_data = {
        'args': event_args,
        'event': event_abi['name'],
        'logIndex': log_entry['logIndex'],
        'transactionIndex': log_entry['transactionIndex'],
        'transactionHash': log_entry['transactionHash'],
        'address': log_entry['address'],
        'blockHash': log_entry['blockHash'],
        'blockNumber': log_entry['blockNumber'],
    }

    return AttributeDict.recursive(event_data)


@to_tuple
def pop_singlets(seq):
    yield from (i[0] if is_list_like(i) and len(i) == 1 else i for i in seq)


@curry
def remove_trailing_from_seq(seq, remove_value=None):
    index = len(seq)
    while index > 0 and seq[index - 1] == remove_value:
        index -= 1
    return seq[:index]


normalize_topic_list = compose(
    remove_trailing_from_seq(remove_value=None),
    pop_singlets,)


def is_indexed(arg):
    if isinstance(arg, TopicArgumentFilter) is True:
        return True
    return False


is_not_indexed = complement(is_indexed)


class EventFilterBuilder:
    formatter = None
    _fromBlock = None
    _toBlock = None
    _address = None
    _immutable = False

    def __init__(self, event_abi, formatter=None):
        self.event_abi = event_abi
        self.formatter = formatter
        self.event_topic = initialize_event_topics(self.event_abi)
        self.args = AttributeDict(
            _build_argument_filters_from_event_abi(event_abi))
        self._ordered_arg_names = tuple(arg['name'] for arg in event_abi['inputs'])

    @property
    def fromBlock(self):
        return self._fromBlock

    @fromBlock.setter
    def fromBlock(self, value):
        if self._fromBlock is None and not self._immutable:
            self._fromBlock = value
        else:
            raise ValueError(
                "fromBlock is already set to {0}. "
                "Resetting filter parameters is not permitted".format(self._fromBlock))

    @property
    def toBlock(self):
        return self._toBlock

    @toBlock.setter
    def toBlock(self, value):
        if self._toBlock is None and not self._immutable:
            self._toBlock = value
        else:
            raise ValueError(
                "toBlock is already set to {0}. "
                "Resetting filter parameters is not permitted".format(self._toBlock))

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if self._address is None and not self._immutable:
            self._address = value
        else:
            raise ValueError(
                "address is already set to {0}. "
                "Resetting filter parameters is not permitted".format(self.address))

    @property
    def ordered_args(self):
        return tuple(map(self.args.__getitem__, self._ordered_arg_names))

    @property
    @to_tuple
    def indexed_args(self):
        return tuple(filter(is_indexed, self.ordered_args))

    @property
    @to_tuple
    def data_args(self):
        return tuple(filter(is_not_indexed, self.ordered_args))

    @property
    def topics(self):
        arg_topics = tuple(arg.match_values for arg in self.indexed_args)
        return normalize_topic_list(cons(to_hex(self.event_topic), arg_topics))

    @property
    def data_argument_values(self):
        if self.data_args is not None:
            return tuple(arg.match_values for arg in self.data_args)
        else:
            return (None,)

    @property
    def filter_params(self):
        params = {
            "topics": self.topics,
            "fromBlock": self.fromBlock,
            "toBlock": self.toBlock,
            "address": self.address
        }
        return valfilter(lambda x: x is not None, params)

    def deploy(self, w3):
        if not isinstance(w3, web3.Web3):
            raise ValueError("Invalid web3 argument: got: {0}".format(repr(w3)))

        for arg in self.args.values():
            arg._immutable = True
        self._immutable = True

        log_filter = w3.eth.filter(self.filter_params)
        log_filter.filter_params = self.filter_params
        log_filter.set_data_filters(self.data_argument_values)
        log_filter.builder = self
        if self.formatter is not None:
            log_filter.log_entry_formatter = self.formatter
        return log_filter


def initialize_event_topics(event_abi):
    if event_abi['anonymous'] is False:
        return event_abi_to_log_topic(event_abi)
    else:
        return list()


@to_dict
def _build_argument_filters_from_event_abi(event_abi):
    for item in event_abi['inputs']:
        key = item['name']
        if item['indexed'] is True:
            value = TopicArgumentFilter(arg_type=item['type'])
        else:
            value = DataArgumentFilter(arg_type=item['type'])
        yield key, value


array_to_tuple = apply_formatter_if(is_list_like, tuple)


@to_tuple
def _normalize_match_values(match_values):
    for value in match_values:
        yield array_to_tuple(value)


class BaseArgumentFilter(ABC):
    _match_values = None
    _immutable = False

    def __init__(self, arg_type):
        self.arg_type = arg_type

    def match_single(self, value):
        if self._immutable:
            raise ValueError("Setting values is forbidden after filter is deployed.")
        if self._match_values is None:
            self._match_values = _normalize_match_values((value,))
        else:
            raise ValueError("An argument match value/s has already been set.")

    def match_any(self, *values):
        if self._immutable:
            raise ValueError("Setting values is forbidden after filter is deployed.")
        if self._match_values is None:
            self._match_values = _normalize_match_values(values)
        else:
            raise ValueError("An argument match value/s has already been set.")

    @property
    @abstractmethod
    def match_values(self):
        pass


class DataArgumentFilter(BaseArgumentFilter):
    @property
    def match_values(self):
        return (self.arg_type, self._match_values)


class TopicArgumentFilter(BaseArgumentFilter):
    @to_tuple
    def _get_match_values(self):
        yield from (self._encode(value) for value in self._match_values)

    @property
    def match_values(self):
        if self._match_values is not None:
            return self._get_match_values()
        else:
            return None

    def _encode(self, value):
        if is_dynamic_sized_type(self.arg_type):
            return to_hex(keccak(encode_single_packed(self.arg_type, value)))
        else:
            return to_hex(encode_single(self.arg_type, value))
