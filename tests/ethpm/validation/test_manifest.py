import pytest

from ethpm.exceptions import (
    EthPMValidationError,
)
from ethpm.validation.manifest import (
    extract_contract_types_from_deployments,
    validate_manifest_against_schema,
    validate_manifest_deployments,
    validate_meta_object,
    validate_raw_manifest_format,
)
from ethpm.validation.package import (
    validate_manifest_version,
    validate_package_name,
)


def test_validate_raw_manifest_configuration_validates_strict_manifests(
    all_strict_manifests
):
    assert validate_raw_manifest_format(all_strict_manifests) is None


def test_validate_raw_manifest_format_invalidates_pretty_manifests(
    all_pretty_manifests
):
    with pytest.raises(EthPMValidationError):
        validate_raw_manifest_format(all_pretty_manifests)


@pytest.mark.parametrize(
    "manifest",
    (
        # not alphabetical
        '{"x":"y","a":"b"}',
        # not UTF-8
        '{"\x80":"b","c":"d"}',
        # newlines
        '{"a":"b",\n"c":"d"}',
        '{"a":"b","c":"d"}\n',
        # whitespace
        '{"a":"b","c": "d"}',
    ),
)
def test_validate_raw_manifest_format_invalidates_invalid_manifests(tmpdir, manifest):
    p = tmpdir.mkdir("invalid").join("manifest.json")
    p.write(manifest)
    invalid_manifest = p.read()
    with pytest.raises(EthPMValidationError):
        validate_raw_manifest_format(invalid_manifest)


def test_validate_manifest_against_all_manifest_types(all_manifests):
    assert validate_manifest_against_schema(all_manifests) is None


def test_validate_manifest_invalidates(invalid_manifest):
    with pytest.raises(EthPMValidationError, match="Manifest invalid for schema"):
        validate_manifest_against_schema(invalid_manifest)


def test_validate_manifest_deployments_catches_missing_contract_type_references(
    manifest_with_conflicting_deployments
):
    with pytest.raises(EthPMValidationError, match="Manifest missing references to contracts"):
        validate_manifest_deployments(manifest_with_conflicting_deployments)


def test_validate_deployments_for_single_deployment(safe_math_lib_package):
    assert validate_manifest_deployments(safe_math_lib_package.manifest) is None


def test_validate_deployments_without_deployment(manifest_with_no_deployments):
    assert validate_manifest_deployments(manifest_with_no_deployments) is None


@pytest.mark.parametrize(
    "data,expected",
    (
        ({}, set()),
        ([{"some": {"contractType": "one"}}], set(["one"])),
        (
            [{"some": {"contractType": "one"}, "other": {"contractType": "two"}}],
            set(["one", "two"]),
        ),
    ),
)
def test_extract_contract_types_from_deployments(data, expected):
    actual = extract_contract_types_from_deployments(data)
    assert actual == expected


def test_validate_manifest_version_validates_version_three_string():
    assert validate_manifest_version("ethpm/3") is None


@pytest.mark.parametrize("version", (2, 3, "2", "3", b"3"))
def test_validate_manifest_version_invalidates_incorrect_versions(version):
    with pytest.raises(EthPMValidationError):
        validate_manifest_version(version)


@pytest.mark.parametrize(
    "meta,extra_fields",
    (
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "A Package that does things.",
                "keywords": ["ethpm", "package"],
                "links": {"documentation": "ipfs://Qm..."},
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "A Package that does things.",
                "keywords": ["ethpm", "package"],
                "links": {"documentation": "ipfs://Qm..."},
                "x-hash": "0x...",
            },
            True,
        ),
    ),
)
def test_validate_meta_object_validates(meta, extra_fields):
    result = validate_meta_object(meta, allow_extra_meta_fields=extra_fields)
    assert result is None


@pytest.mark.parametrize(
    "meta,extra_fields",
    (
        # With allow_extra_meta_fields=False
        ({"invalid": "field"}, False),
        ({"license": 123}, False),
        ({"license": "MIT", "authors": "auther@gmail.com"}, False),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": ["description", "of", "package"],
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "description",
                "keywords": "singlekw",
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "description",
                "keywords": ["auth", "package"],
                "links": ["ipfs://Qm"],
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "description",
                "keywords": ["auth", "package"],
                "links": {"documentation": "ipfs://Qm"},
                "extra": "field",
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "description",
                "keywords": ["auth", "package"],
                "links": {"documentation": "ipfs://Qm"},
                "x-hash": "0x",
            },
            False,
        ),
        # With allow_extra_meta_fields=True
        # Improperly formatted "x" field
        ({"license": "MIT", "extra": "field"}, True),
    ),
)
def test_validate_meta_object_invalidates(meta, extra_fields):
    with pytest.raises(EthPMValidationError):
        validate_meta_object(meta, allow_extra_meta_fields=extra_fields)


@pytest.mark.parametrize(
    "package_name",
    (
        "valid",
        "Valid",
        "pkg1",
        "pkg_1",
        "pkg-1",
        "wallet0",
        "wallet_",
        "wallet-",
        "x" * 256,
    )
)
def test_validate_package_name_with_valid_package_names(package_name):
    assert validate_package_name(package_name) is None


@pytest.mark.parametrize(
    "package_name",
    (
        "",
        "0",
        "_invalid",
        "-invalid",
        ".invalid",
        "wallet.bad",
        "x" * 257,
    )
)
def test_validate_package_name_raises_exception_for_invalid_names(package_name):
    with pytest.raises(EthPMValidationError):
        validate_package_name(package_name)
