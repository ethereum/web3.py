import pytest


def test_merged_topic_list_event(
        web3,
        emitter,
        emitter_event_ids,
        wait_for_transaction):
    manual_topics = [
        '0xf16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec',  # event sig
        '0x0000000000000000000000000000000000000000000000000000000000000457',  # 1111
        '0x0000000000000000000000000000000000000000000000000000000000000457',  # 1111
        '0x0000000000000000000000000000000000000000000000000000000000000457',  # 1111
    ]
    with pytest.raises(TypeError):
        emitter.events.LogTripleWithIndex().createFilter(
            fromBlock="latest",
            topics=manual_topics,
            argument_filters={'arg0': 2222, 'arg1': 2222, 'arg2': 2222})
