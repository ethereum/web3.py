import pytest

from web3.utils.events import (
    construct_event_topic_set,
)

EVENT_1_ABI = {
    "anonymous": False,
    "inputs": [
        {"indexed": False, "name": "arg0", "type": "uint256"},
        {"indexed": True, "name": "arg1", "type": "uint256"},
        {"indexed": True, "name": "arg2", "type": "uint256"},
        {"indexed": False, "name": "arg3", "type": "uint256"},
        {"indexed": True, "name": "arg4", "type": "uint256"},
        {"indexed": False, "name": "arg5", "type": "uint256"},
    ],
    "name": "Event_1",
    "type": "event",
}
EVENT_1_TOPIC = '0xa7144ed450ecab4a6283d3b1e290ff6c889232d922b84d88203eb7619222fb32'


def hex_and_pad(i):
    unpadded_hex_value = hex(i).rstrip('L')
    return '0x' + unpadded_hex_value[2:].zfill(64)


@pytest.mark.parametrize(
    'event_abi,arguments,expected',
    (
        (
            EVENT_1_ABI,
            {},
            [EVENT_1_TOPIC],
        ),
        (
            EVENT_1_ABI,
            {'arg0': 1},
            [EVENT_1_TOPIC],
        ),
        (
            EVENT_1_ABI,
            {'arg0': 1, 'arg3': [1, 2]},
            [EVENT_1_TOPIC],
        ),
        (
            EVENT_1_ABI,
            {'arg1': 1},
            [
                EVENT_1_TOPIC, hex_and_pad(1)
            ],
        ),
        (
            EVENT_1_ABI,
            {'arg1': [1, 2]},
            [
                EVENT_1_TOPIC, [hex_and_pad(1), hex_and_pad(2)],
            ],
        ),
        (
            EVENT_1_ABI,
            {'arg1': [1], 'arg2': [2]},
            [
                EVENT_1_TOPIC, hex_and_pad(1), hex_and_pad(2),
            ],
        ),
        (
            EVENT_1_ABI,
            {'arg1': [1, 3], 'arg2': [2, 4]},
            [
                EVENT_1_TOPIC,
                [hex_and_pad(1), hex_and_pad(3)],
                [hex_and_pad(2), hex_and_pad(4)]
            ],
        ),
    )
)
def test_construct_event_topics(event_abi, arguments, expected):
    actual = construct_event_topic_set(event_abi, arguments)
    assert actual == expected
