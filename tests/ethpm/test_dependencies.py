import pytest

from ethpm import (
    Package,
)
from ethpm.dependencies import (
    Dependencies,
)
from ethpm.exceptions import (
    EthPMValidationError,
)
from ethpm.validation.package import (
    validate_build_dependency,
)


@pytest.fixture
def dependencies(dummy_ipfs_backend, piper_coin_manifest, w3):
    deps = piper_coin_manifest["buildDependencies"]
    dep_pkgs = {dep: Package.from_uri(uri, w3) for dep, uri in deps.items()}
    return Dependencies(dep_pkgs)


@pytest.fixture
def safe_math_lib_package(safe_math_manifest, w3):
    return Package(safe_math_manifest, w3)


def test_dependencies_implements_getitem(dependencies, safe_math_lib_package):
    assert dependencies["standard-token"].name == "standard-token"


def test_dependencies_items(dependencies):
    result = dependencies.items()
    for key, value in result:
        assert key == value.name
        assert isinstance(value, Package)


def test_dependencies_values(dependencies):
    result = dependencies.values()
    for value in result:
        assert isinstance(value, Package)


def test_get_dependency_package(dependencies):
    result = dependencies.get_dependency_package("standard-token")
    assert isinstance(result, Package)
    assert result.name == "standard-token"


def test_validate_build_dependencies(dummy_ipfs_backend):
    result = validate_build_dependency(
        "standard-token", "ipfs://QmVu9zuza5mkJwwcFdh2SXBugm1oSgZVuEKkph9XLsbUwg"
    )
    assert result is None


@pytest.mark.parametrize(
    "name,uri",
    (
        ("standard-token", "invalid_ipfs_uri"),
        ("_invalid_pkg_name", "ipfs://QmVu9zuza5mkJwwcFdh2SXBugm1oSgZVuEKkph9XLsbUwg"),
        ("_invalid_pkg_name", "ipfs://QmVu9zuza5mkJwwcFdh2SXBugm1oSgZVuEKkph9XLsbUwg"),
    ),
)
def test_get_build_dependencies_invalidates(name, uri):
    with pytest.raises(EthPMValidationError):
        validate_build_dependency(name, uri)
