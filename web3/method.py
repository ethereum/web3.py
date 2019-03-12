import functools

from eth_utils import (
    to_tuple,
)
from eth_utils.toolz import (
    identity,
    pipe,
)


def _munger_star_apply(fn):
    @functools.wraps(fn)
    def inner(args):
        return fn(*args)
    return inner


def get_default_formatters(*args, **kwargs):
    return ([identity], [identity],)


def default_munger(module, *args, **kwargs):
    if not args and not kwargs:
        return tuple()
    else:
        raise TypeError("Parameters passed to method without parameter mungers defined.")


def default_root_munger(module, *args):
    return [*args]


class Method:
    """Method object for web3 module methods

    Calls to the Method go through these steps:

    1. input munging - includes normalization, parameter checking, early parameter
    formatting.  Any processing on the input parameters that need to happen before
    json_rpc method string selection occurs.

            A note about mungers: The first (root) munger should reflect the desired
        api function arguments. In other words, if the api function wants to
        behave as: `getBalance(account, block_identifier=None)`, the root munger
        should accept these same arguments, with the addition of the module as
        the first argument e.g.:

        ```
        def getBalance_root_munger(module, account, block_identifier=None):
            if block_identifier is None:
                block_identifier = DEFAULT_BLOCK
            return module, [account, block_identifier]
        ```

        all mungers should return an argument list.

        if no munger is provided, a default munger expecting no method arguments
        will be used.

    2. method selection - The json_rpc_method argument can be method string or a
    function that returns a method string. If a callable is provided the processed
    method inputs are passed to the method selection function, and the returned
    method string is used.

    3. request and response formatters are retrieved - formatters are retrieved
    using the json rpc method string. The lookup function provided by the
    formatter_lookup_fn configuration is passed the method string and is
    expected to return a 2-tuple of lists containing the
    request_formatters and response_formatters in that order.
    e.g. ([*request_formatters], [*response_formatters]).

    4. After the parameter processing from steps 1-3 the request is made using
    the calling function returned by the module attribute ``retrieve_caller_fn``
    and the reponse formatters are applied to the output.
    """
    def __init__(
            self,
            json_rpc_method=None,
            mungers=None,
            formatter_lookup_fn=None,
            web3=None):

        self.json_rpc_method = json_rpc_method
        self.mungers = mungers or [default_munger]
        self.formatter_lookup_fn = formatter_lookup_fn or get_default_formatters

    def __get__(self, obj=None, obj_type=None):
        if obj is None:
            raise TypeError(
                "Direct calls to methods are not supported. "
                "Methods must be called from an module instance, "
                "usually attached to a web3 instance.")
        return obj.retrieve_caller_fn(self)

    @property
    def method_selector_fn(self):
        """Gets the method selector from the config.
        """
        if callable(self.json_rpc_method):
            return self.json_rpc_method
        elif isinstance(self.json_rpc_method, (str,)):
            return lambda *_: self.json_rpc_method
        raise ValueError("``json_rpc_method`` config invalid.  May be a string or function")

    def get_formatters(self, method_string):
        """Lookup the request formatters for the rpc_method

        The lookup_fn output is expected to be a 2 length tuple of lists of
        the request and output formatters, respectively.
        """
        formatters = self.formatter_lookup_fn(method_string)
        return formatters or get_default_formatters()

    def input_munger(self, val):
        try:
            module, args, kwargs = val
        except TypeError:
            raise ValueError("input_munger expects a 3-tuple")

        # TODO: Create friendly error output.
        mungers_iter = iter(self.mungers)
        root_munger = next(mungers_iter)
        munged_inputs = pipe(
            root_munger(module, *args, **kwargs),
            *map(lambda m: _munger_star_apply(functools.partial(m, module)), mungers_iter))

        return munged_inputs

    def process_params(self, module, *args, **kwargs):
        # takes in input params, steps 1-3
        params, method, (req_formatters, ret_formatters) = _pipe_and_accumulate(
            (module, args, kwargs,),
            [self.input_munger, self.method_selector_fn, self.get_formatters])

        return (method, pipe(params, *req_formatters)), ret_formatters


@to_tuple
def _pipe_and_accumulate(val, fns):
    """pipes val through a list of fns while accumulating results from
    each function, returning a tuple.

    e.g.:

        >>> _pipe_and_accumulate([lambda x: x**2, lambda x: x*10], 5)
        (25, 250)

    """
    for fn in fns:
        val = fn(val)
        yield val
