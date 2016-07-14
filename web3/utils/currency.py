import decimal


units = {
    'wei':          decimal.Decimal(1e0),
    'kwei':         decimal.Decimal(1e3),
    'babbage':      decimal.Decimal(1e3),
    'femtoether':   decimal.Decimal(1e3),
    'mwei':         decimal.Decimal(1e6),
    'lovelace':     decimal.Decimal(1e6),
    'picoether':    decimal.Decimal(1e6),
    'gwei':         decimal.Decimal(1e9),
    'shannon':      decimal.Decimal(1e9),
    'nanoether':    decimal.Decimal(1e9),
    'nano':         decimal.Decimal(1e9),
    'szabo':        decimal.Decimal(1e12),
    'microether':   decimal.Decimal(1e12),
    'micro':        decimal.Decimal(1e12),
    'finney':       decimal.Decimal(1e15),
    'milliether':   decimal.Decimal(1e15),
    'milli':        decimal.Decimal(1e15),
    'ether':        decimal.Decimal(1e18),
    'kether':       decimal.Decimal(1e21),
    'grand':        decimal.Decimal(1e21),
    'mether':       decimal.Decimal(1e24),
    'gether':       decimal.Decimal(1e27),
    'tether':       decimal.Decimal(1e30),
}


def from_wei(number, unit):
    """
    Takes a number of wei and converts it to any other ether unit.
    """
    if unit.lower() not in units:
        raise ValueError(
            "Unknown unit.  Must be one of {0}".format('/'.join(units.keys()))
        )

    d_number = decimal.Decimal(number)
    unit_value = units[unit.lower()]

    return d_number / unit_value


def to_wei(number, unit):
    """
    Takes a number of a unit and converts it to wei.
    """
    if unit.lower() not in units:
        raise ValueError(
            "Unknown unit.  Must be one of {0}".format('/'.join(units.keys()))
        )
    d_number = decimal.Decimal(number)
    unit_value = units[unit.lower()]

    return d_number * unit_value
