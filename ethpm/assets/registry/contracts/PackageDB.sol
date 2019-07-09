pragma solidity ^0.4.24;
pragma experimental "v0.5.0";

import {IndexedOrderedSetLib} from "./IndexedOrderedSetLib.sol";
import {Authorized} from "./Authority.sol";


/// @title Database contract for a package index package data.
/// @author Tim Coulter <tim.coulter@consensys.net>, Piper Merriam <pipermerriam@gmail.com>
contract PackageDB is Authorized {
  using IndexedOrderedSetLib for IndexedOrderedSetLib.IndexedOrderedSet;

  struct Package {
    bool exists;
    uint createdAt;
    uint updatedAt;
    string name;
    address owner;
  }

  // Package Data: (nameHash => value)
  mapping (bytes32 => Package) _recordedPackages;
  IndexedOrderedSetLib.IndexedOrderedSet _allPackageNameHashes;

  // Events
  event PackageReleaseAdd(bytes32 indexed nameHash, bytes32 indexed releaseHash);
  event PackageReleaseRemove(bytes32 indexed nameHash, bytes32 indexed releaseHash);
  event PackageCreate(bytes32 indexed nameHash);
  event PackageDelete(bytes32 indexed nameHash, string reason);
  event PackageOwnerUpdate(bytes32 indexed nameHash, address indexed oldOwner, address indexed newOwner);

  /*
   *  Modifiers
   */
  modifier onlyIfPackageExists(bytes32 nameHash) {
    require(packageExists(nameHash), "escape:PackageDB:package-not-found");
    _;
  }

  //
  //  +-------------+
  //  |  Write API  |
  //  +-------------+
  //

  /// @dev Creates or updates a release for a package.  Returns success.
  /// @param name Package name
  function setPackage(string name)
    public
    auth
    returns (bool)
  {
    // Hash the name and the version for storing data
    bytes32 nameHash = hashName(name);

    Package storage package = _recordedPackages[nameHash];

    // Mark the package as existing if it isn't already tracked.
    if (!packageExists(nameHash)) {

      // Set package data
      package.exists = true;
      package.createdAt = block.timestamp; // solium-disable-line security/no-block-members
      package.name = name;

      // Add the nameHash to the list of all package nameHashes.
      _allPackageNameHashes.add(nameHash);

      emit PackageCreate(nameHash);
    }

    package.updatedAt = block.timestamp; // solium-disable-line security/no-block-members

    return true;
  }

  /// @dev Removes a package from the package db.  Packages with existing releases may not be removed.  Returns success.
  /// @param nameHash The name hash of a package.
  function removePackage(bytes32 nameHash, string reason)
    public
    auth
    onlyIfPackageExists(nameHash)
    returns (bool)
  {
    emit PackageDelete(nameHash, reason);

    delete _recordedPackages[nameHash];
    _allPackageNameHashes.remove(nameHash);

    return true;
  }

  /// @dev Sets the owner of a package to the provided address.  Returns success.
  /// @param nameHash The name hash of a package.
  /// @param newPackageOwner The address of the new owner.
  function setPackageOwner(bytes32 nameHash, address newPackageOwner)
    public
    auth
    onlyIfPackageExists(nameHash)
    returns (bool)
  {
    emit PackageOwnerUpdate(nameHash, _recordedPackages[nameHash].owner, newPackageOwner);

    _recordedPackages[nameHash].owner = newPackageOwner;
    _recordedPackages[nameHash].updatedAt = block.timestamp; // solium-disable-line security/no-block-members

    return true;
  }

  //
  //  +------------+
  //  |  Read API  |
  //  +------------+
  //

  /// @dev Query the existence of a package with the given name.  Returns boolean indicating whether the package exists.
  /// @param nameHash The name hash of a package.
  function packageExists(bytes32 nameHash)
    public
    view
    returns (bool)
  {
    return _recordedPackages[nameHash].exists;
  }

  /// @dev Return the total number of packages
  function getNumPackages()
    public
    view
    returns (uint)
  {
    return _allPackageNameHashes.size();
  }

  /// @dev Returns package namehash at the provided index from the set of all known name hashes.
  /// @param idx The index of the package name hash to retrieve.
  function getPackageNameHash(uint idx)
    public
    view
    returns (bytes32)
  {
    return _allPackageNameHashes.get(idx);
  }

  /// @dev Returns information about the package.
  /// @param nameHash The name hash to look up.
  function getPackageData(bytes32 nameHash)
    public
    view
    onlyIfPackageExists(nameHash)
    returns (
      address packageOwner,
      uint createdAt,
      uint updatedAt
    )
  {
    Package storage package = _recordedPackages[nameHash];
    return (package.owner, package.createdAt, package.updatedAt);
  }

  /// @dev Returns the package name for the given namehash
  /// @param nameHash The name hash to look up.
  function getPackageName(bytes32 nameHash)
    public
    view
    onlyIfPackageExists(nameHash)
    returns (string)
  {
    return _recordedPackages[nameHash].name;
  }

  /// @dev Returns a slice of the array of all package hashes for the named package.
  /// @param offset The starting index for the slice.
  /// @param limit  The length of the slice
  function getAllPackageIds(uint _offset, uint limit)
    public
    view
    returns (
      bytes32[] packageIds,
      uint offset
    )
  {
    bytes32[] memory hashes;                 // Array of package ids to return
    uint cursor = _offset;                   // Index counter to traverse DB array
    uint remaining;                          // Counter to collect `limit` packages
    uint totalPackages = getNumPackages();   // Total number of packages in registry

    // Is request within range?
    if (cursor < totalPackages){

      // Get total remaining records
      remaining = totalPackages - cursor;

      // Number of records to collect is lesser of `remaining` and `limit`
      if (remaining > limit ){
        remaining = limit;
      }

      // Allocate return array
      hashes = new bytes32[](remaining);

      // Collect records. (IndexedOrderedSet manages deletions.)
      while(remaining > 0){
        bytes32 hash = getPackageNameHash(cursor);
        hashes[remaining - 1] = hash;
        remaining--;
        cursor++;
      }
    }
    return (hashes, cursor);
  }

  /*
   *  Hash Functions
   */
  /// @dev Returns name hash for a given package name.
  /// @param name Package name
  function hashName(string name)
    public
    pure
    returns (bytes32)
  {
    return keccak256(abi.encodePacked(name));
  }
}
