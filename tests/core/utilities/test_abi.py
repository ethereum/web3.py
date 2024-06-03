import json
import pytest

from eth_abi.registry import (
    registry as default_registry,
)
from eth_typing import (
    ABI,
)

from web3._utils.abi import (
    ExactLengthBytesEncoder,
    abi_data_tree,
    get_tuple_type_str_parts,
    map_abi_data,
    recursive_dict_to_namedtuple,
)
from web3._utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
    abi_string_to_text,
    addresses_checksummed,
)
from web3.exceptions import (
    MismatchedABI,
    Web3ValidationError,
    Web3ValueError,
)
from web3.utils.abi import (
    get_event_abi,
    get_event_log_topics,
    get_function_abi,
    get_function_info,
)


@pytest.mark.parametrize(
    "input, expected",
    (
        # Well-formed tuple type strings
        ("tuple", ("tuple", None)),
        ("tuple[]", ("tuple", "[]")),
        ("tuple[1]", ("tuple", "[1]")),
        ("tuple[10]", ("tuple", "[10]")),
        ("tuple[19]", ("tuple", "[19]")),
        ("tuple[195]", ("tuple", "[195]")),
        ("tuple[][]", ("tuple", "[][]")),
        ("tuple[1][1]", ("tuple", "[1][1]")),
        ("tuple[1][]", ("tuple", "[1][]")),
        ("tuple[][1]", ("tuple", "[][1]")),
        ("tuple[][][]", ("tuple", "[][][]")),
        ("tuple[1][][]", ("tuple", "[1][][]")),
        ("tuple[][1][]", ("tuple", "[][1][]")),
        ("tuple[][][1]", ("tuple", "[][][1]")),
        # Malformed tuple type strings
        ("tupleasfasdf", None),
        ("uint256", None),
        ("bool", None),
        ("", None),
        ("tupletuple", None),
        ("tuple[0]", None),
        ("tuple[01]", None),
        ("tuple[][0]", None),
        ("tuple[][01]", None),
        ("tuple[0][][]", None),
        ("tuple[][0][]", None),
        ("tuple[][][0]", None),
    ),
)
def test_get_tuple_type_str_parts(input, expected):
    assert get_tuple_type_str_parts(input) == expected


TEST_FUNCTION_ABI_JSON = """
{
  "constant": false,
  "inputs": [
    {
      "components": [
        {
          "name": "a",
          "type": "uint256"
        },
        {
          "name": "b",
          "type": "uint256[]"
        },
        {
          "components": [
            {
              "name": "x",
              "type": "uint256"
            },
            {
              "name": "y",
              "type": "uint256"
            }
          ],
          "name": "c",
          "type": "tuple[]"
        }
      ],
      "name": "s",
      "type": "tuple"
    },
    {
      "components": [
        {
          "name": "x",
          "type": "uint256"
        },
        {
          "name": "y",
          "type": "uint256"
        }
      ],
      "name": "t",
      "type": "tuple"
    },
    {
      "name": "a",
      "type": "uint256"
    },
    {
      "components": [
        {
          "name": "x",
          "type": "uint256"
        },
        {
          "name": "y",
          "type": "uint256"
        }
      ],
      "name": "b",
      "type": "tuple[][]"
    }
  ],
  "name": "f",
  "outputs": [],
  "payable": false,
  "stateMutability": "nonpayable",
  "type": "function"
}
"""
TEST_FUNCTION_ABI = json.loads(TEST_FUNCTION_ABI_JSON)


CONTRACT_ABI: ABI = [
    {
        "inputs": [{"name": "_arg0", "type": "uint256"}],
        "name": "logTwoEvents",
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"name": "_arg0", "type": "uint256"}],
        "name": "setValue",
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"name": "_arg0", "type": "uint256"},
            {
                "type": "tuple",
                "name": "arg1",
                "components": [
                    {"name": "a", "type": "uint256"},
                    {"name": "b", "type": "uint256"},
                ],
            },
        ],
        "name": "setValue",
        "stateMutability": "nonpayable",
        "type": "function",
    },
]


@pytest.fixture()
def contract_abi() -> ABI:
    return CONTRACT_ABI


@pytest.mark.parametrize(
    "types, data, expected",
    [
        (
            ["bool[2]", "bytes"],
            [[True, False], b"\x00\xFF"],
            [("bool[2]", [("bool", True), ("bool", False)]), ("bytes", b"\x00\xFF")],
        ),
        (
            ["uint256[]"],
            [[0, 2**256 - 1]],
            [("uint256[]", [("uint256", 0), ("uint256", 2**256 - 1)])],
        ),
    ],
)
def test_abi_data_tree(types, data, expected):
    assert abi_data_tree(types, data) == expected


@pytest.mark.parametrize(
    "types, data, funcs, expected",
    [
        (
            ["bool[2]", "int256"],
            [[True, False], 9876543210],
            [
                lambda typ, dat: (
                    (typ, "Tru-dat") if typ == "bool" and dat else (typ, dat)
                ),
                lambda typ, dat: (typ, hex(dat)) if typ == "int256" else (typ, dat),
            ],
            [["Tru-dat", False], "0x24cb016ea"],
        ),
        (
            ["address"],
            ["0x5b2063246f2191f18f2675cedb8b28102e957458"],
            BASE_RETURN_NORMALIZERS,
            ["0x5B2063246F2191f18F2675ceDB8b28102e957458"],
        ),
        (
            ["address[]"],
            [["0x5b2063246f2191f18f2675cedb8b28102e957458"] * 2],
            BASE_RETURN_NORMALIZERS,
            [["0x5B2063246F2191f18F2675ceDB8b28102e957458"] * 2],
        ),
        (
            ["(address,address)[]"],
            [
                [
                    (
                        "0x5b2063246f2191f18f2675cedb8b28102e957458",
                        "0xebe0da78ecb266c7ea605dc889c64849f860383f",
                    )
                ]
                * 2
            ],
            BASE_RETURN_NORMALIZERS,
            [
                [
                    (
                        "0x5B2063246F2191f18F2675ceDB8b28102e957458",
                        "0xeBe0DA78ecb266C7EA605DC889c64849F860383F",
                    )
                ]
                * 2
            ],
        ),
        (
            ["(string,address[])"],
            [
                (
                    b"a string",
                    [b"\xf2\xe2F\xbbv\xdf\x87l\xef\x8b8\xae\x84\x13\x0fOU\xde9["],
                )
            ],
            [addresses_checksummed, abi_string_to_text],
            [("a string", ["0xF2E246BB76DF876Cef8b38ae84130F4F55De395b"])],
        ),
    ],
)
def test_map_abi_data(types, data, funcs, expected):
    assert map_abi_data(funcs, types, data) == expected


@pytest.mark.parametrize("arg", (6, 7, 9, 12, 20, 30))
def test_exact_length_bytes_encoder_raises_on_non_multiples_of_8_bit_size(arg):
    with pytest.raises(Web3ValueError, match="multiple of 8"):
        _ = ExactLengthBytesEncoder(None, data_byte_size=2, value_bit_size=arg)


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ({"a": 1, "b": 2}, "ABIDecodedNamedTuple(a=1, b=2)"),
        ({"a": 0}, "ABIDecodedNamedTuple(a=0)"),
        ({"a": None}, "ABIDecodedNamedTuple(a=None)"),
        ({"a": False}, "ABIDecodedNamedTuple(a=False)"),
        ({}, "ABIDecodedNamedTuple()"),
        ({"a": {}}, "ABIDecodedNamedTuple(a=ABIDecodedNamedTuple())"),
        ({"a": []}, "ABIDecodedNamedTuple(a=[])"),
        ({"a": [0]}, "ABIDecodedNamedTuple(a=[0])"),
        ({"a": [{}]}, "ABIDecodedNamedTuple(a=[ABIDecodedNamedTuple()])"),
        (
            {"a": {"b": {}}},
            "ABIDecodedNamedTuple(a=ABIDecodedNamedTuple(b=ABIDecodedNamedTuple()))",
        ),
    ],
)
def test_recursive_dict_to_namedtuple(input, expected_output):
    named_tuple_output = recursive_dict_to_namedtuple(input)
    output_repr = named_tuple_output.__repr__()
    assert output_repr == expected_output


@pytest.mark.parametrize(
    "name,input_args,input_kwargs,expected_selector,expected_arguments",
    [
        (
            "logTwoEvents",
            [100],
            {},
            "0x5818fad7",
            [
                100,
            ],
        ),
        (
            "setValue",
            [99],
            {},
            "0x55241077",
            [
                99,
            ],
        ),
        (
            "setValue",
            [1],
            ({"arg1": {"a": 2, "b": 0}}),
            "0x647c15ed",
            (
                1,
                (
                    2,
                    0,
                ),
            ),
        ),
    ],
)
def test_get_function_info(
    contract_abi, name, input_args, input_kwargs, expected_selector, expected_arguments
):
    function_info = get_function_info(contract_abi, name, input_args, input_kwargs)
    assert function_info["abi"] == get_function_abi(
        contract_abi, name, input_args, input_kwargs
    )
    assert function_info["selector"] == expected_selector
    assert function_info["arguments"] == expected_arguments


def test_get_function_abi_by_name_with_args(contract_abi):
    function_abi = get_function_abi(contract_abi, "logTwoEvents", [1])
    expected_abi = {
        "inputs": [{"name": "_arg0", "type": "uint256"}],
        "name": "logTwoEvents",
        "stateMutability": "nonpayable",
        "type": "function",
    }
    assert function_abi == expected_abi


def test_get_function_abi_by_name_with_kwargs(contract_abi):
    function_abi = get_function_abi(
        contract_abi,
        "setValue",
        [0],
        {
            "arg1": {
                "a": 10000,
                "b": 987654321,
            }
        },
    )
    expected_abi = {
        "inputs": [
            {"name": "_arg0", "type": "uint256"},
            {
                "type": "tuple",
                "name": "arg1",
                "components": [
                    {"name": "a", "type": "uint256"},
                    {"name": "b", "type": "uint256"},
                ],
            },
        ],
        "name": "setValue",
        "stateMutability": "nonpayable",
        "type": "function",
    }

    assert function_abi == expected_abi


def test_get_function_abi_raises_without_valid_function_identifier(contract_abi):
    with pytest.raises(TypeError, match="Unsupported function identifier"):
        get_function_abi(contract_abi, 1, ["_arg0"])


def test_get_function_abi_by_name(contract_abi):
    with pytest.raises(
        MismatchedABI,
        match="Function invocation failed due to improper number of arguments.",
    ):
        get_function_abi(contract_abi, "logTwoEvents")


def test_get_function_abi_codec_override(contract_abi):
    from eth_abi.codec import (
        ABICodec,
    )

    codec = ABICodec(default_registry)
    function_abi = get_function_abi(contract_abi, "logTwoEvents", [1], abi_codec=codec)
    expected_abi = {
        "inputs": [{"name": "_arg0", "type": "uint256"}],
        "name": "logTwoEvents",
        "stateMutability": "nonpayable",
        "type": "function",
    }
    assert function_abi == expected_abi


@pytest.mark.parametrize(
    "topics,anonymous,expected_topics",
    [
        (
            [
                "0x87e10a54d1dda06db0fde99bdb2e67e6638ca9d2b5add2e3b5b406525b15824a",
                "0x1",
                "0x2",
            ],
            False,
            ["0x1", "0x2"],
        ),
        (
            [
                "0x111",
            ],
            True,
            ["0x111"],
        ),
    ],
)
def test_get_event_log_topics(topics, anonymous, expected_topics):
    event_abi = {
        "anonymous": anonymous,
        "inputs": [],
        "name": "LogSingleArg",
        "type": "event",
    }

    assert get_event_log_topics(event_abi, topics) == expected_topics


@pytest.mark.parametrize(
    "topics,expected_error",
    [
        (
            [],
            "Expected non-anonymous event to have 1 or more topics",
        ),
        (
            ["0x1"],
            "The event signature did not match the provided ABI",
        ),
    ],
)
def test_get_event_log_topics_raises_for_bad_topics(topics, expected_error):
    event_abi = {
        "anonymous": False,
        "inputs": [],
        "name": "LogSingleArg",
        "type": "event",
    }

    with pytest.raises(MismatchedABI, match=expected_error):
        get_event_log_topics(event_abi, topics)


@pytest.mark.parametrize(
    "event_name,input_args",
    [
        ("LogSingleArg", [{"name": "arg0", "type": "uint256"}]),
        ("LogSingleWithIndex", [{"name": "arg0", "type": "uint256"}]),
        ("LogNoArg", []),
    ],
)
def test_get_event_abi(event_name, input_args):
    contract_abi = [
        {
            "anonymous": False,
            "inputs": [{"name": "arg0", "type": "uint256"}],
            "name": "LogSingleArg",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [{"name": "arg0", "type": "uint256", "indexed": True}],
            "name": "LogSingleWithIndex",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [],
            "name": "LogNoArg",
            "type": "event",
        },
    ]
    expected_event_abi = {
        "anonymous": False,
        "inputs": input_args,
        "name": event_name,
        "type": "event",
    }

    input_names = [arg["name"] for arg in input_args]
    assert get_event_abi(contract_abi, event_name, input_names) == expected_event_abi


@pytest.mark.parametrize(
    "name,args,error_type,expected_value",
    (
        (
            None,
            None,
            Web3ValidationError,
            "event_name is required in order to match an event ABI.",
        ),
        ("foo", None, Web3ValueError, "No matching events found"),
    ),
)
def test_get_event_abi_raises_on_error(name, args, error_type, expected_value):
    contract_abi = [
        {
            "inputs": [
                {"name": "x", "type": "uint256"},
                {"name": "y", "type": "uint256"},
            ],
            "outputs": [
                {"name": "sum", "type": "uint256"},
            ],
            "name": "add",
            "type": "function",
        }
    ]
    with pytest.raises(error_type, match=expected_value):
        get_event_abi(contract_abi, name, args)


def test_get_event_abi_raises_if_multiple_found():
    contract_ambiguous_event = [
        {
            "anonymous": False,
            "inputs": [{"name": "arg0", "type": "uint256"}],
            "name": "LogSingleArg",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [{"name": "arg0", "type": "uint256"}],
            "name": "LogSingleArg",
            "type": "event",
        },
    ]
    with pytest.raises(ValueError, match="Multiple events found"):
        get_event_abi(contract_ambiguous_event, "LogSingleArg", ["arg0"])
