from inspect import (
    isclass,
)
import pytest

from web3 import (
    EthereumTesterProvider,
    Web3,
)
from web3.method import (
    Method,
    _apply_request_formatters,
)
from web3.module import (
    ModuleV2,
    apply_response_formatters,
)


def test_method_accepts_callable_for_selector():
    method = Method(
        mungers=[],
        json_rpc_method=lambda *_: 'eth_method',
        formatter_lookup_fn=''
    )
    assert method.method_selector_fn() == 'eth_method'


def test_method_selector_fn_accepts_str():
    method = Method(
        mungers=[],
        json_rpc_method='eth_method',
        formatter_lookup_fn=''
    )
    assert method.method_selector_fn() == 'eth_method'


def test_method_selector_fn_invalid_arg():
    with pytest.raises(ValueError):
        method = Method(
            mungers=[],
            json_rpc_method=555555,
            formatter_lookup_fn=''
        )
        method.method_selector_fn()


def test_get_formatters_default_formatter_for_falsy_config():
    method = Method(
        mungers=[],
        json_rpc_method='eth_method',
        formatter_lookup_fn=''
    )

    default_request_formatters, default_response_formatters = method.get_formatters('')

    assert _apply_request_formatters(['a', 'b', 'c'], default_request_formatters) == ['a', 'b', 'c']
    assert apply_response_formatters(
        default_response_formatters, {'result': ['a', 'b', 'c']}) == {'result': ['a', 'b', 'c']}


def test_get_formatters_non_falsy_config_retrieval():
    def formatter_lookup_fn(method):
        if method == 'eth_method':
            return 'match'
        return 'nonmatch'
    method = Method(
        mungers=[],
        json_rpc_method='eth_method',
        formatter_lookup_fn=formatter_lookup_fn,
    )
    assert method.get_formatters('eth_method') == 'match'
    assert method.get_formatters('eth_nonmatching') == 'nonmatch'


def test_input_munger_parameter_passthrough_matching_arity():
    method = Method(
        mungers=[lambda m, z, y: ['success']],
        json_rpc_method='eth_method',
        formatter_lookup_fn=''
    )
    method.input_munger(object(), ['first', 'second'], {}) == 'success'


def test_input_munger_parameter_passthrough_mismatch_arity():
    method = Method(
        mungers=[lambda m, z, y: 'success'],
        json_rpc_method='eth_method',
        formatter_lookup_fn=''
    )
    with pytest.raises(TypeError):
        method.input_munger(object(), ['first', 'second', 'third'], {})


def test_input_munger_falsy_config_result_in_default_munger():
    method = Method(
        mungers=[],
        json_rpc_method='eth_method',
        formatter_lookup_fn=''
    )
    method.input_munger(object(), [], {}) == []


def test_default_input_munger_with_input_parameters_exception():
    method = Method(
        mungers=[],
        json_rpc_method='eth_method',
        formatter_lookup_fn=''
    )
    with pytest.raises(TypeError):
        method.input_munger(object(), [1], {})


def get_test_formatters(method):
    def formatter(params):
        return ['ok']

    if method == 'eth_method':
        return ((formatter,), (None, None))
    return (None, (None, None))


@pytest.mark.parametrize(
    "method_config,args,kwargs,expected_result",
    (
        (
            {
                'mungers': [],
                'formatter_lookup_fn': ''
            },
            [],
            {},
            ValueError
        ),
        (
            {
                'mungers': [],
                'json_rpc_method': 'eth_method',
                'formatter_lookup_fn': ''
            },
            ['unexpected_argument'],
            {},
            TypeError
        ),
        (
            {
                'mungers': [],
                'json_rpc_method': 'eth_method',
                'formatter_lookup_fn': ''
            },
            [],
            {},
            ('eth_method', ())
        ),
        (
            {
                'mungers': [],
                'json_rpc_method': lambda *_: 'eth_method',
                'formatter_lookup_fn': ''
            },
            [],
            {},
            ('eth_method', ())
        ),
        (
            {
                'mungers': [
                    lambda m, x, y, z: [x, y],
                    lambda m, x, y: [x],
                    lambda m, x: [str(x)]],
                'json_rpc_method': 'eth_method',
                'formatter_lookup_fn': ''
            },
            [1, 2, 3],
            {},
            ('eth_method', ["1"])
        ),
        (
            {
                'mungers': [
                    lambda m, x, y, z: [x, y],
                    lambda m, x, y: [x],
                    lambda m, x: [str(x)]],
                'json_rpc_method': 'eth_method',
                'formatter_lookup_fn': ''
            },
            [1, 2, 3, 4],
            {},
            TypeError,
        ),
        (
            {
                'mungers': [],
                'json_rpc_method': 'eth_method',
                'formatter_lookup_fn': get_test_formatters
            },
            [],
            {},
            ('eth_method', ['ok'])
        ),
        (
            {
                'mungers': [],
                'json_rpc_method': 'eth_mismatch',
                'formatter_lookup_fn': get_test_formatters
            },
            [],
            {},
            ('eth_mismatch', ())
        ),
        (
            {
                'mungers': [
                    lambda m, x, y, z: [x, y],
                    lambda m, x, y: [x],
                    lambda m, x: [str(x)]],
                'json_rpc_method': 'eth_method',
                'formatter_lookup_fn': get_test_formatters
            },
            [1, 2, 3],
            {},
            ('eth_method', ['ok'])
        ),
    )
)
def test_process_params(
        method_config,
        args,
        kwargs,
        expected_result,):

    if isclass(expected_result) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            method = Method(**method_config)
            req_params, output_formatter = method.process_params(object(), *args, **kwargs)
    else:
        method = Method(**method_config)
        req_params, output_formatter = method.process_params(object(), *args, **kwargs)
        assert req_params == expected_result


def keywords(module, keyword_one, keyword_two):
    return module, [keyword_one, keyword_two]


class Success(Exception):
    pass


def return_exception_raising_formatter(method):
    def formatter(params):
        raise Success()
    return ([formatter], [])


class FakeModule(ModuleV2):
    method = Method(
        'eth_method',
        mungers=[keywords],
        formatter_lookup_fn=return_exception_raising_formatter)


@pytest.fixture
def dummy_w3():
    return Web3(
        EthereumTesterProvider(),
        modules={'fake': (FakeModule,)},
        middlewares=[])


def test_munger_class_method_access_raises_friendly_error():
    with pytest.raises(TypeError):
        FakeModule.method(1, 2)


def test_munger_arguments_by_keyword(dummy_w3):
    with pytest.raises(Success):
        dummy_w3.fake.method(keyword_one=1, keyword_two=2)
    with pytest.raises(Success):
        dummy_w3.fake.method(1, keyword_two=2)
