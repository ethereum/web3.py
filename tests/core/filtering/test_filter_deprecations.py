import sys
import pytest


@pytest.mark.parametrize(
    'filter_type',
    (
        ('latest'),
        ('pending'),
        ({}),
    )
)
@pytest.mark.skipif(sys.version_info.major == 2, reason="Python2 fails weirdly on this test")
def test_async_filter_deprecations(web3, filter_type, skip_if_testrpc):
    if filter_type in ['latest', 'pending']:
        skip_if_testrpc(web3)

    filter = web3.eth.filter(filter_type)
    with pytest.warns(DeprecationWarning) as wr:
        wr.clear()
        filter.watch()

    with pytest.warns(DeprecationWarning):
        filter.stop_watching()


@pytest.mark.skipif(sys.version_info.major == 2, reason="Python2 fails weirdly on this test")
def test_get_log_filter_deprecation(web3):
    log_filter = web3.eth.filter({})
    with pytest.warns(DeprecationWarning):
        log_filter.get()
