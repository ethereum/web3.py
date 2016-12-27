import sys

# raise MyException() from original_exception compatibility
if sys.version_info.major == 3:

    def raise_from(my_exception, other_exception):
        raise my_exception from other_exception
else:

    def raise_from(my_exception, other_exception):
        # This syntax is not accepted under Python 3
        # raise my_exception, None, sys.exc_info()[2]

        # For now, just swallow the original exception under Python 2.
        # For better error messages please upgrade to Python 3.
        raise my_exception