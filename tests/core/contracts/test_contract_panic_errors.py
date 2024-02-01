import pytest
import re

from tests.core.contracts.utils import (
    deploy,
)
from web3._utils.contract_sources.contract_data.panic_errors_contract import (
    PANIC_ERRORS_CONTRACT_DATA,
)
from web3._utils.error_formatters_utils import (
    PANIC_ERROR_CODES,
)
from web3.exceptions import (
    ContractPanicError,
)


@pytest.fixture
def panic_errors_contract(w3, address_conversion_func):
    panic_errors_contract_factory = w3.eth.contract(**PANIC_ERRORS_CONTRACT_DATA)
    return deploy(w3, panic_errors_contract_factory, address_conversion_func)


@pytest.mark.parametrize(
    "panic_error,params",
    (
        ("01", []),
        ("11", []),
        ("12", [0]),
        ("21", [-1]),
        ("22", []),
        ("31", []),
        ("32", []),
        ("41", []),
        ("51", []),
    ),
)
def test_contract_panic_errors(
    w3,
    panic_errors_contract,
    panic_error,
    params,
):
    method = getattr(panic_errors_contract.functions, f"errorCode{panic_error}")
    error_msg = PANIC_ERROR_CODES[panic_error]

    with pytest.raises(ContractPanicError, match=re.escape(error_msg)):
        method(*params).call()
