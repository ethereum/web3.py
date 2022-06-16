from typing import (
    Optional,
    Sequence,
)

from web3.exceptions import (
    InsufficientData,
)


def percentile(
    values: Optional[Sequence[int]] = None, percentile: Optional[float] = None
) -> float:
    """Calculates a simplified weighted average percentile"""
    if values in [None, tuple(), []] or len(values) < 1:
        raise InsufficientData(
            f"Expected a sequence of at least 1 integers, got {values!r}"
        )
    if percentile is None:
        raise ValueError(f"Expected a percentile choice, got {percentile}")

    sorted_values = sorted(values)

    rank = len(values) * percentile / 100
    if rank > 0:
        index = rank - 1
        if index < 0:
            return sorted_values[0]
    else:
        index = rank

    if index % 1 == 0:
        return sorted_values[int(index)]
    else:
        fractional = index % 1
        integer = int(index - fractional)
        lower = sorted_values[integer]
        higher = sorted_values[integer + 1]
        return lower + fractional * (higher - lower)
