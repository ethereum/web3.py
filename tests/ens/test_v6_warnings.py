import pytest
import warnings


def test_resolve_deprecation_warning(ens):
    with pytest.warns(
        DeprecationWarning,
        match="In v6, the `ENS.resolve\\(\\)` method will be made internal and renamed to "
            "`_resolve\\(\\)`. It is recommended to use the abstracted resolve functionality of "
            "`ENS.address\\(\\)` for forward resolution, and `ENS.name\\(\\)` for reverse "
            "resolution instead."
    ):
        ens.resolve('tester.eth')


def test_resolver_future_warning(ens):
    with pytest.warns(
        FutureWarning,
        match="The function signature for resolver\\(\\) will change in v6 to accept `name` as a "
            "the positional argument, over `normal_name`, and the method will instead "
            "normalize the name internally. To suppress warnings for now, `name` may be passed "
            "in as a keyword argument.",
    ):
        ens.resolver('tester.eth')

    # assert no warning when `name` kwarg is passed in
    with warnings.catch_warnings():
        warnings.simplefilter("error")  # turn all warnings to errors
        ens.resolver('tester.eth', name='tester.eth')
