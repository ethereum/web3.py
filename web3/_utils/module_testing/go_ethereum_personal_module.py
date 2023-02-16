import json
import pytest
from typing import (
    TYPE_CHECKING,
    cast,
)

from eth_typing import (
    ChecksumAddress,
)
from eth_utils import (
    is_checksum_address,
    is_list_like,
    is_same_address,
    is_string,
)
from hexbytes import (
    HexBytes,
)

from web3 import (
    constants,
)
from web3.datastructures import (
    AttributeDict,
)
from web3.types import (
    TxParams,
    Wei,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )

PRIVATE_KEY_HEX = "0x56ebb41875ceedd42e395f730e03b5c44989393c9f0484ee6bc05f933673458f"
SECOND_PRIVATE_KEY_HEX = (
    "0x56ebb41875ceedd42e395f730e03b5c44989393c9f0484ee6bc05f9336712345"
)
THIRD_PRIVATE_KEY_HEX = (
    "0x56ebb41875ceedd42e395f730e03b5c44989393c9f0484ee6bc05f9336754321"
)
PASSWORD = "web3-testing"
ADDRESS = "0x844B417c0C58B02c2224306047B9fb0D3264fE8c"
SECOND_ADDRESS = "0xB96b6B21053e67BA59907E252D990C71742c41B8"


PRIVATE_KEY_FOR_UNLOCK = (
    "0x392f63a79b1ff8774845f3fa69de4a13800a59e7083f5187f1558f0797ad0f01"
)
ACCOUNT_FOR_UNLOCK = "0x12efDc31B1a8FA1A1e756DFD8A1601055C971E13"


class GoEthereumPersonalModuleTest:
    def test_personal_import_raw_key(self, w3: "Web3") -> None:
        actual = w3.geth.personal.import_raw_key(PRIVATE_KEY_HEX, PASSWORD)
        assert actual == ADDRESS

    def test_personal_list_accounts(self, w3: "Web3") -> None:
        accounts = w3.geth.personal.list_accounts()
        assert is_list_like(accounts)
        assert len(accounts) > 0
        assert all((is_checksum_address(item) for item in accounts))

    def test_personal_list_wallets(self, w3: "Web3") -> None:
        wallets = w3.geth.personal.list_wallets()
        assert is_list_like(wallets)
        assert len(wallets) > 0
        assert is_checksum_address(wallets[0]["accounts"][0]["address"])
        assert is_string(wallets[0]["accounts"][0]["url"])
        assert is_string(wallets[0]["status"])
        assert is_string(wallets[0]["url"])

    def test_personal_lock_account(
        self, w3: "Web3", unlockable_account_dual_type: ChecksumAddress
    ) -> None:
        # TODO: how do we test this better?
        w3.geth.personal.lock_account(unlockable_account_dual_type)

    def test_personal_unlock_account_success(
        self,
        w3: "Web3",
        unlockable_account_dual_type: ChecksumAddress,
        unlockable_account_pw: str,
    ) -> None:
        result = w3.geth.personal.unlock_account(
            unlockable_account_dual_type, unlockable_account_pw
        )
        assert result is True

    def test_personal_unlock_account_failure(
        self, w3: "Web3", unlockable_account_dual_type: ChecksumAddress
    ) -> None:
        with pytest.raises(ValueError):
            w3.geth.personal.unlock_account(
                unlockable_account_dual_type, "bad-password"
            )

    def test_personal_new_account(self, w3: "Web3") -> None:
        new_account = w3.geth.personal.new_account(PASSWORD)
        assert is_checksum_address(new_account)

    def test_personal_send_transaction(
        self,
        w3: "Web3",
        unlockable_account_dual_type: ChecksumAddress,
        unlockable_account_pw: str,
    ) -> None:
        assert (
            w3.eth.get_balance(unlockable_account_dual_type) > constants.WEI_PER_ETHER
        )
        txn_params: TxParams = {
            "from": unlockable_account_dual_type,
            "to": unlockable_account_dual_type,
            "gas": 21000,
            "value": Wei(1),
            "gasPrice": w3.to_wei(1, "gwei"),
        }
        txn_hash = w3.geth.personal.send_transaction(txn_params, unlockable_account_pw)
        assert txn_hash
        transaction = w3.eth.get_transaction(txn_hash)

        assert is_same_address(
            transaction["from"], cast(ChecksumAddress, txn_params["from"])
        )
        assert is_same_address(
            transaction["to"], cast(ChecksumAddress, txn_params["to"])
        )
        assert transaction["gas"] == txn_params["gas"]
        assert transaction["value"] == txn_params["value"]
        assert transaction["gasPrice"] == txn_params["gasPrice"]

    def test_personal_sign_and_ecrecover(
        self,
        w3: "Web3",
        unlockable_account_dual_type: ChecksumAddress,
        unlockable_account_pw: str,
    ) -> None:
        message = "test-web3-geth-personal-sign"
        signature = w3.geth.personal.sign(
            message, unlockable_account_dual_type, unlockable_account_pw
        )
        signer = w3.geth.personal.ec_recover(message, signature)
        assert is_same_address(signer, unlockable_account_dual_type)

    @pytest.mark.xfail(
        reason="personal_sign_typed_data JSON RPC call has not been released in geth"
    )
    def test_personal_sign_typed_data(
        self,
        w3: "Web3",
        unlockable_account_dual_type: ChecksumAddress,
        unlockable_account_pw: str,
    ) -> None:
        typed_message = """
            {
                "types": {
                    "EIP712Domain": [
                        {"name": "name", "type": "string"},
                        {"name": "version", "type": "string"},
                        {"name": "chainId", "type": "uint256"},
                        {"name": "verifyingContract", "type": "address"}
                    ],
                    "Person": [
                        {"name": "name", "type": "string"},
                        {"name": "wallet", "type": "address"}
                    ],
                    "Mail": [
                        {"name": "from", "type": "Person"},
                        {"name": "to", "type": "Person"},
                        {"name": "contents", "type": "string"}
                    ]
                },
                "primaryType": "Mail",
                "domain": {
                    "name": "Ether Mail",
                    "version": "1",
                    "chainId": "0x01",
                    "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"
                },
                "message": {
                    "from": {
                        "name": "Cow",
                        "wallet": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"
                    },
                    "to": {
                        "name": "Bob",
                        "wallet": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"
                    },
                    "contents": "Hello, Bob!"
                }
            }
        """
        signature = HexBytes(
            w3.geth.personal.sign_typed_data(
                json.loads(typed_message),
                unlockable_account_dual_type,
                unlockable_account_pw,
            )
        )

        expected_signature = HexBytes(
            "0xc8b56aaeefd10ab4005c2455daf28d9082af661ac347cd"
            "b612d5b5e11f339f2055be831bf57a6e6cb5f6d93448fa35"
            "c1bd56fe1d745ffa101e74697108668c401c"
        )
        assert signature == expected_signature
        assert len(signature) == 32 + 32 + 1


class GoEthereumAsyncPersonalModuleTest:
    @pytest.mark.asyncio
    async def test_async_sign_and_ec_recover(
        self,
        async_w3: "AsyncWeb3",
        unlockable_account_dual_type: ChecksumAddress,
        unlockable_account_pw: str,
    ) -> None:
        message = "This is a test"
        signature = await async_w3.geth.personal.sign(
            message, unlockable_account_dual_type, unlockable_account_pw
        )
        address = await async_w3.geth.personal.ec_recover(message, signature)
        assert is_same_address(unlockable_account_dual_type, address)

    @pytest.mark.asyncio
    async def test_async_import_key(self, async_w3: "AsyncWeb3") -> None:
        address = await async_w3.geth.personal.import_raw_key(
            THIRD_PRIVATE_KEY_HEX, "Testing"
        )
        assert address is not None

    @pytest.mark.asyncio
    async def test_async_list_accounts(self, async_w3: "AsyncWeb3") -> None:
        accounts = await async_w3.geth.personal.list_accounts()
        assert len(accounts) > 0

    @pytest.mark.asyncio
    async def test_async_list_wallets(self, async_w3: "AsyncWeb3") -> None:
        wallets = await async_w3.geth.personal.list_wallets()
        assert isinstance(wallets[0], AttributeDict)

    @pytest.mark.asyncio
    async def test_async_new_account(self, async_w3: "AsyncWeb3") -> None:
        passphrase = "Create New Account"
        account = await async_w3.geth.personal.new_account(passphrase)
        assert is_checksum_address(account)

    @pytest.mark.asyncio
    async def test_async_unlock_lock_account(
        self,
        async_w3: "AsyncWeb3",
        unlockable_account_dual_type: ChecksumAddress,
        unlockable_account_pw: str,
    ) -> None:
        unlocked = await async_w3.geth.personal.unlock_account(
            unlockable_account_dual_type, unlockable_account_pw
        )
        assert unlocked is True
        locked = await async_w3.geth.personal.lock_account(unlockable_account_dual_type)
        assert locked is True

    @pytest.mark.asyncio
    async def test_async_send_transaction(
        self,
        async_w3: "AsyncWeb3",
        unlockable_account_dual_type: ChecksumAddress,
        unlockable_account_pw: str,
    ) -> None:
        tx_params = TxParams()
        tx_params["to"] = unlockable_account_dual_type
        tx_params["from"] = unlockable_account_dual_type
        tx_params["value"] = Wei(123)
        response = await async_w3.geth.personal.send_transaction(
            tx_params, unlockable_account_pw
        )
        assert response is not None

    @pytest.mark.xfail(
        reason="personal_signTypedData JSON RPC call has not been released in geth"
    )
    @pytest.mark.asyncio
    async def test_async_sign_typed_data(
        self,
        async_w3: "AsyncWeb3",
        unlockable_account_dual_type: ChecksumAddress,
        unlockable_account_pw: str,
    ) -> None:
        message = {"message": "This is a test"}
        signature = await async_w3.geth.personal.sign_typed_data(
            message, unlockable_account_dual_type, unlockable_account_pw
        )
        address = await async_w3.geth.personal.ec_recover(
            json.dumps(message), signature
        )
        assert is_same_address(unlockable_account_dual_type, address)
