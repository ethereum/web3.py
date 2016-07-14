import decimal


units = {
    'wei':          decimal.Decimal('1'),
    'kwei':         decimal.Decimal('1000'),
    'babbage':      decimal.Decimal('1000'),
    'femtoether':   decimal.Decimal('1000'),
    'mwei':         decimal.Decimal('1000000'),
    'lovelace':     decimal.Decimal('1000000'),
    'picoether':    decimal.Decimal('1000000'),
    'gwei':         decimal.Decimal('1000000000'),
    'shannon':      decimal.Decimal('1000000000'),
    'nanoether':    decimal.Decimal('1000000000'),
    'nano':         decimal.Decimal('1000000000'),
    'szabo':        decimal.Decimal('1000000000000'),
    'microether':   decimal.Decimal('1000000000000'),
    'micro':        decimal.Decimal('1000000000000'),
    'finney':       decimal.Decimal('1000000000000000'),
    'milliether':   decimal.Decimal('1000000000000000'),
    'milli':        decimal.Decimal('1000000000000000'),
    'ether':        decimal.Decimal('1000000000000000000'),
    'kether':       decimal.Decimal('1000000000000000000000'),
    'grand':        decimal.Decimal('1000000000000000000000'),
    'mether':       decimal.Decimal('1000000000000000000000000'),
    'gether':       decimal.Decimal('1000000000000000000000000000'),
    'tether':       decimal.Decimal('1000000000000000000000000000000'),
}

CURRENCY_CONTEXT = decimal.Context(prec=60, rounding=decimal.ROUND_DOWN)


def from_wei(number, unit):
    """
    Takes a number of wei and converts it to any other ether unit.
    """
    if unit.lower() not in units:
        raise ValueError(
            "Unknown unit.  Must be one of {0}".format('/'.join(units.keys()))
        )

    d_number = CURRENCY_CONTEXT.create_decimal(number)
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
    d_number = CURRENCY_CONTEXT.create_decimal(number)
    unit_value = units[unit.lower()]

    return d_number * unit_value
