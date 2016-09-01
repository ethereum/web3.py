import functools

from eth_abi import (
    decode_abi,
    decode_single,
)
from .abi import (
    get_abi_input_types,
    get_abi_input_names,
    get_indexed_event_inputs,
    exclude_indexed_event_inputs,
)
from .functional import (
    replace_key,
)


def coerce_event_abi_types_for_decoding(abi_inputs):
    """
    Event logs use the `sha3(value)` for inputs of type `bytes` or `string`.
    Because of this we need to modify the types so that we can decode the log
    entries using the correct types.
    """
    replace_fn = functools.partial(replace_key, key='type', replacement='bytes32')
    return [
        arg if arg['type'] not in {'bytes', 'string'} else replace_fn(arg)
        for arg in abi_inputs
    ]


def get_event_data(event_abi, log_entry):
    """
    Given an event ABI and a log entry for that event, return the decoded
    """
    log_topics = log_entry['topics'][1:]
    log_topics_abi = get_indexed_event_inputs(event_abi)
    log_topic_raw_types = get_abi_input_types({'inputs': log_topics_abi})
    log_topic_types = coerce_event_abi_types_for_decoding(log_topic_raw_types)
    log_topic_names = get_abi_input_names({'inputs': log_topics_abi})

    if len(log_topics) != len(log_topic_types):
        raise ValueError("Expected {0} log topics.  Got {1}".format(
            len(log_topic_types),
            len(log_topics),
        ))

    log_data = log_entry['data']
    log_data_abi = exclude_indexed_event_inputs(event_abi)
    log_data_raw_types = get_abi_input_types({'inputs': log_data_abi})
    log_data_types = coerce_event_abi_types_for_decoding(log_data_raw_types)
    log_data_names = get_abi_input_names({'inputs': log_data_abi})

    decoded_log_data = decode_abi(log_data_types, log_data)
    decoded_topic_data = [
        decode_single(topic_type, topic_data)
        for topic_type, topic_data
        in zip(log_topic_types, log_topics)
    ]

    decoded_data = {
        'topics': dict(zip(log_topic_names, decoded_topic_data)),
        'data': dict(zip(log_data_names, decoded_log_data)),
    }
    return decoded_data
