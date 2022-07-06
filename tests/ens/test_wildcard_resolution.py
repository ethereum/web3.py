import pytest


@pytest.mark.parametrize("subdomain", ("sub1", "sub2", "rändöm", "🌈rainbow", "faß"))
def test_wildcard_resolution_with_extended_resolver_for_subdomains(ens, subdomain):
    # validate subdomains of `extended-resolver.eth` by asserting it returns the
    # specified hard-coded address from `tests/test_contracts/ExtendedResolver.sol`
    # which requires certain conditions to be met that are specific to subdomains only
    resolved_child_address = ens.address(f"{subdomain}.extended-resolver.eth")
    assert resolved_child_address == "0x000000000000000000000000000000000000dEaD"


def test_wildcard_resolution_with_extended_resolver_for_parent_ens_domain(ens):
    # validate `extended-resolver.eth` by asserting it returns the specified
    # hard-coded address from `tests/test_contracts/ExtendedResolver.sol`
    # which requires a specific condition to be met for the parent domain
    # `extended-resolver.eth`
    resolved_parent_address = ens.address("extended-resolver.eth")
    assert resolved_parent_address == "0x000000000000000000000000000000000000bEEF"


# -- async -- #


@pytest.mark.asyncio
@pytest.mark.parametrize("subdomain", ("sub1", "sub2", "rändöm", "🌈rainbow", "faß"))
async def test_async_wildcard_resolution_with_extended_resolver_for_subdomains(
    async_ens, subdomain
):
    # validate subdomains of `extended-resolver.eth` by asserting it returns the
    # specified hard-coded address from `tests/test_contracts/ExtendedResolver.sol`
    # which requires certain conditions to be met that are specific to subdomains only
    resolved_child_address = await async_ens.address(
        f"{subdomain}.extended-resolver.eth"
    )
    assert resolved_child_address == "0x000000000000000000000000000000000000dEaD"


@pytest.mark.asyncio
async def test_async_wildcard_resolution_with_extended_resolver_for_parent_ens_domain(
    async_ens,
):
    # validate `extended-resolver.eth` by asserting it returns the specified
    # hard-coded address from `tests/test_contracts/ExtendedResolver.sol`
    # which requires a specific condition to be met for the parent domain
    # `extended-resolver.eth`
    resolved_parent_address = await async_ens.address("extended-resolver.eth")
    assert resolved_parent_address == "0x000000000000000000000000000000000000bEEF"
