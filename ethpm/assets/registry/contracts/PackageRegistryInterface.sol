pragma solidity ^0.4.24;
pragma experimental "v0.5.0";


/// @title EIP 1319 Smart Contract Package Registry Interface
/// @author Piper Merriam <pipermerriam@gmail.com>, Christopher Gewecke <christophergewecke@gmail.com>
contract PackageRegistryInterface {

  //
  // +-------------+
  // |  Write API  |
  // +-------------+
  //

  /// @dev Creates a a new release for the named package.
  /// @notice Will create a new release the given package with the given release information.
  /// @param packageName Package name
  /// @param version Version string (ex: 1.0.0)
  /// @param manifestURI The URI for the release manifest for this release.
  function release(
    string packageName,
    string version,
    string manifestURI
  )
    public
    returns (bytes32 releaseId);

  //
  // +------------+
  // |  Read API  |
  // +------------+
  //

  /// @dev Returns the string name of the package associated with a package id
  /// @param packageId The package id to look up
  function getPackageName(bytes32 packageId)
    public
    view
    returns (string packageName);

  /// @dev Returns a slice of the array of all package ids for the named package.
  /// @param offset The starting index for the slice.
  /// @param limit  The length of the slice
  function getAllPackageIds(uint offset, uint limit)
    public
    view
    returns (
      bytes32[] packageIds,
      uint pointer
    );

  /// @dev Returns a slice of the array of all release hashes for the named package.
  /// @param packageName Package name
  /// @param offset The starting index for the slice.
  /// @param limit  The length of the slice
  function getAllReleaseIds(string packageName, uint offset, uint limit)
    public
    view
    returns (
      bytes32[] releaseIds,
      uint pointer
    );

  /// @dev Returns the package data for a release.
  /// @param releaseId Release id
  function getReleaseData(bytes32 releaseId)
    public
    view
    returns (
      string packageName,
      string version,
      string manifestURI
    );

  // @dev Returns release id that *would* be generated for a name and version pair on `release`.
  // @param packageName Package name
  // @param version Version string (ex: '1.0.0')
  function generateReleaseId(string packageName, string version)
    public
    view
    returns (bytes32 releaseId);

  /// @dev Returns the release id for a given name and version pair if present on registry.
  /// @param packageName Package name
  /// @param version Version string(ex: '1.0.0')
  function getReleaseId(string packageName, string version)
    public
    view
    returns (bytes32 releaseId);

  /// @dev Returns the number of packages stored on the registry
  function numPackageIds() public view returns (uint totalCount);

  /// @dev Returns the number of releases for a given package name on the registry
  /// @param packageName Package name
  function numReleaseIds(string packageName) public view returns (uint totalCount);
}
