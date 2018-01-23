from hypothesis import (
    given,
    strategies as st,
)

from web3.utils.datastructures import (
    HexBytes,
)
from web3.utils.encoding import (
    to_bytes,
)
from web3.utils.hypothesis import (
    hexstr_strategy,
)


@given(st.binary())
def test_hexbytes_equals_bytes(bytesval):
    assert HexBytes(bytesval) == bytesval


@given(hexstr_strategy())
def test_hexbytes_hexstr_to_bytes(hexstr):
    assert HexBytes(hexstr) == to_bytes(hexstr=hexstr)
