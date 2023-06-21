import json
import os
import pytest

from ens import (
    InvalidName,
)
from ens._normalization import (
    normalize_name_ensip15,
)

NORMALIZATION_TESTS_PATH = os.path.join(
    os.path.dirname(__file__), "normalization_tests.json"
)
with open(NORMALIZATION_TESTS_PATH) as f:
    normalization_tests = json.load(f)

POSITIVE_TEST_CASES = [test for test in normalization_tests if "error" not in test]
NEGATIVE_TEST_CASES = [test for test in normalization_tests if "error" in test]

# gut check that we have all the tests
if not len(POSITIVE_TEST_CASES) + len(NEGATIVE_TEST_CASES) == len(normalization_tests):
    raise AssertionError("Not all normalization tests are accounted for.")


@pytest.mark.parametrize(
    "positive_test_case",
    POSITIVE_TEST_CASES,
    ids=lambda t: t["name"],
)
def test_normalize_name_ensip15_positive_test_cases(positive_test_case):
    name = positive_test_case["name"]

    expected = positive_test_case.get("norm", positive_test_case.get("name"))
    assert normalize_name_ensip15(name).as_text == expected


@pytest.mark.parametrize(
    "negative_test_case",
    NEGATIVE_TEST_CASES,
    ids=lambda t: t["name"],
)
def test_normalize_name_ensip15_negative_test_cases(negative_test_case):
    name = negative_test_case["name"]

    with pytest.raises(InvalidName):
        normalize_name_ensip15(name)
