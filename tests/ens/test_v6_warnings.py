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
        ens.resolve("tester.eth")


def test_resolver_future_warning_when_name_is_missing(ens):
    with pytest.warns(
        FutureWarning,
        match="The function signature for resolver\\(\\) will change in v6 to accept `name` as a "
            "the positional argument, over `normal_name`, and the method will instead "
            "normalize the name internally. You may migrate to using `name` by passing it in "
            "as a keyword, e.g. resolver\\(name=\"ensname.eth\"\\).",
    ):
        assert ens.resolver("eth")

    # assert no warning when `name` is passed in as a kwarg
    with warnings.catch_warnings():
        warnings.simplefilter("error")  # turn all warnings to errors
        assert ens.resolver(name="EtH")

    # assert TypeError if both arguments passed in
    with pytest.raises(
        TypeError,
        match="Only supply one positional argument or the `name` keyword, e.g. resolver\\("
        "\"ensname.eth\"\\) or resolver\\(name=\"ensname.eth\"\\).",
    ):
        ens.resolver("eth", name="EtH")
