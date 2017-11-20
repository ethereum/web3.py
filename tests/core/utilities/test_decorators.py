from web3.utils.compat import (
    sleep,
    spawn,
)
from web3.utils.decorators import (
    reject_recursive_repeats,
)


def test_reject_recursive_repeats_multithreaded():
    @reject_recursive_repeats
    def recurse(sleep_now):
        sleep(sleep_now)
        try:
            recurse(0.05)
            return True
        except ValueError:
            return False
    thd1 = spawn(recurse, 0)
    thd2 = spawn(recurse, 0.02)
    assert thd2.get() and thd1.get()
