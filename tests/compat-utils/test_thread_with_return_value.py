from web3.utils.compat.compat_stdlib import (
    spawn,
)


def test_thread_with_return_value():
    container = {
        'success': None,
    }

    def target_fn():
        container['success'] = True
        return 12345

    thread = spawn(target_fn)
    thread.join()

    assert container['success'] is True

    assert thread.get() == 12345
