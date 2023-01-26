import pytest

from eth_abi.exceptions import (
    EncodingTypeError,
    ValueOutOfBounds,
)

from web3._utils.events import (
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
EVENT_1_TOPIC = "0xa7144ed450ecab4a6283d3b1e290ff6c889232d922b84d88203eb7619222fb32"
EVENT_2_TOPIC = "0xe74d4a9355b06f414793e46ef1aed5b520bf68289bbd21b6bbfdbf4154451d64"
EVENT_2_ABI = {
    "anonymous": False,
    "inputs": [
        {"indexed": True, "name": "arg0", "type": "bytes2"},
        {"indexed": True, "name": "arg1", "type": "bytes2"},
    ],
    "name": "Event_2",
    "type": "event",
}


def hex_and_pad(i):
    unpadded_hex_value = hex(i).rstrip("L")
    return "0x" + unpadded_hex_value[2:].zfill(64)


@pytest.mark.parametrize(
    "arguments,expected",
    (
        (
            {},
            [EVENT_1_TOPIC],
        ),
        (
            {"arg0": 1},
            [EVENT_1_TOPIC],
        ),
        (
            {"arg0": 1, "arg3": [1, 2]},
            [EVENT_1_TOPIC],
        ),
        (
            {"arg1": 1},
            [EVENT_1_TOPIC, hex_and_pad(1)],
        ),
        (
            {"arg1": [1, 2]},
            [
                EVENT_1_TOPIC,
                [hex_and_pad(1), hex_and_pad(2)],
            ],
        ),
        (
            {"arg1": [1], "arg2": [2]},
            [
                EVENT_1_TOPIC,
                hex_and_pad(1),
                hex_and_pad(2),
            ],
        ),
        (
            {"arg1": [1, 3], "arg2": [2, 4]},
            [
                EVENT_1_TOPIC,
                [hex_and_pad(1), hex_and_pad(3)],
                [hex_and_pad(2), hex_and_pad(4)],
            ],
        ),
    ),
)
def test_construct_event_topics(w3, arguments, expected):
    actual = construct_event_topic_set(EVENT_1_ABI, w3.codec, arguments)
    assert actual == expected


@pytest.mark.parametrize(
    "arguments,expected",
    (
        (
            {},
            [EVENT_1_TOPIC],
        ),
        (
            {"arg0": 1},
            [EVENT_1_TOPIC],
        ),
        (
            {"arg0": 1, "arg3": [1, 2]},
            [EVENT_1_TOPIC],
        ),
        (
            {"arg1": 1},
            [EVENT_1_TOPIC, hex_and_pad(1)],
        ),
        (
            {"arg1": [1, 2]},
            [
                EVENT_1_TOPIC,
                [hex_and_pad(1), hex_and_pad(2)],
            ],
        ),
        (
            {"arg1": [1], "arg2": [2]},
            [
                EVENT_1_TOPIC,
                hex_and_pad(1),
                hex_and_pad(2),
            ],
        ),
        (
            {"arg1": [1, 3], "arg2": [2, 4]},
            [
                EVENT_1_TOPIC,
                [hex_and_pad(1), hex_and_pad(3)],
                [hex_and_pad(2), hex_and_pad(4)],
            ],
        ),
    ),
)
def test_construct_event_topics_non_strict(w3_non_strict_abi, arguments, expected):
    actual = construct_event_topic_set(EVENT_1_ABI, w3_non_strict_abi.codec, arguments)
    assert actual == expected


@pytest.mark.parametrize(
    "arguments,error",
    (
        (
            {"arg0": [b"123412"]},
            ValueOutOfBounds,
        ),
        (
            {"arg1": [b""]},
            ValueOutOfBounds,
        ),
        (
            {"arg0": [b""], "arg1": [b""]},
            ValueOutOfBounds,
        ),
        (
            {"arg0": [""]},
            EncodingTypeError,
        ),
    ),
)
def test_construct_event_topics_strict_errors(w3, arguments, error):
    with pytest.raises(error):
        construct_event_topic_set(EVENT_2_ABI, w3.codec, arguments)
