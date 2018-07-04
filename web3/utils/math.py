import math


def percentile(values, percentile):
    if not values:
        return None
    index = len(values) * percentile / 100
    sorted_values = sorted(values)
    if index % 2 == 0:
        return (sorted_values[index] + sorted_values[index + 1]) / 2

    return sorted_values[math.ceil(index)]
