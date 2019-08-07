import pytest

from eth_abi.exceptions import (
    EncodingTypeError,
    ValueOutOfBounds,
)

from web3._utils.events import (
    construct_event_data_set,
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

EVENT_2_ABI = {
    "anonymous": False,
    "inputs": [
        {"indexed": False, "name": "arg0", "type": "bytes3"},
    ],
    "name": "Event_2",
    "type": "event",
}
EVENT_2_TOPIC = '0x84fa8d791e38d043e0c66b2437051fd24d32b1022f91a754123d8e1746e98453'


def hex_and_pad(i):
    unpadded_hex_value = hex(i).rstrip('L')
    return '0x' + unpadded_hex_value[2:].zfill(64)


@pytest.mark.parametrize(
    'event_abi,arguments,expected',
    (
        (
            EVENT_1_ABI,
            {},
            [[]],
        ),
        (
            EVENT_1_ABI,
            {'arg1': 1},
            [[]],
        ),
        (
            EVENT_1_ABI,
            {'arg0': 1},
            [[hex_and_pad(1), None, None]],
        ),
        (
            EVENT_1_ABI,
            {'arg0': [1]},
            [[hex_and_pad(1), None, None]],
        ),
        (
            EVENT_1_ABI,
            {'arg0': [1, 2]},
            [
                [hex_and_pad(1), None, None],
                [hex_and_pad(2), None, None],
            ],
        ),
        (
            EVENT_1_ABI,
            {'arg0': [1, 3], 'arg3': [2, 4]},
            [
                [hex_and_pad(1), hex_and_pad(2), None],
                [hex_and_pad(1), hex_and_pad(4), None],
                [hex_and_pad(3), hex_and_pad(2), None],
                [hex_and_pad(3), hex_and_pad(4), None],
            ],
        ),
    )
)
def test_construct_event_data_set(web3, event_abi, arguments, expected):
    actual = construct_event_data_set(event_abi, web3.codec, arguments)
    assert actual == expected


@pytest.mark.parametrize(
    'event_abi,arguments,expected',
    (
        (
            EVENT_1_ABI,
            {},
            [[]],
        ),
        (
            EVENT_1_ABI,
            {'arg1': 1},
            [[]],
        ),
        (
            EVENT_1_ABI,
            {'arg0': 1},
            [[hex_and_pad(1), None, None]],
        ),
        (
            EVENT_1_ABI,
            {'arg0': [1]},
            [[hex_and_pad(1), None, None]],
        ),
        (
            EVENT_1_ABI,
            {'arg0': [1, 2]},
            [
                [hex_and_pad(1), None, None],
                [hex_and_pad(2), None, None],
            ],
        ),
        (
            EVENT_1_ABI,
            {'arg0': [1, 3], 'arg3': [2, 4]},
            [
                [hex_and_pad(1), hex_and_pad(2), None],
                [hex_and_pad(1), hex_and_pad(4), None],
                [hex_and_pad(3), hex_and_pad(2), None],
                [hex_and_pad(3), hex_and_pad(4), None],
            ],
        ),
    )
)
def test_construct_event_data_set_strict(web3_strict_types, event_abi, arguments, expected):
    actual = construct_event_data_set(event_abi, web3_strict_types.codec, arguments)
    assert actual == expected


@pytest.mark.parametrize(
    'event_abi,arguments,expected_error',
    (
        (
            EVENT_2_ABI,
            {'arg0': '131414'},
            EncodingTypeError,
        ),
        (
            EVENT_2_ABI,
            {'arg0': b'131414'},
            ValueOutOfBounds,
        ),
        (
            EVENT_2_ABI,
            {'arg0': b'13'},
            ValueOutOfBounds,
        ),
        (
            EVENT_2_ABI,
            {'arg0': b'12'},
            ValueOutOfBounds,
        ),
    )
)
def test_construct_event_data_set_strict_with_errors(web3_strict_types,
                                                     event_abi,
                                                     arguments,
                                                     expected_error):
    with pytest.raises(expected_error):
        construct_event_data_set(event_abi, web3_strict_types.codec, arguments)
