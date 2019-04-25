import pytest

from eth_utils import (
    is_address,
)

from web3.pm import (
    ERCRegistry,
    VyperReferenceRegistry,
)


def test_vyper_registry_deploy_new_instance(w3):
    registry = VyperReferenceRegistry.deploy_new_instance(w3)
    assert isinstance(registry, ERCRegistry)
    assert isinstance(registry, VyperReferenceRegistry)
    assert is_address(registry.address)


def test_vyper_registry_auth(w3):
    registry = VyperReferenceRegistry.deploy_new_instance(w3)
    assert registry.owner() == w3.eth.accounts[0]
    registry.transfer_owner(w3.eth.accounts[1])
    assert registry.owner() == w3.eth.accounts[1]


@pytest.mark.parametrize(
    "registry_getter", ["empty_vy_registry", "empty_sol_registry"], indirect=True
)
def test_registry_releases_properly(registry_getter):
    registry = registry_getter
    release_id_1 = registry._release(
        "package", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    )
    release_id_2 = registry._release(
        "package1", "1.0.1", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGZ"
    )
    release_data_1 = registry._get_release_data(release_id_1)
    release_data_2 = registry._get_release_data(release_id_2)
    assert release_data_1[0] == "package"
    assert release_data_1[1] == "1.0.0"
    assert release_data_1[2] == "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    assert release_data_2[0] == "package1"
    assert release_data_2[1] == "1.0.1"
    assert release_data_2[2] == "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGZ"


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_registry_get_all_package_ids_and_get_package_name(registry_getter):
    registry, expected_ids, _ = registry_getter
    package_ids = registry._get_all_package_ids()
    assert len(package_ids) == 6
    assert package_ids[0] == expected_ids[0]
    assert package_ids[1] == expected_ids[1]
    assert package_ids[2] == expected_ids[2]
    assert registry._get_package_name(package_ids[0]) == "package"
    assert registry._get_package_name(package_ids[1]) == "package1"
    assert registry._get_package_name(package_ids[2]) == "package2"


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_registry_get_release_id_and_get_all_release_ids(registry_getter):
    registry, _, expected_ids = registry_getter
    release_ids = registry._get_all_release_ids("package")
    assert len(release_ids) == 6
    assert release_ids[:3] == expected_ids[:3]
    assert registry._get_release_id("package", "1.0.0") == expected_ids[0]
    assert registry._get_release_id("package", "1.0.1") == expected_ids[1]
    assert registry._get_release_id("package", "1.0.2") == expected_ids[2]


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_registry_num_package_ids(registry_getter):
    registry, _, _ = registry_getter
    assert registry._num_package_ids() == 6


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_registry_num_release_ids(registry_getter):
    registry, _, _ = registry_getter
    assert registry._num_release_ids("package") == 6
    assert registry._num_release_ids("package1") == 1
    assert registry._num_release_ids("package2") == 1


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_registry_generate_release_id(registry_getter):
    registry, _, expected_ids = registry_getter
    assert registry._generate_release_id("package", "1.0.0") == expected_ids[0]
    assert registry._generate_release_id("package", "1.0.1") == expected_ids[1]
    assert registry._generate_release_id("package", "1.0.2") == expected_ids[2]
    assert registry._generate_release_id("does-not-exist", "1.0.0") == expected_ids[3]


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_registry_get_release_data(registry_getter):
    registry, _, release_ids = registry_getter
    release_data_1 = registry._get_release_data(release_ids[0])
    release_data_2 = registry._get_release_data(release_ids[1])
    release_data_3 = registry._get_release_data(release_ids[2])
    assert release_data_1 == (
        "package",
        "1.0.0",
        "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV",
    )
    assert release_data_2 == (
        "package",
        "1.0.1",
        "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGW",
    )
    assert release_data_3 == (
        "package",
        "1.0.2",
        "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGX",
    )
