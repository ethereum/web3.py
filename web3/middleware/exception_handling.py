from web3.utils.toolz import (
    excepts,
)


def construct_exception_handler_middleware(method_handlers=None):
    if method_handlers is None:
        method_handlers = {}

    def exception_handler_middleware(make_request, web3):
        def middleware(method, params):
            if method in method_handlers:
                exc_type, handler = method_handlers[method]
                return excepts(
                    exc_type,
                    make_request,
                    handler,
                )(method, params)
            else:
                return make_request(method, params)
        return middleware
    return exception_handler_middleware
