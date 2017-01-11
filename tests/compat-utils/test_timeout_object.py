import pytest

import time

from web3.utils.compat.compat_stdlib import (
    Timeout,
)


def test_inline_completion_before_timeout():
    timeout = Timeout(0.01)
    timeout.start()
    timeout.check()
    timeout.cancel()
    time.sleep(0.02)


def test_inline_timeout():
    timeout = Timeout(0.01)
    timeout.start()
    time.sleep(0.02)
    with pytest.raises(Timeout):
        timeout.check()


def test_contextmanager_completion_before_timeout():
    with Timeout(0.01) as timeout:
        timeout.check()
    time.sleep(0.02)


def test_contextmanager_timeout():
    with pytest.raises(Timeout):
        with Timeout(0.01) as timeout:
            time.sleep(0.02)
            timeout.check()


def test_with_custom_exception_type():
    timeout = Timeout(0.01, ValueError)
    timeout.start()
    time.sleep(0.02)
    with pytest.raises(ValueError):
        timeout.check()


def test_with_custom_exception_instance():
    exc = ValueError("an instance of an excepiton")
    timeout = Timeout(0.01, exc)
    timeout.start()
    time.sleep(0.02)
    with pytest.raises(ValueError) as err:
        timeout.check()

    assert err.value is exc
