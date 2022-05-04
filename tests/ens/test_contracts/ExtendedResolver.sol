/**
 * The SimpleExtendedResolver is really only meant to test the validation of the parent ens domain
 * `extended-resolver.eth` and, separately, the subdomains of this parent domain. We then "resolve"
 * to arbitrary addresses 0x000000000000000000000000000000000000dEaD for subdomain validations and
 * 0x000000000000000000000000000000000000bEEF for the parent domain validation so that we can be
 * sure each case was validated via the appropriate logic via the `resolve()` function of the contract.
 */


pragma solidity >=0.4.24;

interface ENS {

    // Logged when the owner of a node assigns a new owner to a subnode.
    event NewOwner(bytes32 node, bytes32 label, address owner);

    // Logged when the owner of a node transfers ownership to a new account.
    event Transfer(bytes32 node, address owner);

    // Logged when the resolver for a node changes.
    event NewResolver(bytes32  node, address resolver);

    // Logged when the TTL of a node changes
    event NewTTL(bytes32  node, uint64 ttl);


    function setSubnodeOwner(bytes32 node, bytes32 label, address owner) external;
    function setResolver(bytes32 node, address resolver) external;
    function setOwner(bytes32 node, address owner) external;
    function setTTL(bytes32 node, uint64 ttl) external;
    function owner(bytes32 node) external view returns (address);
    function resolver(bytes32 node) external view returns (address);
    function ttl(bytes32 node) external view returns (uint64);
}

pragma solidity >= 0.7.0;

abstract contract ResolverBase {
    bytes4 private constant INTERFACE_META_ID = 0x01ffc9a7;

    function supportsInterface(bytes4 interfaceID) virtual public pure returns(bool) {
        return interfaceID == INTERFACE_META_ID;
    }

    function isAuthorised(bytes32 node) internal virtual view returns(bool);

    modifier authorised(bytes32 node) {
        require(isAuthorised(node));
        _;
    }

    function bytesToAddress(bytes memory b) internal pure returns(address payable a) {
        require(b.length == 20);
        assembly {
            a := div(mload(add(b, 32)), exp(256, 12))
        }
    }

    function addressToBytes(address a) internal pure returns(bytes memory b) {
        b = new bytes(20);
        assembly {
            mstore(add(b, 32), mul(a, exp(256, 12)))
        }
    }
}

contract ExtendedResolver is ResolverBase  {
    ENS ens;

    bytes4 constant private EXTENDED_RESOLVER_INTERFACE_ID = 0x9061b923;
    string constant extendedResolverParentDomain = "\x11extended-resolver\x03eth\x00";
    bytes32 constant extendedResolverNamehash = 0xf0a378cc2afe91730d0105e67d6bb037cc5b8b6bfec5b5962d9b637ff6497e55;

    /**
     * A mapping of authorisations. An address that is authorised for a name
     * may make any changes to the name that the owner could, but may not update
     * the set of authorisations.
     * (node, owner, caller) => isAuthorised
     */
    mapping(bytes32=>mapping(address=>mapping(address=>bool))) public authorisations;

    event AuthorisationChanged(bytes32  node, address  owner, address  target, bool isAuthorised);

    constructor(ENS _ens) public {
        ens = _ens;
    }

    /**
     * @dev Sets or clears an authorisation.
     * Authorisations are specific to the caller. Any account can set an authorisation
     * for any name, but the authorisation that is checked will be that of the
     * current owner of a name. Thus, transferring a name effectively clears any
     * existing authorisations, and new authorisations can be set in advance of
     * an ownership transfer if desired.
     *
     * @param node The name to change the authorisation on.
     * @param target The address that is to be authorised or deauthorised.
     * @param isAuthorised True if the address should be authorised, or false if it should be deauthorised.
     */
    function setAuthorisation(bytes32 node, address target, bool isAuthorised) external {
        authorisations[node][msg.sender][target] = isAuthorised;
        emit AuthorisationChanged(node, msg.sender, target, isAuthorised);
    }

    function isAuthorised(bytes32 node) override internal view returns(bool) {
        address owner = ens.owner(node);
        return owner == msg.sender || authorisations[node][owner][msg.sender];
    }

    function supportsInterface(bytes4 interfaceID) override public pure returns(bool) {
        return interfaceID == EXTENDED_RESOLVER_INTERFACE_ID || super.supportsInterface(interfaceID);
    }

    // Simple resolve method solely used to test ENSIP-10 / Wildcard Resolution functionality
    function resolve(bytes calldata dnsName, bytes calldata data) external view returns (bytes memory) {
        // validate 'extended-resolver.eth' parent domain
        if (keccak256(dnsName) == keccak256(bytes(extendedResolverParentDomain)) && data.length >= 36) {
            require(bytes32(data[4:36]) == extendedResolverNamehash, "parent domain not validated appropriately");
            return abi.encode(address(0x000000000000000000000000000000000000bEEF));
        } else {
            uint length = uint8(dnsName[0]);
            // validate subdomains of 'extended-resolver.eth' parent domain
            require(keccak256(dnsName[1 + length:]) == keccak256(bytes(extendedResolverParentDomain)), "subdomain not validated appropriately");
            return abi.encode(address(0x000000000000000000000000000000000000dEaD));
        }
    }
}
