import json
import os

from ens.utils import normalize_name


NORMALIZATION_TESTS = os.path.join(
    os.path.dirname(__file__), "normalization_tests.json"
)


def test_normalize_name_from_spec_tests():
    with open(NORMALIZATION_TESTS) as f:
        normalization_tests = json.load(f)

    for test_vector in normalization_tests:
        name = test_vector["name"]

        if "error" not in test_vector:
            expected = test_vector.get("norm", test_vector.get("name"))
            assert normalize_name(name) == expected
