from eth_utils import (
    is_address,
    is_list_like,
    is_same_address,
)


PRIVATE_KEY_HEX = '0x56ebb41875ceedd42e395f730e03b5c44989393c9f0484ee6bc05f933673458f'
PASSWORD = 'web3-testing'
ADDRESS = '0x844b417c0c58b02c2224306047b9fb0d3264fe8c'


PRIVATE_KEY_FOR_UNLOCK = '0x392f63a79b1ff8774845f3fa69de4a13800a59e7083f5187f1558f0797ad0f01'
ACCOUNT_FOR_UNLOCK = '0x12efdc31b1a8fa1a1e756dfd8a1601055c971e13'


class PersonalModuleTest(object):
    def test_personal_importRawKey(self, web3):
        actual = web3.personal.importRawKey(PRIVATE_KEY_HEX, PASSWORD)
        assert is_same_address(actual, ADDRESS)

    def test_personal_listAccounts(self, web3):
        accounts = web3.personal.listAccounts
        assert is_list_like(accounts)
        assert len(accounts) > 0
        assert all((
            is_address(item)
            for item
            in accounts
        ))

    def test_personal_lockAccount(self, web3, unlocked_account):
        # TODO: how do we test this better?
        web3.personal.lockAccount(unlocked_account)

    def test_personal_unlockAccount(self, web3):
        account = web3.personal.importRawKey(PRIVATE_KEY_FOR_UNLOCK, PASSWORD)
        assert is_same_address(account)
        # TODO: how do we test this better?
        web3.personal.unlockAccount(account, PASSWORD)

    def test_personal_newAccount(self, web3):
        new_account = web3.personal.newAccount(PASSWORD)
        assert is_address(new_account)

    def test_personal_sendAndSignTransaction(seelf, web3):
        # TODO: how to do this without overhead?
        pass
