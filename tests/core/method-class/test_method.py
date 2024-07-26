from inspect import (
    isclass,
)
import pytest

from eth_utils.toolz import (
    compose,
)

from web3 import (
    EthereumTesterProvider,
    Web3,
)
from web3.exceptions import (
    Web3ValidationError,
    Web3ValueError,
)
from web3.method import (
    Method,
    _apply_request_formatters,
    default_root_munger,
)
from web3.module import (
    Module,
    apply_result_formatters,
)


def test_method_accepts_callable_for_selector():
    method = Method(
        mungers=[],
        json_rpc_method=lambda *_: "eth_method",
    )
    assert method.method_selector_fn() == "eth_method"


def test_method_selector_fn_accepts_str():
    method = Method(
        is_property=True,
        json_rpc_method="eth_method",
    )
    assert method.method_selector_fn() == "eth_method"


def test_method_selector_fn_invalid_arg():
    with pytest.raises(Web3ValueError):
        method = Method(
            mungers=[],
            json_rpc_method=555555,
        )
        method.method_selector_fn()


def test_get_formatters_default_formatter_for_falsy_config():
    method = Method(
        mungers=[],
        json_rpc_method="eth_method",
    )

    default_request_formatters = method.request_formatters(method.method_selector_fn())
    default_result_formatters = method.result_formatters(
        method.method_selector_fn(), "some module"
    )
    assert _apply_request_formatters(["a", "b", "c"], default_request_formatters) == (
        "a",
        "b",
        "c",
    )
    assert apply_result_formatters(default_result_formatters, ["a", "b", "c"]) == [
        "a",
        "b",
        "c",
    ]


def test_get_formatters_non_falsy_config_retrieval():
    method = Method(
        mungers=[],
        json_rpc_method="eth_getBalance",
    )
    method_name = method.method_selector_fn()
    first_formatter = (method.request_formatters(method_name).first,)
    all_other_formatters = method.request_formatters(method_name).funcs
    assert len(first_formatter + all_other_formatters) == 2
    assert (method.request_formatters("eth_getBalance").first,) == first_formatter


def test_input_munger_parameter_passthrough_matching_arity():
    method = Method(
        mungers=[lambda m, z, y: ["success"]],
        json_rpc_method="eth_method",
    )
    assert method.input_munger(object(), ["first", "second"], {}) == ["success"]


def test_input_munger_parameter_passthrough_mismatch_arity():
    method = Method(
        mungers=[lambda m, z, y: "success"],
        json_rpc_method="eth_method",
    )
    with pytest.raises(TypeError):
        method.input_munger(object(), ["first", "second", "third"], {})


def test_default_input_munger_with_no_input_parameters():
    method = Method(
        json_rpc_method="eth_method",
    )
    assert method.input_munger(object(), [], {}) == []


@pytest.mark.parametrize(
    "empty", ([], (), None), ids=["empty-list", "empty-tuple", "None"]
)
def test_empty_input_munger_with_no_input_parameters(empty):
    method = Method(
        mungers=empty,
        json_rpc_method="eth_method",
    )
    assert method.input_munger(object(), [], {}) == []


def test_default_input_munger_with_input_parameters():
    method = Method(
        json_rpc_method="eth_method",
    )
    assert method.input_munger(object(), [1], {}) == [1]


@pytest.mark.parametrize(
    "empty", ([], (), None), ids=["empty-list", "empty-tuple", "None"]
)
def test_empty_input_mungers_with_input_parameters(empty):
    method = Method(
        mungers=empty,
        json_rpc_method="eth_method",
    )
    assert method.input_munger(object(), [1], {}) == [1]


def test_default_munger_for_property_with_no_input_parameters():
    method = Method(
        is_property=True,
        json_rpc_method="eth_method",
    )
    assert method.input_munger(object(), [], {}) == ()


@pytest.mark.parametrize(
    "empty", ([], (), None), ids=["empty-list", "empty-tuple", "None"]
)
def test_empty_mungers_for_property_with_no_input_parameters(empty):
    method = Method(
        is_property=True,
        mungers=empty,
        json_rpc_method="eth_method",
    )
    assert method.input_munger(object(), [], {}) == ()


def test_default_munger_for_property_with_input_params_raises_validation_error():
    method = Method(
        is_property=True,
        json_rpc_method="eth_method",
    )
    with pytest.raises(
        Web3ValidationError, match="Parameters cannot be passed to a property"
    ):
        method.input_munger(object(), [1], {})


@pytest.mark.parametrize(
    "empty", ([], (), None), ids=["empty-list", "empty-tuple", "None"]
)
def test_empty_mungers_for_property_with_input_params_raises_validation_error(empty):
    method = Method(
        is_property=True,
        mungers=empty,
        json_rpc_method="eth_method",
    )
    with pytest.raises(
        Web3ValidationError, match="Parameters cannot be passed to a property"
    ):
        method.input_munger(object(), [1], {})


def test_property_with_mungers_raises_validation_error():
    with pytest.raises(
        Web3ValidationError, match="Mungers cannot be used with a property"
    ):
        Method(
            is_property=True,
            mungers=[lambda m, z, y: "success"],
            json_rpc_method="eth_method",
        )


@pytest.mark.parametrize(
    "method_config,args,kwargs,expected_request_result",
    (
        (
            {
                "mungers": [],
            },
            [],
            {},
            Web3ValueError,
        ),
        (
            {
                "mungers": [],
                "json_rpc_method": "eth_getBalance",
            },
            ["only_the_first_argument_but_expects_two"],
            {},
            IndexError,
        ),
        (
            {
                "mungers": [default_root_munger],
                "json_rpc_method": "eth_getBalance",
            },
            ["0x0000000000000000000000000000000000000000", 3],
            {},
            ("eth_getBalance", (("0x" + "00" * 20), "0x3")),
        ),
        (
            {
                "mungers": [default_root_munger],
                "json_rpc_method": lambda *_: "eth_getBalance",
            },
            ["0x0000000000000000000000000000000000000000", 3],
            {},
            ("eth_getBalance", (("0x" + "00" * 20), "0x3")),
        ),
        (
            {
                "mungers": [
                    lambda m, x, y, z, addr: [x, y, addr],
                    lambda m, x, y, addr: [x, addr],
                    lambda m, x, addr: [addr, str(x)],
                ],
                "json_rpc_method": "eth_getBalance",
            },
            [1, 2, 3, ("0x" + "00" * 20)],
            {},
            ("eth_getBalance", (("0x" + "00" * 20), "1")),
        ),
        (
            {
                "mungers": [
                    lambda m, x, y, z: [x, y],
                    lambda m, x, y: [x],
                    lambda m, x: [str(x)],
                ],
                "json_rpc_method": "eth_getBalance",
            },
            [1, 2, 3, 4],
            {},
            TypeError,
        ),
        (
            {
                "mungers": [default_root_munger],
                "json_rpc_method": "eth_getBalance",
            },
            ("0x0000000000000000000000000000000000000000", 3),
            {},
            ("eth_getBalance", ("0x0000000000000000000000000000000000000000", "0x3")),
        ),
        (
            {
                "json_rpc_method": "eth_getBalance",
            },
            ("0x0000000000000000000000000000000000000000", 3),
            {},
            ("eth_getBalance", ("0x0000000000000000000000000000000000000000", "0x3")),
        ),
        (
            {
                "mungers": [
                    lambda m, addr, x, y, z: [addr, x, y],
                    lambda m, addr, x, y: [addr, x],
                    lambda m, addr, x: [addr, str(x)],
                ],
                "json_rpc_method": "eth_getBalance",
            },
            [("0x" + "00" * 20), 1, 2, 3],
            {},
            ("eth_getBalance", (("0x" + "00" * 20), "1")),
        ),
        (
            {
                "mungers": None,
                "json_rpc_method": "eth_chainId",
            },
            [],
            {},
            ("eth_chainId", ()),
        ),
        (
            {
                "is_property": True,
                "json_rpc_method": "eth_chainId",
            },
            [],
            {},
            ("eth_chainId", ()),
        ),
    ),
    ids=[
        "raises-error-no-rpc-method",
        "test-missing-argument",
        "test-rpc-method-as-string",
        "test-rpc-method-as-callable",
        "test-arg-munger",
        "test-munger-too-many-args",
        "test-request-formatters-default-root-munger-explicit",
        "test-request-formatters-default-root-munger-implicit",
        "test-mungers-and-request-formatters",
        "test-response-formatters",
        "test-set-as-property-default-munger-implicit",
    ],
)
def test_process_params(
    method_config,
    args,
    kwargs,
    expected_request_result,
):
    if isclass(expected_request_result) and issubclass(
        expected_request_result, Exception
    ):
        with pytest.raises(expected_request_result):
            method = Method(**method_config)
            method.process_params(object(), *args, **kwargs)
    else:
        method = Method(**method_config)
        request_params, output_formatter = method.process_params(
            object(), *args, **kwargs
        )
        assert request_params == expected_request_result

        first_formatter = (output_formatter[0],)

        # the expected result formatters length is 1
        assert len(first_formatter) == 1


def keywords(module, keyword_one, keyword_two):
    return module, [keyword_one, keyword_two]


class Success(Exception):
    pass


def return_exception_raising_formatter(_method):
    def formatter(_params):
        raise Success()

    return compose(formatter)


class FakeModule(Module):
    method = Method(
        "eth_method",
        mungers=[keywords],
        request_formatters=return_exception_raising_formatter,
    )


@pytest.fixture
def dummy_w3():
    return Web3(EthereumTesterProvider(), modules={"fake": FakeModule})


def test_munger_class_method_access_raises_friendly_error():
    with pytest.raises(TypeError, match="Direct calls to methods are not supported"):
        FakeModule.method(1, 2)


def test_munger_arguments_by_keyword(dummy_w3):
    with pytest.raises(Success):
        dummy_w3.fake.method(keyword_one=1, keyword_two="latest")
    with pytest.raises(Success):
        dummy_w3.fake.method(1, keyword_two=2)
