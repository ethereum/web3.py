from web3.utils.compat.compat_stdlib import (
    spawn,
    ThreadWithReturn,
)


class CustomThreadClass(ThreadWithReturn):
    pass


def test_spawning_simple_thread():
    container = {
        'success': None,
    }

    def target_fn():
        container['success'] = True

    thread = spawn(target_fn)
    thread.join()

    assert container['success'] is True


def test_spawning_specific_thread_class():
    container = {
        'success': None,
    }

    def target_fn():
        container['success'] = True

    thread = spawn(target_fn, thread_class=CustomThreadClass)
    thread.join()

    assert isinstance(thread, CustomThreadClass)

    assert container['success'] is True
