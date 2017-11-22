def test_admin_addPeer(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    result = web3.admin.addPeer(
        'enode://44826a5d6a55f88a18298bca4773fca5749cdc3a5c9f308aa7d810e9b31123f3e7c5fba0b1d70aac5308426f47df2a128a6747040a3815cc7dd7167d03be320d@127.0.0.1:30304',  # noqa: E501
    )
    assert result is True
