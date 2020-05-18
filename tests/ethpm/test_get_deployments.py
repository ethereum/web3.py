import pytest

from ethpm import (
    Package,
)
from ethpm.deployments import (
    Deployments,
)
from ethpm.exceptions import (
    EthPMValidationError,
)


def test_get_deployments_with_no_deployments(w3, manifest_with_empty_deployments):
    package = Package(manifest_with_empty_deployments, w3)
    assert package.deployments == {}


def test_get_deployments_with_no_deployments_raises_exception(
    w3, manifest_with_no_deployments
):
    package = Package(manifest_with_no_deployments, w3)
    assert package.deployments == {}


def test_get_deployments_with_no_match_raises_exception(
    manifest_with_no_matching_deployments, w3
):
    package = Package(manifest_with_no_matching_deployments, w3)
    with pytest.raises(EthPMValidationError, match="Package has no matching URIs on chain."):
        package.deployments


def test_get_deployments_with_multiple_matches_raises_exception(
    manifest_with_multiple_matches, w3
):
    package = Package(manifest_with_multiple_matches, w3)
    with pytest.raises(EthPMValidationError, match="Package has too many \\(2\\) matching URIs"):
        package.deployments


def test_get_deployments_with_a_match_returns_deployments(w3, safe_math_lib_package):
    deployment = safe_math_lib_package.deployments
    assert isinstance(deployment, Deployments)
    assert "SafeMathLib" in deployment
