import sys


def raise_from(my_exception, other_exception):
    raise my_exception, None, sys.exc_info()[2]  # noqa: W602, E999
