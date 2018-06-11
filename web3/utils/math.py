import math


def percentile(values, percentile):
    if not values:
        return None
    index = len(values) * percentile / 100
    if index % 2 == 0:
        return (sorted(values)[index] + sorted(values)[index + 1]) / 2

    return sorted(values)[math.ceil(index)]
