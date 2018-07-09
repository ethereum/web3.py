import math


def percentile(values, percentile):
    if not values:
        raise ValueError("Expected a sequence of values, got {0}".format(values))
    if not percentile:
        raise ValueError("Expected a percentile choice, got {0}".format(percentile))

    index = len(values) * percentile / 100
    sorted_values = sorted(values)
    if index % 2 == 0:
        return (sorted_values[index] + sorted_values[index + 1]) / 2

    return sorted_values[math.ceil(index)]
