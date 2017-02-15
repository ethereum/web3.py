import pytest

from eth_utils import (
    event_abi_to_log_topic,
)

from web3.utils.filters import (
    construct_event_filter_params,
)

EVENT_1_ABI = {
    "anonymous": False,
    "inputs": [
        {"indexed": False,"name":"arg0","type":"uint256"},
        {"indexed": True,"name":"arg1","type":"uint256"},
    ],
    "name": "Event_1",
    "type":"event",
}


@pytest.mark.parametrize(
    "event_abi,fn_kwargs,expected",
    (
        (EVENT_1_ABI, {}, {
            "topics": ['0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6'],
        }),
        (EVENT_1_ABI, {'topics': ['should-be-preserved']}, {
            "topics": [
                ['should-be-preserved'],
                ['0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6'],
            ]
        }),
        (EVENT_1_ABI, {'contract_address': '0xd3cda913deb6f67967b99d67acdfa1712c293601'}, {
            "topics": ['0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6'],
            'address': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        }),
        (EVENT_1_ABI, {
            'contract_address': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
            'address': '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
        }, {
            "topics": ['0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6'],
            'address': [
                '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
                '0xd3cda913deb6f67967b99d67acdfa1712c293601',
            ],
        }),
        (EVENT_1_ABI, {'address': '0xd3cda913deb6f67967b99d67acdfa1712c293601'}, {
            "topics": ['0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6'],
            'address': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        }),
    ),
)
def test_construct_event_filter_params(event_abi, fn_kwargs, expected):
    _, actual = construct_event_filter_params(event_abi, **fn_kwargs)
    assert actual == expected


def hex_and_pad(i):
    unpadded_hex_value = hex(i).rstrip('L')
    return '0x' + unpadded_hex_value[2:].zfill(64)


@pytest.mark.parametrize(
    "event_abi,fn_kwargs,expected",
    (
        (EVENT_1_ABI, {}, [[]]),
        (EVENT_1_ABI, {'argument_filters': {'arg0': 1}}, [[hex_and_pad(1)]]),
        (EVENT_1_ABI, {'argument_filters': {'arg0': [1]}}, [[hex_and_pad(1)]]),
        (EVENT_1_ABI, {'argument_filters': {'arg0': [1, 2]}}, [
            [hex_and_pad(1)],
            [hex_and_pad(2)],
        ]),
    ),
)
def test_construct_event_filter_params_for_data_filters(event_abi, fn_kwargs,
                                                        expected):
    actual, _ = construct_event_filter_params(event_abi, **fn_kwargs)
    assert actual == expected
