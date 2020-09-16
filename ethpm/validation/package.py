import re
from typing import (
    Any,
    Dict,
)

from eth_utils import (
    is_text,
)

from ethpm._utils.ipfs import (
    is_ipfs_uri,
)
from ethpm.constants import (
    PACKAGE_NAME_REGEX,
)
from ethpm.exceptions import (
    EthPMValidationError,
    InsufficientAssetsError,
)


def validate_minimal_contract_factory_data(contract_data: Dict[str, str]) -> None:
    """
    Validate that contract data in a package contains at least an "abi" and
    "deploymentBytecode" necessary to generate a deployable contract factory.
    """
    if not all(key in contract_data.keys() for key in ("abi", "deploymentBytecode")):
        raise InsufficientAssetsError(
            "Minimum required contract data to generate a deployable "
            "contract factory (abi & deploymentBytecode) not found."
        )


def validate_package_version(version: Any) -> None:
    """
    Validates that a package version is of text type.
    """
    if not is_text(version):
        raise EthPMValidationError(
            f"Expected a version of text type, instead received {type(version)}."
        )


def validate_package_name(pkg_name: str) -> None:
    """
    Raise an exception if the value is not a valid package name
    as defined in the EthPM-Spec.
    """
    if not bool(re.match(PACKAGE_NAME_REGEX, pkg_name)):
        raise EthPMValidationError(f"{pkg_name} is not a valid package name.")


def validate_manifest_version(version: str) -> None:
    """
    Raise an exception if the version is not "ethpm/3".
    """
    if not version == "ethpm/3":
        raise EthPMValidationError(
            f"Py-EthPM does not support the provided specification version: {version}"
        )


def validate_build_dependency(key: str, uri: str) -> None:
    """
    Raise an exception if the key in dependencies is not a valid package name,
    or if the value is not a valid IPFS URI.
    """
    validate_package_name(key)
    # validate is supported content-addressed uri
    if not is_ipfs_uri(uri):
        raise EthPMValidationError(f"URI: {uri} is not a valid IPFS URI.")


CONTRACT_NAME_REGEX = re.compile("^[a-zA-Z][-a-zA-Z0-9_]{0,255}$")


def validate_contract_name(name: str) -> None:
    if not CONTRACT_NAME_REGEX.match(name):
        raise EthPMValidationError(f"Contract name: {name} is not valid.")
