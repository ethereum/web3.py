from eth_utils import (
    is_hex,
    is_string,
    is_integer,
    remove_0x_prefix,
    force_text,
)


def is_predefined_block_number(value):
    if not is_string(value):
        return False
    return force_text(value) in {"latest", "pending", "earliest"}


def is_hex_encoded_block_hash(value):
    if not is_string(value):
        return False
    return len(remove_0x_prefix(value)) == 64 and is_hex(value)


def is_hex_encoded_block_number(value):
    if not is_string(value):
        return False
    elif is_hex_encoded_block_hash(value):
        return False
    try:
        value_as_int = int(value, 16)
    except ValueError:
        return False
    return 0 <= value_as_int < 2**256


def select_method_for_block_identifier(value, if_hash, if_number, if_predefined):
    if is_predefined_block_number(value):
        return if_predefined
    elif isinstance(value, bytes):
        return if_hash
    elif is_hex_encoded_block_hash(value):
        return if_hash
    elif is_integer(value) and (0 <= value < 2**256):
        return if_number
    elif is_hex_encoded_block_number(value):
        return if_number
    else:
        raise ValueError(
            "Value did not match any of the recognized block identifiers: {0}".format(value)
        )
