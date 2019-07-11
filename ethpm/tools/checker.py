import re
from typing import (
    Any,
    Dict,
)

from eth_typing import (
    Manifest,
)
from eth_utils.toolz import (
    assoc,
    assoc_in,
    curry,
)

from ethpm.constants import (
    PACKAGE_NAME_REGEX,
)
from ethpm.tools.builder import (
    build,
)

# todo: validate no duplicate blockchain uris in deployments, if web3 is available

WARNINGS = {
    "manifest_version_missing": "Manifest missing a required 'manifest_version' field.",
    "manifest_version_invalid": "'manifest_version' is invalid. The only supported version is '2'.",
    "package_name_missing": "Manifest missing a required 'package_name' field",
    "package_name_invalid": "'package_name' is invalid. "
    f"Doesn't match the regex: {PACKAGE_NAME_REGEX}",
    "version_missing": "Manifest missing a required 'version' field.",
    "meta_missing": "Manifest missing a suggested 'meta' field.",
    "authors_missing": "'meta' field missing suggested 'authors' field.",
    "description_missing": "'meta' field missing suggested 'description' field.",
    "links_missing": "'meta' field missing suggested 'links' field.",
    "license_missing": "'meta' field missing suggested 'license' field.",
    "keywords_missing": "'meta' field missing suggested 'keywords' field.",
    "sources_missing": """Manifest is missing a sources field, which defines a source tree """
    """that should comprise the full source tree necessary to recompile the contracts """
    """contained in this release.""",
    "contract_type_missing": """Manifest does not contain any 'contract_types'. Packages """
    """should only include contract types that can be found in the source files for this """
    """package. Packages should not include contract types from dependencies. Packages """
    """should not include abstract contracts in the contract types section of a release.""",
    "abi_missing": """Contract type: {0} is missing an abi field, which is essential for using """
    """this package.""",
    "deployment_bytecode_missing": """Contract type: {0} is missing a deployment_bytecode field,"""
    """ which is essential for using this package.""",
    "contract_type_subfield_missing": """Contract type: {0} is missing a contract_type field, """
    """which is essential if an alias is being used to namespace this contract type.""",
    "runtime_bytecode_missing": "Contract type: {0} is missing a runtime_bytecode field.",
    "bytecode_subfield_missing": """Contract type: {0} is missing a required bytecode subfield """
    """in its {1} bytecode object.""",
    "natspec_missing": "Contract type: {0} is missing a natspec field.",
    "compiler_missing": "Contract type: {0} is missing a compiler field.",
}


#
# Validation
#


def check_manifest(manifest: Manifest) -> Dict[str, str]:
    generate_warnings = (
        check_manifest_version(manifest),
        check_package_name(manifest),
        check_version(manifest),
        check_meta(manifest),
        check_sources(manifest),
        check_contract_types(manifest),
    )
    return build({}, *generate_warnings)


#
# Required fields
#


@curry
def check_manifest_version(
    manifest: Manifest, warnings: Dict[str, str]
) -> Dict[str, str]:
    if "manifest_version" not in manifest or not manifest["manifest_version"]:
        return assoc(warnings, "manifest_version", WARNINGS["manifest_version_missing"])
    if manifest["manifest_version"] != "2":
        return assoc(warnings, "manifest_version", WARNINGS["manifest_version_invalid"])
    return warnings


@curry
def check_package_name(manifest: Manifest, warnings: Dict[str, str]) -> Dict[str, str]:
    if "package_name" not in manifest or not manifest["package_name"]:
        return assoc(warnings, "package_name", WARNINGS["package_name_missing"])
    if not bool(re.match(PACKAGE_NAME_REGEX, manifest["package_name"])):
        return assoc(warnings, "package_name", WARNINGS["package_name_invalid"])
    return warnings


@curry
def check_version(manifest: Manifest, warnings: Dict[str, str]) -> Dict[str, str]:
    if "version" not in manifest or not manifest["version"]:
        return assoc(warnings, "version", WARNINGS["version_missing"])
    return warnings


#
# Meta fields
#


@curry
def check_meta(manifest: Manifest, warnings: Dict[str, str]) -> Dict[str, str]:
    if "meta" not in manifest or not manifest["meta"]:
        return assoc(warnings, "meta", WARNINGS["meta_missing"])
    meta_validation = (
        check_authors(manifest["meta"]),
        check_license(manifest["meta"]),
        check_description(manifest["meta"]),
        check_keywords(manifest["meta"]),
        check_links(manifest["meta"]),
    )
    return build(warnings, *meta_validation)


@curry
def check_authors(meta: Dict[str, Any], warnings: Dict[str, str]) -> Dict[str, str]:
    if "authors" not in meta:
        return assoc(warnings, "meta.authors", WARNINGS["authors_missing"])
    return warnings


@curry
def check_license(meta: Dict[str, Any], warnings: Dict[str, str]) -> Dict[str, str]:
    if "license" not in meta or not meta["license"]:
        return assoc(warnings, "meta.license", WARNINGS["license_missing"])
    return warnings


@curry
def check_description(meta: Dict[str, Any], warnings: Dict[str, str]) -> Dict[str, str]:
    if "description" not in meta or not meta["description"]:
        return assoc(warnings, "meta.description", WARNINGS["description_missing"])
    return warnings


@curry
def check_keywords(meta: Dict[str, Any], warnings: Dict[str, str]) -> Dict[str, str]:
    if "keywords" not in meta or not meta["keywords"]:
        return assoc(warnings, "meta.keywords", WARNINGS["keywords_missing"])
    return warnings


@curry
def check_links(meta: Dict[str, Any], warnings: Dict[str, str]) -> Dict[str, str]:
    if "links" not in meta or not meta["links"]:
        return assoc(warnings, "meta.links", WARNINGS["links_missing"])
    return warnings


#
# Sources
#


@curry
def check_sources(manifest: Manifest, warnings: Dict[str, str]) -> Dict[str, str]:
    if "sources" not in manifest or not manifest["sources"]:
        return assoc(warnings, "sources", WARNINGS["sources_missing"])
    return warnings


#
# Contract Types
#

# todo: validate a contract type matches source
@curry
def check_contract_types(
    manifest: Manifest, warnings: Dict[str, str]
) -> Dict[str, str]:
    if "contract_types" not in manifest or not manifest["contract_types"]:
        return assoc(warnings, "contract_types", WARNINGS["contract_type_missing"])

    all_contract_type_validations = (
        (
            check_abi(contract_name, data),
            check_contract_type(contract_name, data),
            check_deployment_bytecode(contract_name, data),
            check_runtime_bytecode(contract_name, data),
            check_natspec(contract_name, data),
            check_compiler(contract_name, data),
        )
        for contract_name, data in manifest["contract_types"].items()
    )
    return build(warnings, *sum(all_contract_type_validations, ()))


@curry
def check_abi(
    contract_name: str, data: Dict[str, Any], warnings: Dict[str, str]
) -> Dict[str, str]:
    if "abi" not in data or not data["abi"]:
        return assoc_in(
            warnings,
            ["contract_types", contract_name, "abi"],
            WARNINGS["abi_missing"].format(contract_name),
        )
    return warnings


@curry
def check_contract_type(
    contract_name: str, data: Dict[str, Any], warnings: Dict[str, str]
) -> Dict[str, str]:
    if "contract_type" not in data or not data["contract_type"]:
        return assoc_in(
            warnings,
            ["contract_types", contract_name, "contract_type"],
            WARNINGS["contract_type_subfield_missing"].format(contract_name),
        )
    return warnings


@curry
def check_deployment_bytecode(
    contract_name: str, data: Dict[str, Any], warnings: Dict[str, str]
) -> Dict[str, str]:
    if "deployment_bytecode" not in data or not data["deployment_bytecode"]:
        return assoc_in(
            warnings,
            ["contract_types", contract_name, "deployment_bytecode"],
            WARNINGS["deployment_bytecode_missing"].format(contract_name),
        )
    return build(
        warnings,
        check_bytecode_object(contract_name, "deployment", data["deployment_bytecode"]),
    )


@curry
def check_runtime_bytecode(
    contract_name: str, data: Dict[str, Any], warnings: Dict[str, str]
) -> Dict[str, str]:
    if "runtime_bytecode" not in data or not data["runtime_bytecode"]:
        return assoc_in(
            warnings,
            ["contract_types", contract_name, "runtime_bytecode"],
            WARNINGS["runtime_bytecode_missing"].format(contract_name),
        )
    return build(
        warnings,
        check_bytecode_object(contract_name, "runtime", data["runtime_bytecode"]),
    )


@curry
def check_bytecode_object(
    contract_name: str,
    bytecode_type: str,
    bytecode_data: Dict[str, Any],
    warnings: Dict[str, str],
) -> Dict[str, str]:
    # todo: check if bytecode has link_refs & validate link_refs present in object
    if "bytecode" not in bytecode_data or not bytecode_data["bytecode"]:
        return assoc_in(
            warnings,
            ["contract_types", contract_name, f"{bytecode_type}_bytecode"],
            WARNINGS["bytecode_subfield_missing"].format(contract_name, bytecode_type),
        )
    return warnings


@curry
def check_natspec(
    contract_name: str, data: Dict[str, Any], warnings: Dict[str, str]
) -> Dict[str, str]:
    if "natspec" not in data or not data["natspec"]:
        return assoc_in(
            warnings,
            ["contract_types", contract_name, "natspec"],
            WARNINGS["natspec_missing"].format(contract_name),
        )
    return warnings


@curry
def check_compiler(
    contract_name: str, data: Dict[str, Any], warnings: Dict[str, str]
) -> Dict[str, str]:
    if "compiler" not in data or not data["compiler"]:
        return assoc_in(
            warnings,
            ["contract_types", contract_name, "compiler"],
            WARNINGS["compiler_missing"].format(contract_name),
        )
    return warnings
