from typing import Final


DEFAULT_HTTP_TIMEOUT: Final = 30.0


def construct_user_agent(
    module: str,
    class_name: str,
) -> str:
    from faster_web3 import (
        __version__ as web3_version,
    )

    return f"faster_web3.py/{web3_version}/{module}.{class_name}"
