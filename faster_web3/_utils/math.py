from typing import (
    Sequence,
)

from faster_web3.exceptions import (
    InsufficientData,
    Web3ValueError,
)


def percentile(values: Sequence[int], percentile: float) -> float:
    """Calculates a simplified weighted average percentile"""
    if not values:
        raise InsufficientData(
            f"Expected a sequence of at least 1 integers, got {values!r}"
        )
    if percentile < 0 or percentile > 100:
        raise Web3ValueError("percentile must be in the range [0, 100]")

    sorted_values = sorted(values)

    index = len(values) * percentile / 100 - 1
    if index < 0:
        return sorted_values[0]

    fractional = index % 1
    if fractional == 0:
        return sorted_values[int(index)]

    integer = int(index - fractional)
    lower = sorted_values[integer]
    higher = sorted_values[integer + 1]
    return lower + fractional * (higher - lower)
