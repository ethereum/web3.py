from eth_utils import (
    force_bytes,
    force_text,
    is_bytes,
)


def is_prefixed(value, prefix):
    return value.startswith(
        force_bytes(prefix) if is_bytes(value) else force_text(prefix)
    )
