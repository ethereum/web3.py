import pytest


@pytest.mark.parametrize(
    'filter_type',
    (
        ('latest'),
        ('pending'),
        ({}),
    )
)
def test_filter_deprecations(web3, filter_type, skip_if_testrpc):
    if filter_type in ['latest', 'pending']:
        skip_if_testrpc(web3)

    filt = web3.eth.filter(filter_type)
    with pytest.warns(DeprecationWarning):
        filt.watch()

    with pytest.warns(DeprecationWarning):
        filt.stop_watching()
