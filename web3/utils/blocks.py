from eth_utils import (
    is_string,
    force_text,
)


def is_predefined_block_number(block_number):
    if not is_string(block_number):
        return False
    return force_text(block_number) in {"latest", "pending", "earliest"}
