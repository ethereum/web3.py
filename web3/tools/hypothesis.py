from hypothesis import (
    strategies as st,
)


def hexstr_strategy():
    return st.from_regex(r'\A(0[xX])?[0-9a-fA-F]*\Z')
