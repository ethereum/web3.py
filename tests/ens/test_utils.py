import pytest
from unittest.mock import (
    patch,
)

from eth_utils import (
    is_integer,
    to_bytes,
)

from ens import (
    BaseENS,
)
from ens._normalization import (
    ENSNormalizedName,
)
from ens.exceptions import (
    ENSValidationError,
)
from ens.utils import (
    ens_encode_name,
    init_async_web3,
    init_web3,
    is_valid_name,
    label_to_hash,
    normal_name_to_hash,
    normalize_name,
    raw_name_to_hash,
)
from tests.ens.conftest import (
    ENSIP15_NORMALIZED_TESTER_DOT_ETH,
)
from web3.eth import (
    AsyncEth,
)
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
)


def test_init_web3_adds_expected_middlewares():
    w3 = init_web3()
    middlewares = map(str, w3.manager.middleware_onion)
    assert "stalecheck_middleware" in next(middlewares)


@pytest.mark.parametrize(
    "name,expected",
    (
        # test some allowed cases
        ("tester.eth", b"\x06tester\x03eth\x00"),
        (
            "a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p",
            b"\x01a\x01b\x01c\x01d\x01e\x01f\x01g\x01h\x01i\x01j\x01k\x01l\x01m\x01n\x01o\x01p\x00",  # noqa: E501
        ),
        (
            "1.2.3.4.5.6.7.8.9.10",
            b"\x011\x012\x013\x014\x015\x016\x017\x018\x019\x0210\x00",
        ),
        ("abc.123.def-456.eth", b"\x03abc\x03123\x07def-456\x03eth\x00"),
        ("abc.123.def-456.eth", b"\x03abc\x03123\x07def-456\x03eth\x00"),
        (
            "nhéééééé.eth",
            b"\x0enh\xc3\xa9\xc3\xa9\xc3\xa9\xc3\xa9\xc3\xa9\xc3\xa9\x03eth\x00",
        ),
        ("🌈rainbow.eth", b"\x0b\xf0\x9f\x8c\x88rainbow\x03eth\x00"),
        ("🐔🐔.tk", b"\x08\xf0\x9f\x90\x94\xf0\x9f\x90\x94\x02tk\x00"),
        # test that label length may be less than 255
        (f"{'a' * 255}.b", b"\xff" + (b"a" * 255) + b"\x01b\x00"),
        (f"a.{'b' * 255}", b"\x01a" + b"\xff" + (b"b" * 255) + b"\x00"),
        (f"abc-123.{'b' * 255}", b"\x07abc-123" + b"\xff" + b"b" * 255 + b"\x00"),
    ),
)
def test_ens_encode_name(name, expected):
    assert ens_encode_name(name) == expected


@pytest.mark.parametrize(
    "name,expected",
    (
        (
            f"{'a' * 63}.{'b' * 63}.{'c' * 63}.{'d' * 63}.{'e' * 63}.{'f' * 63}.{'g' * 63}",  # noqa: E501
            b"".join([b"?" + to_bytes(text=label) * 63 for label in "abcdefg"])
            + b"\x00",
        ),
        (
            f"{'a-1' * 21}.{'b-2' * 21}.{'c-3' * 21}.{'d-4' * 21}.{'e-5' * 21}.{'f-6' * 21}",  # noqa: E501
            b"".join(
                [
                    b"?" + to_bytes(text=label) * 21
                    for label in [
                        "a-1",
                        "b-2",
                        "c-3",
                        "d-4",
                        "e-5",
                        "f-6",
                    ]
                ]
            )
            + b"\x00",
        ),
    ),
)
def test_ens_encode_name_validating_total_encoded_name_size(name, expected):
    # This test is important because dns validation technically limits the
    # total encoded domain name size to 255. ENSIP-10 expects the name to be
    # DNS encoded with one of the validation exceptions being that the
    # total encoded size can be any length.
    ens_encoded = ens_encode_name(name)
    assert len(ens_encoded) > 255
    assert ens_encoded == expected


@pytest.mark.parametrize("empty_name", ("", ".", None, " ", "  "))
def test_ens_encode_name_returns_single_zero_byte_for_empty_name(empty_name):
    assert ens_encode_name(empty_name) == b"\00"


@pytest.mark.parametrize(
    "name,invalid_label_index",
    (
        ("a" * 256, 0),
        (f"{'a' * 256}.b", 0),
        (f"a.{'a-b1' * 64}x", 1),
        (f"{'a' * 256}.{'1' * 255}.{'b' * 255}", 0),
        (f"{'a' * 255}.{'1' * 256}.{'b' * 255}", 1),
        (f"{'a' * 255}.{'1' * 255}.{'b' * 256}", 2),
    ),
)
def test_ens_encode_name_raises_ValidationError_on_label_lengths_over_63(
    name, invalid_label_index
):
    with pytest.raises(
        ENSValidationError, match=f"Label at position {invalid_label_index} too long"
    ):
        ens_encode_name(name)


def test_ens_encode_name_normalizes_name_before_encoding():
    assert ens_encode_name("Öbb.at") == ens_encode_name("öbb.at")
    assert ens_encode_name("nhÉéÉéÉé.eth") == ens_encode_name("nhéééééé.eth")
    assert ens_encode_name("TESTER.eth") == ens_encode_name("tester.eth")
    assert ens_encode_name("test\u200btest.com") == ens_encode_name("testtest.com")
    assert ens_encode_name("O\u0308bb.at") == ens_encode_name("öbb.at")


@pytest.mark.parametrize(
    "name,hashed",
    (
        (None, "0x" + ("00" * 32)),
        ("", "0x" + ("00" * 32)),
        ("eth", "0x93cdeb708b7545dc668eb9280176169d1c33cfd8ed6f04690a0bcc88a93fc4ae"),
        (
            "foo.eth",
            "0xde9b09fd7c5f901e23a3f19fecc54828e9c848539801e86591bd9801b019f84f",
        ),
    ),
)
def test_normal_name_to_hash(name, hashed):
    assert normal_name_to_hash(name).hex() == hashed


@pytest.mark.parametrize(
    "utility_method",
    (
        normalize_name,
        is_valid_name,
        BaseENS.namehash,
        BaseENS.nameprep,
        ens_encode_name,
        raw_name_to_hash,
    ),
)
def test_name_utility_methods_with_ensip15_flag(utility_method):
    # we already have tests for `normalize_name_ensip15` so we just need to make sure
    # that the flag is passed through to that function
    name = ENSIP15_NORMALIZED_TESTER_DOT_ETH.as_text

    with patch("ens.utils.normalize_name_ensip15") as normalize_name_ensip15_mock:
        with pytest.warns(FutureWarning, match="ENSIP-15"):
            # also asserts ensip15 flag is False by default
            utility_method(name)
            normalize_name_ensip15_mock.assert_not_called()

    with patch("ens.utils.normalize_name_ensip15") as normalize_name_ensip15_mock:
        normalize_name_ensip15_mock.return_value = ENSIP15_NORMALIZED_TESTER_DOT_ETH

        utility_method(name, ensip15=True)
        normalize_name_ensip15_mock.assert_called_once_with(name)


def test_label_to_hash_with_ensip15_flag():
    # we already have tests for `normalize_name_ensip15` so we just need to make sure
    # that the flag is passed through to that function
    for label in ENSIP15_NORMALIZED_TESTER_DOT_ETH.labels:
        normalized_label = ENSNormalizedName([label])

        with patch("ens.utils.normalize_name_ensip15") as normalize_name_ensip15_mock:
            with pytest.warns(FutureWarning, match="ENSIP-15"):
                # also asserts ensip15 flag is False by default
                label_to_hash(label.text)
                normalize_name_ensip15_mock.assert_not_called()

        with patch("ens.utils.normalize_name_ensip15") as normalize_name_ensip15_mock:
            normalize_name_ensip15_mock.return_value = normalized_label

            label_to_hash(label.text, ensip15=True)
            normalize_name_ensip15_mock.assert_called_once_with(label.text)


# -- async -- #


@pytest.mark.asyncio
async def test_init_async_web3_adds_expected_async_middlewares():
    async_w3 = init_async_web3()
    middlewares = map(str, async_w3.manager.middleware_onion)
    assert "stalecheck_middleware" in next(middlewares)


@pytest.mark.asyncio
async def test_init_async_web3_adds_async_eth():
    async_w3 = init_async_web3()
    assert isinstance(async_w3.eth, AsyncEth)


@pytest.mark.asyncio
async def test_init_async_web3_with_provider_argument_adds_async_eth():
    async_w3 = init_async_web3(AsyncEthereumTesterProvider())

    assert isinstance(async_w3.provider, AsyncEthereumTesterProvider)
    assert isinstance(async_w3.eth, AsyncEth)

    latest_block = await async_w3.eth.get_block("latest")
    assert latest_block
    assert is_integer(latest_block["number"])
