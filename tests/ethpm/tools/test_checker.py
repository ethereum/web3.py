import pytest

from ethpm.tools.checker import (
    WARNINGS,
    check_contract_types,
    check_manifest,
    check_meta,
    check_sources,
)


def test_checker_simple():
    warnings = check_manifest({})
    assert warnings == {
        "manifest_version": "Manifest missing a required 'manifest_version' field.",
        "package_name": "Manifest missing a required 'package_name' field",
        "version": "Manifest missing a required 'version' field.",
        "meta": "Manifest missing a suggested 'meta' field.",
        "sources": """Manifest is missing a sources field, which defines a source tree that """
        """should comprise the full source tree necessary to recompile the contracts """
        """contained in this release.""",
        "contract_types": """Manifest does not contain any 'contract_types'. Packages should """
        """only include contract types that can be found in the source files for this """
        """package. Packages should not include contract types from dependencies. """
        """Packages should not include abstract contracts in the contract types section """
        """of a release.""",
    }


BASIC_MANIFEST = {
    "package_name": "package",
    "version": "1.0.0",
    "manifest_version": "2",
}


@pytest.mark.parametrize(
    "manifest,expected",
    (
        ({}, {"meta": WARNINGS["meta_missing"]}),
        ({"meta": {}}, {"meta": WARNINGS["meta_missing"]}),
        (
            {"meta": {"x": "x"}},
            {
                "meta.authors": WARNINGS["authors_missing"],
                "meta.description": WARNINGS["description_missing"],
                "meta.links": WARNINGS["links_missing"],
                "meta.keywords": WARNINGS["keywords_missing"],
                "meta.license": WARNINGS["license_missing"],
            },
        ),
    ),
)
def test_check_meta(manifest, expected):
    warnings = check_meta(manifest, {})
    assert warnings == expected


@pytest.mark.parametrize(
    "manifest,expected",
    (
        # Sad paths
        ({}, {"sources": WARNINGS["sources_missing"]}),
        ({"sources": []}, {"sources": WARNINGS["sources_missing"]}),
        # Happy path
        ({"sources": {"links": "www.github.com"}}, {}),
    ),
)
def test_check_sources(manifest, expected):
    warnings = check_sources(manifest, {})
    assert warnings == expected


@pytest.mark.parametrize(
    "manifest,expected",
    (
        ({}, {"contract_types": WARNINGS["contract_type_missing"]}),
        ({"contract_types": {}}, {"contract_types": WARNINGS["contract_type_missing"]}),
        (
            {"contract_types": {"x": {"runtime_bytecode": {"invalid": "invalid"}}}},
            {
                "contract_types": {
                    "x": {
                        "abi": WARNINGS["abi_missing"].format("x"),
                        "contract_type": WARNINGS[
                            "contract_type_subfield_missing"
                        ].format("x"),
                        "deployment_bytecode": WARNINGS[
                            "deployment_bytecode_missing"
                        ].format("x"),
                        "runtime_bytecode": WARNINGS[
                            "bytecode_subfield_missing"
                        ].format("x", "runtime"),
                        "natspec": WARNINGS["natspec_missing"].format("x"),
                        "compiler": WARNINGS["compiler_missing"].format("x"),
                    }
                }
            },
        ),
        (
            {
                "contract_types": {
                    "x": {
                        "deployment_bytecode": [],
                        "runtime_bytecode": {"bytecode": []},
                    },
                    "y": {
                        "abi": [1],
                        "deployment_bytecode": [],
                        "runtime_bytecode": [],
                    },
                }
            },
            {
                "contract_types": {
                    "x": {
                        "abi": WARNINGS["abi_missing"].format("x"),
                        "contract_type": WARNINGS[
                            "contract_type_subfield_missing"
                        ].format("x"),
                        "deployment_bytecode": WARNINGS[
                            "deployment_bytecode_missing"
                        ].format("x"),
                        "runtime_bytecode": WARNINGS[
                            "bytecode_subfield_missing"
                        ].format("x", "runtime"),
                        "natspec": WARNINGS["natspec_missing"].format("x"),
                        "compiler": WARNINGS["compiler_missing"].format("x"),
                    },
                    "y": {
                        "contract_type": WARNINGS[
                            "contract_type_subfield_missing"
                        ].format("y"),
                        "deployment_bytecode": WARNINGS[
                            "deployment_bytecode_missing"
                        ].format("y"),
                        "runtime_bytecode": WARNINGS["runtime_bytecode_missing"].format(
                            "y"
                        ),
                        "natspec": WARNINGS["natspec_missing"].format("y"),
                        "compiler": WARNINGS["compiler_missing"].format("y"),
                    },
                }
            },
        ),
    ),
)
def test_check_contract_types(manifest, expected):
    warnings = check_contract_types(manifest, {})
    assert warnings == expected
