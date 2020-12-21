from typing import (  # noqa: F401
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
    Tuple,
    Type,
)

from eth_utils import (
    combomethod,
    is_canonical_address,
    to_bytes,
    to_canonical_address,
)
from eth_utils.toolz import (
    assoc,
    curry,
    pipe,
)

from ethpm.exceptions import (
    BytecodeLinkingError,
    EthPMValidationError,
)
from ethpm.validation.misc import (
    validate_empty_bytes,
)
from web3._utils.validation import (
    validate_address,
)
from web3.contract import (
    Contract,
    ContractConstructor,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class LinkableContract(Contract):
    """
    A subclass of web3.contract.Contract that is capable of handling
    contract factories with link references in their package's manifest.
    """

    unlinked_references: Optional[Tuple[Dict[str, Any]]] = None
    linked_references: Optional[Tuple[Dict[str, Any]]] = None
    needs_bytecode_linking = None

    def __init__(self, address: bytes, **kwargs: Any) -> None:
        if self.needs_bytecode_linking:
            raise BytecodeLinkingError(
                "Contract cannot be instantiated until its bytecode is linked."
            )
        validate_address(address)
        # type ignored to allow for undefined **kwargs on `Contract` base class __init__
        super(LinkableContract, self).__init__(address=address, **kwargs)  # type: ignore

    @classmethod
    def factory(
        cls, web3: "Web3", class_name: str = None, **kwargs: Any
    ) -> Contract:
        dep_link_refs = kwargs.get("unlinked_references")
        bytecode = kwargs.get("bytecode")
        needs_bytecode_linking = False
        if dep_link_refs and bytecode:
            if not is_prelinked_bytecode(to_bytes(hexstr=bytecode), dep_link_refs):
                needs_bytecode_linking = True
        kwargs = assoc(kwargs, "needs_bytecode_linking", needs_bytecode_linking)
        return super(LinkableContract, cls).factory(web3, class_name, **kwargs)

    @classmethod
    def constructor(cls, *args: Any, **kwargs: Any) -> ContractConstructor:
        if cls.needs_bytecode_linking:
            raise BytecodeLinkingError(
                "Contract cannot be deployed until its bytecode is linked."
            )
        return super(LinkableContract, cls).constructor(*args, **kwargs)

    @classmethod
    def link_bytecode(cls, attr_dict: Dict[str, str]) -> Type["LinkableContract"]:
        """
        Return a cloned contract factory with the deployment / runtime bytecode linked.

        :attr_dict: Dict[`ContractType`: `Address`] for all deployment and runtime link references.
        """
        if not cls.unlinked_references and not cls.linked_references:
            raise BytecodeLinkingError("Contract factory has no linkable bytecode.")
        if not cls.needs_bytecode_linking:
            raise BytecodeLinkingError(
                "Bytecode for this contract factory does not require bytecode linking."
            )
        cls.validate_attr_dict(attr_dict)
        bytecode = apply_all_link_refs(cls.bytecode, cls.unlinked_references, attr_dict)
        runtime = apply_all_link_refs(
            cls.bytecode_runtime, cls.linked_references, attr_dict
        )
        linked_class = cls.factory(
            cls.web3, bytecode_runtime=runtime, bytecode=bytecode
        )
        if linked_class.needs_bytecode_linking:
            raise BytecodeLinkingError(
                "Expected class to be fully linked, but class still needs bytecode linking."
            )
        return linked_class

    @combomethod
    def validate_attr_dict(self, attr_dict: Dict[str, str]) -> None:
        """
        Validates that ContractType keys in attr_dict reference existing manifest ContractTypes.
        """
        attr_dict_names = list(attr_dict.keys())

        if not self.unlinked_references and not self.linked_references:
            raise BytecodeLinkingError(
                "Unable to validate attr dict, this contract has no linked/unlinked references."
            )

        unlinked_refs = self.unlinked_references or ({},)
        linked_refs = self.linked_references or ({},)
        all_link_refs = unlinked_refs + linked_refs

        all_link_names = [ref["name"] for ref in all_link_refs if ref]
        if set(attr_dict_names) != set(all_link_names):
            raise BytecodeLinkingError(
                "All link references must be defined when calling "
                "`link_bytecode` on a contract factory."
            )
        for address in attr_dict.values():
            validate_address(address)


def is_prelinked_bytecode(bytecode: bytes, link_refs: List[Dict[str, Any]]) -> bool:
    """
    Returns False if all expected link_refs are unlinked, otherwise returns True.
    todo support partially pre-linked bytecode (currently all or nothing)
    """
    for link_ref in link_refs:
        for offset in link_ref["offsets"]:
            try:
                validate_empty_bytes(offset, link_ref["length"], bytecode)
            except EthPMValidationError:
                return True
    return False


def apply_all_link_refs(
    bytecode: bytes, link_refs: List[Dict[str, Any]], attr_dict: Dict[str, str]
) -> bytes:
    """
    Applies all link references corresponding to a valid attr_dict to the bytecode.
    """
    if link_refs is None:
        return bytecode
    link_fns = (
        apply_link_ref(offset, ref["length"], attr_dict[ref["name"]])
        for ref in link_refs
        for offset in ref["offsets"]
    )
    linked_bytecode = pipe(bytecode, *link_fns)
    return linked_bytecode


@curry
def apply_link_ref(offset: int, length: int, value: bytes, bytecode: bytes) -> bytes:
    """
    Returns the new bytecode with `value` put into the location indicated by `offset` and `length`.
    """
    try:
        validate_empty_bytes(offset, length, bytecode)
    except EthPMValidationError:
        raise BytecodeLinkingError("Link references cannot be applied to bytecode")

    address = value if is_canonical_address(value) else to_canonical_address(value)
    new_bytes = (
        # Ignore linting error b/c conflict b/w black & flake8
        bytecode[:offset] + address + bytecode[offset + length:]  # noqa: E201, E203
    )
    return new_bytes
