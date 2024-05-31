DEFAULT_HTTP_TIMEOUT = 30.0


def construct_user_agent(class_type: type) -> str:
    from web3 import (
        __version__ as web3_version,
    )

    return f"web3.py/{web3_version}/{class_type.__module__}.{class_type.__qualname__}"
