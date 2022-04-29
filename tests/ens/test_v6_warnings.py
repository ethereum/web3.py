import pytest


def test_resolve_deprecation_warning(ens):
    with pytest.warns(
        DeprecationWarning,
        match="In v6, the resolve\\(\\) method will be made internal and renamed to "
              "_resolve\\(\\). The 'get' param name will also change to 'fn_name'.",
    ):
        ens.resolve('tester.eth')


def test_resolver_future_warning(ens):
    with pytest.warns(
        FutureWarning,
        match="The function signature for resolver\\(\\) will change in v6 to accept 'name' as a "
              "param, over 'normalized_name', and the method will normalize the name internally.",
    ):
        ens.resolver('tester.eth')
