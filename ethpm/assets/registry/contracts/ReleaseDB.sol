pragma solidity ^0.4.24;
pragma experimental "v0.5.0";


import {IndexedOrderedSetLib} from "./IndexedOrderedSetLib.sol";
import {Authorized} from "./Authority.sol";


/// @title Database contract for a package index.
/// @author Tim Coulter <tim.coulter@consensys.net>, Piper Merriam <pipermerriam@gmail.com>
contract ReleaseDB is Authorized {
  using IndexedOrderedSetLib for IndexedOrderedSetLib.IndexedOrderedSet;

  struct Release {
    bool exists;
    uint createdAt;
    uint updatedAt;
    bytes32 nameHash;
    bytes32 versionHash;
    string manifestURI;
  }

  // Release Data: (releaseId => value)
  mapping (bytes32 => Release) _recordedReleases;
  mapping (bytes32 => bool) _removedReleases;
  IndexedOrderedSetLib.IndexedOrderedSet _allReleaseIds;
  mapping (bytes32 => IndexedOrderedSetLib.IndexedOrderedSet) _releaseIdsByNameHash;

  // Version Data: (versionHash => value)
  mapping (bytes32 => string) _recordedVersions;
  mapping (bytes32 => bool) _versionExists;

  // Events
  event ReleaseCreate(bytes32 indexed releaseId);
  event ReleaseUpdate(bytes32 indexed releaseId);
  event ReleaseDelete(bytes32 indexed releaseId, string reason);

  /*
   *  Modifiers
   */
  modifier onlyIfVersionExists(bytes32 versionHash) {
    require(versionExists(versionHash), "escape:ReleaseDB:version-not-found");
    _;
  }

  modifier onlyIfReleaseExists(bytes32 releaseId) {
    require(releaseExists(releaseId), "escape:ReleaseDB:release-not-found");
    _;
  }

  //
  // +-------------+
  // |  Write API  |
  // +-------------+
  //

  /// @dev Creates or updates a release for a package.  Returns success.
  /// @param nameHash The name hash of the package.
  /// @param versionHash The version hash for the release version.
  /// @param manifestURI The URI for the release manifest for this release.
  function setRelease(
    bytes32 nameHash,
    bytes32 versionHash,
    string manifestURI
  )
    public
    auth
    returns (bool)
  {
    bytes32 releaseId = hashRelease(nameHash, versionHash);

    Release storage release = _recordedReleases[releaseId];

    // If this is a new version push it onto the array of version hashes for
    // this package.
    if (release.exists) {
      emit ReleaseUpdate(releaseId);
    } else {
      // Populate the basic release data.
      release.exists = true;
      release.createdAt = block.timestamp; // solium-disable-line security/no-block-members
      release.nameHash = nameHash;
      release.versionHash = versionHash;

      // Push the release hash into the array of all release hashes.
      _allReleaseIds.add(releaseId);
      _releaseIdsByNameHash[nameHash].add(releaseId);

      emit ReleaseCreate(releaseId);
    }

    // Record the last time the release was updated.
    release.updatedAt = block.timestamp; // solium-disable-line security/no-block-members

    // Save the release manifest URI
    release.manifestURI = manifestURI;

    return true;
  }

  /// @dev Removes a release from a package.  Returns success.
  /// @param releaseId The release hash to be removed
  /// @param reason Explanation for why the removal happened.
  function removeRelease(bytes32 releaseId, string reason)
    public
    auth
    onlyIfReleaseExists(releaseId)
    returns (bool)
  {
    bytes32 nameHash;
    bytes32 versionHash;

    (nameHash, versionHash,,) = getReleaseData(releaseId);

    // Zero out the release data.
    delete _recordedReleases[releaseId];
    delete _recordedVersions[versionHash];

    // Remove the release hash from the list of all release hashes
    _allReleaseIds.remove(releaseId);
    _releaseIdsByNameHash[nameHash].remove(releaseId);

    // Add the release hash to the map of removed releases
    _removedReleases[releaseId] = true;

    // Log the removal.
    emit ReleaseDelete(releaseId, reason);

    return true;
  }


  /// @dev Adds the given version to the local version database.  Returns the versionHash for the provided version.
  /// @param version Version string (ex: '1.0.0')
  function setVersion(string version)
    public
    auth
    returns (bytes32)
  {
    bytes32 versionHash = hashVersion(version);

    if (!_versionExists[versionHash]) {
      _recordedVersions[versionHash] = version;
      _versionExists[versionHash] = true;
    }
    return versionHash;
  }

  //
  // +------------+
  // |  Read API  |
  // +------------+
  //

  /// @dev Returns a slice of the array of all releases hashes for the named package.
  /// @param offset The starting index for the slice.
  /// @param limit  The length of the slice
  function getAllReleaseIds(bytes32 nameHash, uint _offset, uint limit)
    public
    view
    returns (
      bytes32[] releaseIds,
      uint offset
    )
  {
    bytes32[] memory hashes;                                  // Release ids to return
    uint cursor = _offset;                                    // Index counter to traverse DB array
    uint remaining;                                           // Counter to collect `limit` packages
    uint totalReleases = getNumReleasesForNameHash(nameHash); // Total number of packages in registry

    // Is request within range?
    if (cursor < totalReleases){

      // Get total remaining records
      remaining = totalReleases - cursor;

      // Number of records to collect is lesser of `remaining` and `limit`
      if (remaining > limit ){
        remaining = limit;
      }

      // Allocate return array
      hashes = new bytes32[](remaining);

      // Collect records. (IndexedOrderedSet manages deletions.)
      while(remaining > 0){
        bytes32 hash = getReleaseIdForNameHash(nameHash, cursor);
        hashes[remaining - 1] = hash;
        remaining--;
        cursor++;
      }
    }
    return (hashes, cursor);
  }

  /// @dev Get the total number of releases
  /// @param nameHash the name hash to lookup.
  function getNumReleasesForNameHash(bytes32 nameHash)
    public
    view
    returns (uint)
  {
    return _releaseIdsByNameHash[nameHash].size();
  }

  /// @dev Release hash for a Package at a given index
  /// @param nameHash the name hash to lookup.
  /// @param idx The index of the release hash to retrieve.
  function getReleaseIdForNameHash(bytes32 nameHash, uint idx)
    public
    view
    returns (bytes32)
  {
    return _releaseIdsByNameHash[nameHash].get(idx);
  }

  /// @dev Query the existence of a release at the provided version for a package.  Returns boolean indicating whether such a release exists.
  /// @param releaseId The release hash to query.
  function releaseExists(bytes32 releaseId)
    public
    view
    returns (bool)
  {
    return _recordedReleases[releaseId].exists;
  }

  /// @dev Query the past existence of a release at the provided version for a package.  Returns boolean indicating whether such a release ever existed.
  /// @param releaseHash The release hash to query.
  function releaseExisted(bytes32 releaseHash)
    public
    view
    returns (bool)
  {
    return _removedReleases[releaseHash];
  }

  /// @dev Query the existence of the provided version in the recorded versions.  Returns boolean indicating whether such a version exists.
  /// @param versionHash the version hash to check.
  function versionExists(bytes32 versionHash)
    public
    view
    returns (bool)
  {
    return _versionExists[versionHash];
  }

  /// @dev Returns the releaseData for the given release has a package.
  /// @param releaseId The release hash.
  function getReleaseData(bytes32 releaseId)
    public
    view
    onlyIfReleaseExists(releaseId)
    returns (
      bytes32 nameHash,
      bytes32 versionHash,
      uint createdAt,
      uint updatedAt
    )
  {
    Release storage release = _recordedReleases[releaseId];
    return (release.nameHash, release.versionHash, release.createdAt, release.updatedAt);
  }

  /// @dev Returns string version identifier from the version of the given release hash.
  /// @param versionHash the version hash
  function getVersion(bytes32 versionHash)
    public
    view
    onlyIfVersionExists(versionHash)
    returns (string)
  {
    return _recordedVersions[versionHash];
  }

  /// @dev Returns the URI of the release manifest for the given release hash.
  /// @param releaseId Release hash
  function getManifestURI(bytes32 releaseId)
    public
    view
    onlyIfReleaseExists(releaseId)
    returns (string)
  {
    return _recordedReleases[releaseId].manifestURI;
  }

  /*
   *  Hash Functions
   */
  /// @dev Returns version hash for the given semver version.
  /// @param version Version string
  function hashVersion(string version)
    public
    pure
    returns (bytes32)
  {
    return keccak256(abi.encodePacked(version));
  }

  /// @dev Returns release hash for the given release
  /// @param nameHash The name hash of the package name.
  /// @param versionHash The version hash for the release version.
  function hashRelease(bytes32 nameHash, bytes32 versionHash)
    public
    pure
    returns (bytes32)
  {
    return keccak256(abi.encodePacked(nameHash, versionHash));
  }
}
