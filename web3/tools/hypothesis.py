from hypothesis import (  # noqa: F401
    example,
    given,
    settings,
    strategies,
)


def hexstr_strategy():
    return strategies.from_regex(r'\A(0[xX])?[0-9a-fA-F]*\Z')
