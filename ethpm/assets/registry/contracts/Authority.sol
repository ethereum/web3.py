pragma solidity ^0.4.24;
pragma experimental "v0.5.0";


contract AuthorityInterface {
  function canCall(
    address callerAddress,
    address codeAddress,
    bytes4 sig
  )
    public
    view
    returns (bool);
}


contract AuthorizedInterface {
  address public owner;
  AuthorityInterface public authority;

  modifier auth {
    require(isAuthorized(),"escape:Authority:caller-not-authorized");
    _;
  }

  event OwnerUpdate(address indexed oldOwner, address indexed newOwner);
  event AuthorityUpdate(address indexed oldAuthority, address indexed newAuthority);

  function setOwner(address newOwner) public returns (bool);

  function setAuthority(AuthorityInterface newAuthority) public returns (bool);

  function isAuthorized() internal returns (bool);
}


contract Authorized is AuthorizedInterface {
  constructor() public {
    owner = msg.sender;
    emit OwnerUpdate(0x0, owner);
  }

  function setOwner(address newOwner)
    public
    auth
    returns (bool)
  {
    emit OwnerUpdate(owner, newOwner);
    owner = newOwner;
    return true;
  }

  function setAuthority(AuthorityInterface newAuthority)
    public
    auth
    returns (bool)
  {
    emit AuthorityUpdate(authority, newAuthority);
    authority = newAuthority;
    return true;
  }

  function isAuthorized() internal returns (bool) {
    if (msg.sender == owner) {
      return true;
    } else if (address(authority) == (0)) {
      return false;
    } else {
      return authority.canCall(msg.sender, this, msg.sig);
    }
  }
}


contract WhitelistAuthorityInterface is AuthorityInterface, AuthorizedInterface {
  event SetCanCall(
    address indexed callerAddress,
    address indexed codeAddress,
    bytes4 indexed sig,
    bool can
  );

  event SetAnyoneCanCall(
    address indexed codeAddress,
    bytes4 indexed sig,
    bool can
  );

  function setCanCall(
    address callerAddress,
    address codeAddress,
    bytes4 sig,
    bool can
  )
    public
    returns (bool);

  function setAnyoneCanCall(
    address codeAddress,
    bytes4 sig,
    bool can
  )
    public
    returns (bool);
}


contract WhitelistAuthority is WhitelistAuthorityInterface, Authorized {
  mapping (address => mapping (address => mapping (bytes4 => bool))) _canCall;
  mapping (address => mapping (bytes4 => bool)) _anyoneCanCall;

  function canCall(
    address callerAddress,
    address codeAddress,
    bytes4 sig
  )
    public
    view
    returns (bool)
  {
    if (_anyoneCanCall[codeAddress][sig]) {
      return true;
    } else {
      return _canCall[callerAddress][codeAddress][sig];
    }
  }

  function setCanCall(
    address callerAddress,
    address codeAddress,
    bytes4 sig,
    bool can
  )
    public
    auth
    returns (bool)
  {
    _canCall[callerAddress][codeAddress][sig] = can;
    emit SetCanCall(callerAddress, codeAddress, sig, can);
    return true;
  }

  function setAnyoneCanCall(
    address codeAddress,
    bytes4 sig,
    bool can
  )
    public
    auth
    returns (bool)
  {
    _anyoneCanCall[codeAddress][sig] = can;
    emit SetAnyoneCanCall(codeAddress, sig, can);
    return true;
  }
}
