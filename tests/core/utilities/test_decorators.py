import time

from web3.utils.decorators import (
    reject_recursive_repeats,
)
from web3.utils.threads import (
    spawn,
)


def test_reject_recursive_repeats_multithreaded():
    @reject_recursive_repeats
    def recurse(sleep_now):
        time.sleep(sleep_now)
        try:
            recurse(0.05)
            return True
        except ValueError:
            return False
    thd1 = spawn(recurse, 0)
    thd2 = spawn(recurse, 0.02)
    assert thd2.get() and thd1.get()
