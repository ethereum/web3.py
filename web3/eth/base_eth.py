from typing import (
    Any,
    List,
    NoReturn,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    overload,
)

from eth_account import (
    Account,
)
from eth_typing import (
    Address,
    ChecksumAddress,
    HexStr,
)
from eth_utils import (
    is_checksum_address,
    is_string,
)
from eth_utils.toolz import (
    assoc,
)

from web3._utils.empty import (
    Empty,
    empty,
)
from web3.contract import (
    AsyncContract,
    AsyncContractCaller,
    Contract,
    ContractCaller,
)
from web3.module import (
    Module,
)
from web3.types import (
    ENS,
    BlockIdentifier,
    CallOverride,
    FilterParams,
    GasPriceStrategy,
    TxParams,
    Wei,
)


class BaseEth(Module):
    _default_account: Union[ChecksumAddress, Empty] = empty
    _default_block: BlockIdentifier = "latest"
    _default_contract_factory: Any = None
    _gas_price_strategy = None

    is_async = False
    account = Account()

    def namereg(self) -> NoReturn:
        raise NotImplementedError()

    def icap_namereg(self) -> NoReturn:
        raise NotImplementedError()

    @property
    def default_block(self) -> BlockIdentifier:
        return self._default_block

    @default_block.setter
    def default_block(self, value: BlockIdentifier) -> None:
        self._default_block = value

    @property
    def default_account(self) -> Union[ChecksumAddress, Empty]:
        return self._default_account

    @default_account.setter
    def default_account(self, account: Union[ChecksumAddress, Empty]) -> None:
        self._default_account = account

    def send_transaction_munger(self, transaction: TxParams) -> Tuple[TxParams]:
        if "from" not in transaction and is_checksum_address(self.default_account):
            transaction = assoc(transaction, "from", self.default_account)

        return (transaction,)

    def generate_gas_price(
        self, transaction_params: Optional[TxParams] = None
    ) -> Optional[Wei]:
        if self._gas_price_strategy:
            return self._gas_price_strategy(self.w3, transaction_params)
        return None

    def set_gas_price_strategy(
        self, gas_price_strategy: Optional[GasPriceStrategy]
    ) -> None:
        self._gas_price_strategy = gas_price_strategy

    def estimate_gas_munger(
        self, transaction: TxParams, block_identifier: Optional[BlockIdentifier] = None
    ) -> Sequence[Union[TxParams, BlockIdentifier]]:
        if "from" not in transaction and is_checksum_address(self.default_account):
            transaction = assoc(transaction, "from", self.default_account)

        if block_identifier is None:
            params: Sequence[Union[TxParams, BlockIdentifier]] = [transaction]
        else:
            params = [transaction, block_identifier]

        return params

    def get_block_munger(
        self, block_identifier: BlockIdentifier, full_transactions: bool = False
    ) -> Tuple[BlockIdentifier, bool]:
        return (block_identifier, full_transactions)

    def block_id_munger(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> Tuple[Union[Address, ChecksumAddress, ENS], BlockIdentifier]:
        if block_identifier is None:
            block_identifier = self.default_block
        return (account, block_identifier)

    def get_storage_at_munger(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        position: int,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> Tuple[Union[Address, ChecksumAddress, ENS], int, BlockIdentifier]:
        if block_identifier is None:
            block_identifier = self.default_block
        return (account, position, block_identifier)

    def call_munger(
        self,
        transaction: TxParams,
        block_identifier: Optional[BlockIdentifier] = None,
        state_override: Optional[CallOverride] = None,
    ) -> Union[
        Tuple[TxParams, BlockIdentifier], Tuple[TxParams, BlockIdentifier, CallOverride]
    ]:
        # TODO: move to middleware
        if "from" not in transaction and is_checksum_address(self.default_account):
            transaction = assoc(transaction, "from", self.default_account)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.default_block

        if state_override is None:
            return (transaction, block_identifier)
        else:
            return (transaction, block_identifier, state_override)

    def filter_munger(
        self,
        filter_params: Optional[Union[str, FilterParams]] = None,
        filter_id: Optional[HexStr] = None,
    ) -> Union[List[FilterParams], List[HexStr], List[str]]:
        if filter_id and filter_params:
            raise TypeError(
                "Ambiguous invocation: provide either a `filter_params` or a "
                "`filter_id` argument. Both were supplied."
            )
        if isinstance(filter_params, dict):
            return [filter_params]
        elif is_string(filter_params):
            if filter_params in {"latest", "pending"}:
                return [filter_params]
            else:
                raise ValueError(
                    "The filter API only accepts the values of `pending` or "
                    "`latest` for string based filters"
                )
        elif filter_id and not filter_params:
            return [filter_id]
        else:
            raise TypeError(
                "Must provide either filter_params as a string or "
                "a valid filter object, or a filter_id as a string "
                "or hex."
            )

    @overload
    def contract(
        self, address: None = None, **kwargs: Any
    ) -> Union[Type[Contract], Type[AsyncContract]]:
        ...  # noqa: E704,E501

    @overload  # noqa: F811
    def contract(
        self, address: Union[Address, ChecksumAddress, ENS], **kwargs: Any
    ) -> Union[Contract, AsyncContract]:
        ...  # noqa: E704,E501

    def contract(  # noqa: F811
        self,
        address: Optional[Union[Address, ChecksumAddress, ENS]] = None,
        **kwargs: Any,
    ) -> Union[Type[Contract], Contract, Type[AsyncContract], AsyncContract]:
        ContractFactoryClass = kwargs.pop(
            "ContractFactoryClass", self._default_contract_factory
        )

        ContractFactory = ContractFactoryClass.factory(self.w3, **kwargs)

        if address:
            return ContractFactory(address)
        else:
            return ContractFactory

    def set_contract_factory(
        self,
        contract_factory: Type[
            Union[Contract, AsyncContract, ContractCaller, AsyncContractCaller]
        ],
    ) -> None:
        self._default_contract_factory = contract_factory
