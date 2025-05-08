import pytest

from web3._utils.filters import (
    construct_event_filter_params,
)

EVENT_1_ABI = {
    "anonymous": False,
    "inputs": [
        {"indexed": False, "name": "arg0", "type": "uint256"},
        {"indexed": True, "name": "arg1", "type": "uint256"},
    ],
    "name": "Event_1",
    "type": "event",
}


@pytest.mark.parametrize(
    "event_abi,fn_kwargs,expected",
    (
        pytest.param(
            EVENT_1_ABI,
            {},
            {
                "topics": [
                    "0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6"
                ],
            },
            id="no-args",
        ),
        pytest.param(
            EVENT_1_ABI,
            {"topics": ["should-overwrite-topics"]},
            {"topics": ["should-overwrite-topics"]},
            id="overwrite-topics",
        ),
        pytest.param(
            EVENT_1_ABI,
            {"contract_address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601"},
            {
                "topics": [
                    "0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6"
                ],
                "address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
            },
            id="contract_address-string",
        ),
        pytest.param(
            EVENT_1_ABI,
            {
                "contract_address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                "address": "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
            },
            {
                "topics": [
                    "0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6"
                ],
                "address": [
                    "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
                    "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                ],
            },
            id="address-with-contract_address",
        ),
        pytest.param(
            EVENT_1_ABI,
            {"address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601"},
            {
                "topics": [
                    "0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6"
                ],
                "address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
            },
            id="address-string",
        ),
        pytest.param(
            EVENT_1_ABI,
            {"address": ["0xd3CdA913deB6f67967B99D67aCDFa1712C293601"]},
            {
                "topics": [
                    "0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6"
                ],
                "address": ["0xd3CdA913deB6f67967B99D67aCDFa1712C293601"],
            },
            id="address-list",
        ),
        pytest.param(
            EVENT_1_ABI,
            {
                "address": [
                    "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                    "0x1234567890123456789012345678901234567890",
                ]
            },
            {
                "topics": [
                    "0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6"
                ],
                "address": [
                    "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                    "0x1234567890123456789012345678901234567890",
                ],
            },
            id="multiple-address",
        ),
        pytest.param(
            EVENT_1_ABI,
            {
                "address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                "contract_address": ["0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"],
            },
            {
                "topics": [
                    "0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6"
                ],
                "address": [
                    "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                    "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
                ],
            },
            id="one-address-with-multiple-contract_address",
        ),
        pytest.param(
            EVENT_1_ABI,
            {
                "address": [
                    "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                    "0x1234567890123456789012345678901234567890",
                ],
                "contract_address": "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
            },
            {
                "topics": [
                    "0xb470a829ed7792f06947f0ca3730a570cb378329ddcf09f2b4efabd6326f51f6"
                ],
                "address": [
                    "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                    "0x1234567890123456789012345678901234567890",
                    "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413",
                ],
            },
            id="multiple-address-with-one-contract_address",
        ),
    ),
)
def test_construct_event_filter_params(w3, event_abi, fn_kwargs, expected):
    _, actual = construct_event_filter_params(event_abi, w3.codec, **fn_kwargs)
    assert actual == expected


def hex_and_pad(i):
    unpadded_hex_value = hex(i).rstrip("L")
    return "0x" + unpadded_hex_value[2:].zfill(64)


@pytest.mark.parametrize(
    "event_abi,fn_kwargs,expected",
    (
        (EVENT_1_ABI, {}, [[]]),
        (EVENT_1_ABI, {"argument_filters": {"arg0": 1}}, [[hex_and_pad(1)]]),
        (EVENT_1_ABI, {"argument_filters": {"arg0": [1]}}, [[hex_and_pad(1)]]),
        (
            EVENT_1_ABI,
            {"argument_filters": {"arg0": [1, 2]}},
            [
                [hex_and_pad(1)],
                [hex_and_pad(2)],
            ],
        ),
    ),
)
def test_construct_event_filter_params_for_data_filters(
    event_abi, w3, fn_kwargs, expected
):
    actual, _ = construct_event_filter_params(event_abi, w3.codec, **fn_kwargs)
    assert actual == expected
