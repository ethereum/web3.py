import pytest

from eth_utils import (
    ValidationError,
    to_bytes,
)

from ens.utils import (
    ens_encode_name,
    init_web3,
)


def test_init_adds_middlewares():
    w3 = init_web3()
    middlewares = map(str, w3.manager.middleware_onion)
    assert 'stalecheck_middleware' in next(middlewares)


@pytest.mark.parametrize(
    'name,expected',
    (
        # test some allowed cases
        ('tester.eth', b'\x06tester\x03eth\x00'),
        (
            'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p',
            b'\x01a\x01b\x01c\x01d\x01e\x01f\x01g\x01h\x01i\x01j\x01k\x01l\x01m\x01n\x01o\x01p\x00'
        ),
        ('1.2.3.4.5.6.7.8.9.10', b'\x011\x012\x013\x014\x015\x016\x017\x018\x019\x0210\x00'),
        ('abc.123.def-456.eth', b'\x03abc\x03123\x07def-456\x03eth\x00'),
        ('abc.123.def-456.eth', b'\x03abc\x03123\x07def-456\x03eth\x00'),
        ('nhéééééé.eth', b'\x0enh\xc3\xa9\xc3\xa9\xc3\xa9\xc3\xa9\xc3\xa9\xc3\xa9\x03eth\x00'),
        ('🌈rainbow.eth', b'\x0b\xf0\x9f\x8c\x88rainbow\x03eth\x00'),
        ('🐔🐔.tk', b'\x08\xf0\x9f\x90\x94\xf0\x9f\x90\x94\x02tk\x00'),

        # test that label length may be less than 255
        (f"{'a' * 255}.b", b'\xff' + (b'a' * 255) + b'\x01b\x00'),
        (f"a.{'b' * 255}", b'\x01a' + b'\xff' + (b'b' * 255) + b'\x00'),
        (f"abc-123.{'b' * 255}", b'\x07abc-123' + b'\xff' + b'b' * 255 + b'\x00'),
    )
)
def test_ens_encode_name(name, expected):
    assert ens_encode_name(name) == expected


@pytest.mark.parametrize(
    'name,expected',
    (
        (
            f"{'a' * 63}.{'b' * 63}.{'c' * 63}.{'d' * 63}.{'e' * 63}.{'f' * 63}.{'g' * 63}",
            b''.join([b'?' + to_bytes(text=label) * 63 for label in 'abcdefg']) + b'\x00'
        ),
        (
            f"{'a-1' * 21}.{'b-2' * 21}.{'c-3' * 21}.{'d-4' * 21}.{'e-5' * 21}.{'f-6' * 21}",
            b''.join([
                b'?' + to_bytes(text=label) * 21 for label in [
                    'a-1', 'b-2', 'c-3', 'd-4', 'e-5', 'f-6',
                ]
            ]) + b'\x00'
        ),
    )
)
def test_ens_encode_name_validating_total_encoded_name_size(name, expected):
    # This test is important because dns validation technically limits the total encoded domain name
    # size to 255. ENSIP-10 expects the name to be DNS encoded with one of the validation exceptions
    # being that the total encoded size can be any length.
    ens_encoded = ens_encode_name(name)
    assert len(ens_encoded) > 255
    assert ens_encoded == expected


@pytest.mark.parametrize('empty_name', ('', '.'))
def test_ens_encode_name_returns_single_zero_byte_for_empty_name(empty_name):
    assert ens_encode_name(empty_name) == b'\00'


@pytest.mark.parametrize(
    'name,invalid_label_index',
    (
        ('a' * 256, 0),
        (f"{'a' * 256}.b", 0),
        (f"a.{'a-b1' * 64}x", 1),
        (f"{'a' * 256}.{'1' * 255}.{'b' * 255}", 0),
        (f"{'a' * 255}.{'1' * 256}.{'b' * 255}", 1),
        (f"{'a' * 255}.{'1' * 255}.{'b' * 256}", 2),
    )
)
def test_ens_encode_name_raises_ValidationError_on_label_lengths_over_63(name, invalid_label_index):
    with pytest.raises(ValidationError, match=f'Label at position {invalid_label_index} too long'):
        ens_encode_name(name)


def test_ens_encode_name_normalizes_name_before_encoding():
    assert ens_encode_name('Öbb.at') == ens_encode_name('öbb.at')
    assert ens_encode_name('nhÉéÉéÉé.eth') == ens_encode_name('nhéééééé.eth')
    assert ens_encode_name('TESTER.eth') == ens_encode_name('tester.eth')
    assert ens_encode_name('test\u200btest.com') == ens_encode_name('testtest.com')
    assert ens_encode_name("O\u0308bb.at") == ens_encode_name("öbb.at")
