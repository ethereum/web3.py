import pytest
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
)

from eth_abi.codec import (
    ABICodec,
)
from eth_abi.registry import (
    registry as default_registry,
)
from eth_typing import (
    ABI,
    ABIComponent,
    ABIComponentIndexed,
    ABIConstructor,
    ABIElement,
    ABIError,
    ABIEvent,
    ABIFallback,
    ABIFunction,
    ABIReceive,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    ExactLengthBytesEncoder,
    abi_data_tree,
    get_tuple_type_str_parts,
    map_abi_data,
    recursive_dict_to_namedtuple,
)
from web3._utils.abi_element_identifiers import (
    FallbackFn,
    ReceiveFn,
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
from web3.types import (
    ABIElementIdentifier,
)
from web3.utils.abi import (
    get_abi_element,
    get_abi_element_info,
    get_event_abi,
    get_event_log_topics,
)

FUNCTION_ABI_NO_INPUTS = ABIFunction({"type": "function", "name": "myFunction"})

FUNCTION_ABI: ABIFunction = {
    "constant": False,
    "inputs": [
        {
            "components": [
                {"name": "a", "type": "uint256"},
                {"name": "b", "type": "uint256[]"},
                {
                    "components": [
                        {"name": "x", "type": "uint256"},
                        {"name": "y", "type": "uint256"},
                    ],
                    "name": "c",
                    "type": "tuple[]",
                },
            ],
            "name": "s",
            "type": "tuple",
        },
        {
            "components": [
                {"name": "x", "type": "uint256"},
                {"name": "y", "type": "uint256"},
            ],
            "name": "t",
            "type": "tuple",
        },
        {"name": "a", "type": "uint256"},
        {
            "components": [
                {"name": "x", "type": "uint256"},
                {"name": "y", "type": "uint256"},
            ],
            "name": "b",
            "type": "tuple[][]",
        },
    ],
    "name": "f",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function",
}

LOG_TWO_EVENTS_ABI: ABIFunction = {
    "inputs": [{"name": "_arg0", "type": "uint256"}],
    "name": "logTwoEvents",
    "stateMutability": "nonpayable",
    "type": "function",
}

SET_VALUE_ABI: ABIFunction = {
    "inputs": [{"name": "_arg0", "type": "uint256"}],
    "name": "setValue",
    "stateMutability": "nonpayable",
    "type": "function",
}
SET_VALUE_WITH_TUPLE_ABI: ABIFunction = {
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

CONTRACT_ABI: ABI = [
    LOG_TWO_EVENTS_ABI,
    SET_VALUE_ABI,
    SET_VALUE_WITH_TUPLE_ABI,
    FUNCTION_ABI_NO_INPUTS,
]

ABI_CONSTRUCTOR = ABIConstructor({"type": "constructor"})

ABI_FALLBACK = ABIFallback({"type": "fallback"})

ABI_RECEIVE = ABIReceive({"type": "receive"})

ABI_EVENT_TRANSFER = ABIEvent(
    {
        "anonymous": False,
        "name": "Transfer",
        "type": "event",
        "inputs": [
            ABIComponentIndexed({"indexed": True, "name": "from", "type": "address"}),
            ABIComponentIndexed({"indexed": True, "name": "to", "type": "address"}),
            ABIComponentIndexed({"indexed": False, "name": "value", "type": "uint256"}),
        ],
    }
)

ABI_ERROR = ABIError({"type": "error", "name": "error"})


@pytest.fixture()
def contract_abi() -> ABI:
    return CONTRACT_ABI


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
def test_get_tuple_type_str_parts(
    input: str, expected: Optional[Tuple[str, Optional[str]]]
) -> None:
    assert get_tuple_type_str_parts(input) == expected


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
def test_abi_data_tree(
    types: List[str], data: Tuple[List[bool], bytes], expected: List[Any]
) -> None:
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
def test_map_abi_data(
    types: List[str],
    data: Tuple[Any, ...],
    funcs: Tuple[Callable[..., Any], ...],
    expected: Tuple[Any, ...],
) -> None:
    assert map_abi_data(funcs, types, data) == expected


@pytest.mark.parametrize("arg", (6, 7, 9, 12, 20, 30))
def test_exact_length_bytes_encoder_raises_on_non_multiples_of_8_bit_size(
    arg: Tuple[int, ...]
) -> None:
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
def test_recursive_dict_to_namedtuple(
    input: Dict[str, Any], expected_output: str
) -> None:
    named_tuple_output = recursive_dict_to_namedtuple(input)
    output_repr = named_tuple_output.__repr__()
    assert output_repr == expected_output


@pytest.mark.parametrize(
    "abi_element_identifier,args,kwargs,expected_selector,expected_arguments",
    [
        ("logTwoEvents", [100], {}, "0x5818fad7", (100,)),
        ("setValue", [99], {}, "0x55241077", (99,)),
        (
            "setValue",
            [1],
            {"arg1": {"a": 2, "b": 0}},
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
def test_get_abi_element_info(
    contract_abi: ABI,
    abi_element_identifier: ABIElementIdentifier,
    args: Sequence[Any],
    kwargs: Dict[str, Any],
    expected_selector: str,
    expected_arguments: Any,
) -> None:
    function_info = get_abi_element_info(
        contract_abi, abi_element_identifier, *args, **kwargs
    )
    assert function_info["abi"] == get_abi_element(
        contract_abi, abi_element_identifier, *args, **kwargs
    )
    assert function_info["selector"] == expected_selector
    assert function_info["arguments"] == expected_arguments


def test_get_abi_element_info_without_args_and_kwargs(
    contract_abi: ABI,
) -> None:
    function_info = get_abi_element_info(contract_abi, "myFunction")
    assert function_info["abi"] == get_abi_element(contract_abi, "myFunction")
    assert function_info["selector"] == "0xc3780a3a"
    assert function_info["arguments"] == ()


def test_get_abi_element_info_raises_mismatched_abi(contract_abi: ABI) -> None:
    with pytest.raises(MismatchedABI, match="Could not identify the intended function"):
        args: Sequence[Any] = [1]
        get_abi_element_info(contract_abi, "foo", *args, **{})


@pytest.mark.parametrize(
    "abi,abi_element_identifier,args,kwargs,expected_abi",
    (
        (
            CONTRACT_ABI,
            "setValue",
            [0],
            {},
            SET_VALUE_ABI,
        ),
        (
            CONTRACT_ABI,
            "setValue",
            [0],
            {
                "arg1": {
                    "a": 10000,
                    "b": 987654321,
                }
            },
            SET_VALUE_WITH_TUPLE_ABI,
        ),
        (
            CONTRACT_ABI,
            "logTwoEvents",
            [1],
            {},
            LOG_TWO_EVENTS_ABI,
        ),
        (
            [FUNCTION_ABI_NO_INPUTS],
            "myFunction",
            [],
            {},
            FUNCTION_ABI_NO_INPUTS,
        ),
        (
            [ABI_EVENT_TRANSFER],
            "Transfer",
            [
                "0x0000000000000000000000000000000000000000",
                "0x0000000000000000000000000000000000000000",
                1,
            ],
            {},
            ABI_EVENT_TRANSFER,
        ),
        (
            [ABI_ERROR],
            "error",
            [],
            {},
            ABI_ERROR,
        ),
        (
            [ABI_FALLBACK],
            "fallback",
            [],
            {},
            ABI_FALLBACK,
        ),
        (
            [ABI_FALLBACK],
            FallbackFn,
            [],
            {},
            ABI_FALLBACK,
        ),
        (
            [ABI_RECEIVE],
            "receive",
            [],
            {},
            ABI_RECEIVE,
        ),
        (
            [ABI_RECEIVE],
            ReceiveFn,
            [],
            {},
            ABI_RECEIVE,
        ),
        (
            [ABI_CONSTRUCTOR],
            "constructor",
            [],
            {},
            ABI_CONSTRUCTOR,
        ),
    ),
)
def test_get_abi_element(
    abi: ABI,
    abi_element_identifier: ABIElementIdentifier,
    args: Sequence[Any],
    kwargs: Dict[str, Any],
    expected_abi: ABIElement,
) -> None:
    assert (
        get_abi_element(
            abi,
            abi_element_identifier,
            *args,
            **kwargs,
        )
        == expected_abi
    )


@pytest.mark.parametrize(
    "abi,abi_element_identifier,args,kwargs,expected_error,expected_message",
    (
        (
            CONTRACT_ABI,
            1,
            ["_arg0"],
            {},
            TypeError,
            "Unsupported function identifier",
        ),
        (
            CONTRACT_ABI,
            "logTwoEvents",
            [],
            {},
            MismatchedABI,
            "Function invocation failed due to improper number of arguments.",
        ),
    ),
)
def test_get_abi_element_raises_with_invalid_parameters(
    abi: ABI,
    abi_element_identifier: ABIElementIdentifier,
    args: Optional[Sequence[Any]],
    kwargs: Optional[Dict[str, Any]],
    expected_error: Type[Exception],
    expected_message: str,
) -> None:
    with pytest.raises(expected_error, match=expected_message):
        get_abi_element(abi, abi_element_identifier, *args, **kwargs)  # type: ignore


def test_get_abi_element_codec_override(contract_abi: ABI) -> None:
    codec = ABICodec(default_registry)
    args: Sequence[Any] = [1]
    function_abi = get_abi_element(contract_abi, "logTwoEvents", *args, abi_codec=codec)
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
def test_get_event_log_topics(
    topics: Sequence[HexBytes], anonymous: bool, expected_topics: Sequence[HexBytes]
) -> None:
    event_abi: ABIEvent = {
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
def test_get_event_log_topics_raises_for_bad_topics(
    topics: Sequence[HexBytes], expected_error: str
) -> None:
    event_abi: ABIEvent = {
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
        ("LogSingleWithIndex", [{"name": "arg0", "type": "uint256", "indexed": True}]),
        ("LogNoArg", []),
    ],
)
def test_get_event_abi(event_name: str, input_args: Sequence[ABIComponent]) -> None:
    contract_abi: ABI = [
        {
            "anonymous": False,
            "inputs": [{"name": "arg0", "type": "uint256"}],
            "name": "LogSingleArg",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                ABIComponentIndexed(
                    {"name": "arg0", "type": "uint256", "indexed": True}
                )
            ],
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
def test_get_event_abi_raises_on_error(
    name: str, args: Sequence[str], error_type: Type[Exception], expected_value: str
) -> None:
    contract_abi: ABI = [
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


def test_get_event_abi_raises_if_multiple_found() -> None:
    contract_ambiguous_event: ABI = [
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
