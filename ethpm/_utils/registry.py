import json
from typing import Any, Dict


def is_ens_domain(authority: str) -> bool:
    """
    Return false if authority is not a valid ENS domain.
    """
    # check that authority ends with the tld '.eth'
    # check that there are either 2 or 3 subdomains in the authority
    # i.e. zeppelinos.eth or packages.zeppelinos.eth
    if authority[-4:] != ".eth" or len(authority.split(".")) not in [2, 3]:
        return False
    return True


def fetch_standard_registry_abi() -> Dict[str, Any]:
    """
    Return the standard Registry ABI to interact with a deployed Registry.
    TODO: Update once the standard is finalized via ERC process.
    """
    # In-lining abi here since it needs to be updated to a registry conforming to
    # https://github.com/ethereum/EIPs/issues/1319
    return json.loads(
        '[{"constant":true,"inputs":[{"name":"_name","type":"bytes32"}],"name":"lookupPackage","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"index","outputs":[{"name":"uri","type":"string"},{"name":"version","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"bytes32"},{"name":"_version","type":"string"},{"name":"_uri","type":"string"}],"name":"registerPackage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501
    )
