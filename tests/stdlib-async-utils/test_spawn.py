from web3.utils.async.stdlib_async import spawn


def test_spawning_simple_thread():
    container = {
        'success': None,
    }

    def target_fn():
        container['success'] = True

    thread = spawn(target_fn)
    thread.join()

    assert container['success'] is True
