def _trim_trailing_zeros(value: str) -> str:
    if value[-1] != '0':
        return value
    else:
        return _trim_trailing_zeros(value[:-1])


def parseUnits(value: str, decimals: int) -> int:
    """
    Parse formatted decimal string `value` to an `int` considering
    the provided `decimal` places.
    This can be used to convert a formatted string to a numeric
    value in the smallest denomination of the asset, e.g.
    ```
    parseUnits("1.5", 18) -> 1500000000000000000
    ```
    """
    value = _trim_trailing_zeros(value)
    decimals_pos = value.find('.')
    if decimals_pos == -1:
        return int(value+"0"*decimals)
    else:
        return int(value[0:decimals_pos]
                    + value[decimals_pos+1:]
                    + "0"*(decimals - len(value[decimals_pos+1:])))


def formatUnits(value: int, decimals: int) -> str:
    """
    Format a `value` in the smallest denomination of an asset
    to a higher denomination, by providing the `decimal`
    places that should be considered.
    This can be used to convert a value in wei to a formatted
    string in ETH.
    ```
    formatUnits(1500000000000000000, 18) -> "1.5"
    ```
    """
    value = str(value)
    if len(value) > decimals:
        return _trim_trailing_zeros(value[0:len(value)-decimals]
                                    + "." + value[len(value)-decimals:])
    else:
        return _trim_trailing_zeros("0." + "0"*(decimals-len(value))+value)


def formatEther(value: int) -> str:
    """
    Convert a value in wei to a formatted string in ETH.
    """
    return formatUnits(value, 18)


def parseEther(value: str) -> int:
    """
    Parse an formatted string in ETH to a value in wei
    """
    return parseUnits(value, 18)
