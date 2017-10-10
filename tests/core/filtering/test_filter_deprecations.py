import pytest


@pytest.mark.parametrize(
    'filter_type',
    (
        ('latest'),
        ('pending'),
        ({}),
    )
)
def test_async_filter_deprecations(web3, filter_type, skip_if_testrpc):
    if filter_type in ['latest', 'pending']:
        skip_if_testrpc(web3)

    filter = web3.eth.filter(filter_type)
    with pytest.warns(DeprecationWarning):
        filter.watch()

    with pytest.warns(DeprecationWarning):
        filter.stop_watching()


def test_get_log_filter_deprecation(web3):
    log_filter = web3.eth.filter({})
    with pytest.warns(DeprecationWarning):
        log_filter.get()
