import pytest

from eth_utils import (
    to_canonical_address,
)

from ethpm import (
    Package,
)
from ethpm.contract import (
    LinkableContract,
    apply_all_link_refs,
)
from ethpm.exceptions import (
    BytecodeLinkingError,
)
from web3.contract import (
    Contract,
)


@pytest.mark.parametrize(
    "package,factory,attr_dict",
    (
        (
            "escrow",
            "Escrow",
            {
                "SafeSendLib": "0x4F5B11c860b37b68DE6D14Fb7e7b5f18A9A1bdC0"
            },
        ),
        (
            "wallet",
            "Wallet",
            {
                "safe-math-lib:SafeMathLib": "0xa66A05D6AB5c1c955F4D2c3FCC166AE6300b452B"
            },
        ),
    ),
)
def test_linkable_contract_class_handles_link_refs(
    package, factory, attr_dict, get_factory, w3
):
    factory = get_factory(package, factory)
    assert factory.needs_bytecode_linking is True
    linked_factory = factory.link_bytecode(attr_dict)
    assert issubclass(LinkableContract, Contract)
    assert issubclass(factory, LinkableContract)
    assert issubclass(linked_factory, LinkableContract)
    assert factory.needs_bytecode_linking is True
    assert linked_factory.needs_bytecode_linking is False
    # Can't link a factory that's already linked
    with pytest.raises(BytecodeLinkingError):
        linked_factory.link_bytecode(attr_dict)
    offset = factory.unlinked_references[0]["offsets"][0]
    link_address = to_canonical_address(list(attr_dict.values())[0])
    # Ignore lint error b/c black conflict
    assert factory.bytecode[offset : offset + 20] == b"\00" * 20  # noqa: E203
    assert linked_factory.bytecode[offset : offset + 20] == link_address  # noqa: E203


def test_linkable_contract_class_handles_missing_link_refs(get_manifest, w3):
    safe_math_manifest = get_manifest("safe-math-lib")
    SafeMathLib = Package(safe_math_manifest, w3)
    safe_math_lib = SafeMathLib.get_contract_factory("SafeMathLib")
    assert safe_math_lib.needs_bytecode_linking is False
    with pytest.raises(BytecodeLinkingError):
        safe_math_lib.link_bytecode(
            {"SafeMathLib": "0xa66A05D6AB5c1c955F4D2c3FCC166AE6300b452B"}
        )


SAFE_SEND_ADDRESS = "0x4F5B11c860b37b68DE6D14Fb7e7b5f18A9A1bdC0"
SAFE_MATH_ADDRESS = "0xa66A05D6AB5c1c955F4D2c3FCC166AE6300b452B"
SAFE_SEND_CANON = to_canonical_address(SAFE_SEND_ADDRESS)
SAFE_MATH_CANON = to_canonical_address(SAFE_MATH_ADDRESS)


@pytest.mark.parametrize(
    "bytecode,link_refs,attr_dict,expected",
    (
        (
            bytearray(60),
            [{"length": 20, "name": "SafeSendLib", "offsets": [1]}],
            {"SafeSendLib": SAFE_SEND_CANON},
            b"\00" + SAFE_SEND_CANON + bytearray(39),
        ),
        (
            bytearray(60),
            [{"length": 20, "name": "SafeSendLib", "offsets": [1, 31]}],
            {"SafeSendLib": SAFE_SEND_CANON},
            b"\00" + SAFE_SEND_CANON + bytearray(10) + SAFE_SEND_CANON + bytearray(9),
        ),
        (
            bytearray(80),
            [
                {"length": 20, "name": "SafeSendLib", "offsets": [1, 50]},
                {"length": 20, "name": "SafeMathLib", "offsets": [25]},
            ],
            {"SafeSendLib": SAFE_SEND_CANON, "SafeMathLib": SAFE_MATH_CANON},
            b"\00" + SAFE_SEND_CANON + bytearray(4) + SAFE_MATH_CANON
            + bytearray(5) + SAFE_SEND_CANON + bytearray(10),
        ),
    ),
)
def test_apply_all_link_refs(bytecode, link_refs, attr_dict, expected):
    actual = apply_all_link_refs(bytecode, link_refs, attr_dict)
    assert actual == expected


@pytest.mark.parametrize(
    "bytecode,link_refs,attr_dict",
    (
        # Non-empty bytecode
        (
            b"\01" * 60,
            [{"length": 20, "name": "SafeSendLib", "offsets": [1]}],
            {"SafeSendLib": SAFE_SEND_CANON},
        ),
        # Illegal offset
        (
            bytearray(60),
            [{"length": 20, "name": "SafeSendLib", "offsets": [61]}],
            {"SafeSendLib": SAFE_SEND_CANON},
        ),
        # Illegal offsets
        (
            bytearray(60),
            [{"length": 20, "name": "SafeSendLib", "offsets": [1, 3]}],
            {"SafeSendLib": SAFE_SEND_CANON},
        ),
        # Illegal length
        (
            bytearray(60),
            [{"length": 61, "name": "SafeSendLib", "offsets": [0]}],
            {"SafeSendLib": SAFE_SEND_CANON},
        ),
        # Conflicting link refs
        (
            bytearray(60),
            [
                {"length": 20, "name": "SafeSendLib", "offsets": [1]},
                {"length": 20, "name": "SafeMathLib", "offsets": [15]},
            ],
            {"SafeSendLib": SAFE_SEND_CANON, "SafeMathLib": SAFE_MATH_CANON},
        ),
    ),
)
def test_apply_all_link_refs_with_incorrect_args(bytecode, link_refs, attr_dict):
    with pytest.raises(BytecodeLinkingError):
        apply_all_link_refs(bytecode, link_refs, attr_dict)


@pytest.mark.parametrize(
    "attr_dict",
    (
        {},
        # invalid address
        {"SafeSendLib": "abc"},
        {"SafeSendLib": 123},
        {"SafeSendLib": b"abc"},
        # Non-matching refs
        {"safe-send-lib": "0x4F5B11c860b37b68DE6D14Fb7e7b5f18A9A1bdC0"},
        {
            "SafeSendLib": "0x4F5B11c860b37b68DE6D14Fb7e7b5f18A9A1bdC0",
            "Wallet": "0xa66A05D6AB5c1c955F4D2c3FCC166AE6300b452B",
        },
    ),
)
def test_contract_factory_invalidates_incorrect_attr_dicts(get_factory, attr_dict):
    safe_send = get_factory("escrow", "SafeSendLib")
    assert safe_send.needs_bytecode_linking is False
    with pytest.raises(BytecodeLinkingError):
        safe_send.link_bytecode(attr_dict)


def test_unlinked_factory_cannot_be_deployed(get_factory):
    escrow = get_factory("escrow", "Escrow")
    assert escrow.needs_bytecode_linking
    with pytest.raises(BytecodeLinkingError):
        escrow.constructor("0x4F5B11c860b37b68DE6D14Fb7e7b5f18A9A1bdC0").transact()
