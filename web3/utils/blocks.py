from .types import is_string
from .string import force_text


def is_predefined_block_number(block_number):
    if not is_string(block_number):
        return False
    return force_text(block_number) in {"latest", "pending", "earliest"}
