import itertools

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


ABI_EVENT_TYPE_MAP = {
}


def coerce_event_abi_types_for_decoding(input_types):
    """
    Event logs use the `sha3(value)` for inputs of type `bytes` or `string`.
    Because of this we need to modify the types so that we can decode the log
    entries using the correct types.
    """
    return [
        'bytes32' if arg_type in {'bytes', 'string'} else arg_type
        for arg_type in input_types
    ]


def get_event_data(event_abi, log_entry):
    """
    Given an event ABI and a log entry for that event, return the decoded
    """
    if event_abi['anonymous']:
        log_topics = log_entry['topics']
    else:
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

    # sanity check that there are not name intersections between the topic
    # names and the data argument names.
    duplicate_names = set(log_topic_names).intersection(log_data_names)
    if duplicate_names:
        raise ValueError(
            "Invalid Event ABI:  The following argument names are duplicated "
            "between event inputs: '{0}'".format(', '.join(duplicate_names))
        )

    decoded_log_data = decode_abi(log_data_types, log_data)
    decoded_topic_data = [
        decode_single(topic_type, topic_data)
        for topic_type, topic_data
        in zip(log_topic_types, log_topics)
    ]

    event_args = dict(itertools.chain(
        zip(log_topic_names, decoded_topic_data),
        zip(log_data_names, decoded_log_data),
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

    return event_data
