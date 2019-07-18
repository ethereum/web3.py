from web3 import Web3


def validate_w3_instance(w3: Web3) -> None:
    if w3 is None or not isinstance(w3, Web3):
        raise ValueError("Package does not have valid web3 instance.")
