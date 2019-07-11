pragma solidity ^0.4.24;
pragma experimental "v0.5.0";

import {PackageDB} from "./PackageDB.sol";
import {ReleaseDB} from "./ReleaseDB.sol";

/// @title Database contract for a package index.
/// @author Piper Merriam <pipermerriam@gmail.com>
contract ReleaseValidator {
  /// @dev Runs validation on all of the data needed for releasing a package.  Returns success.
  /// @param packageDb The address of the PackageDB
  /// @param releaseDb The address of the ReleaseDB
  /// @param callerAddress The address which is attempting to create the release.
  /// @param name The name of the package.
  /// @param version The version string of the package (ex: `1.0.0`)
  /// @param manifestURI The URI of the release manifest.
  function validateRelease(
    PackageDB packageDb,
    ReleaseDB releaseDb,
    address callerAddress,
    string name,
    string version,
    string manifestURI
  )
    public
    view
    returns (bool)
  {
    if (address(packageDb) == 0x0){
      // packageDb address is null
      revert("escape:ReleaseValidator:package-db-not-set");
    } else if (address(releaseDb) == 0x0){
      // releaseDb address is null
      revert("escape:ReleaseValidator:release-db-not-set");
    } else if (!validateAuthorization(packageDb, callerAddress, name)) {
      // package exists and msg.sender is not the owner not the package owner.
      revert("escape:ReleaseValidator:caller-not-authorized");
    } else if (!validateIsNewRelease(packageDb, releaseDb, name, version)) {
      // this version has already been released.
      revert("escape:ReleaseValidator:version-previously-published");
    } else if (!validatePackageName(packageDb, name)) {
      // invalid package name.
      revert("escape:ReleaseValidator:invalid-package-name");
    } else if (!validateStringIdentifier(manifestURI)) {
      // disallow empty release manifest URI
      revert("escape:ReleaseValidator:invalid-manifest-uri");
    } else if (!validateStringIdentifier(version)) {
      // disallow version 0.0.0
      revert("escape:ReleaseValidator:invalid-release-version");
    }
    return true;
  }

  /// @dev Validate whether the callerAddress is authorized to make this release.
  /// @param packageDb The address of the PackageDB
  /// @param callerAddress The address which is attempting to create the release.
  /// @param name The name of the package.
  function validateAuthorization(
    PackageDB packageDb,
    address callerAddress,
    string name
  )
    public
    view
    returns (bool)
  {
    bytes32 nameHash = packageDb.hashName(name);
    if (!packageDb.packageExists(nameHash)) {
      return true;
    }
    address packageOwner;

    (packageOwner,,) = packageDb.getPackageData(nameHash);

    if (packageOwner == callerAddress) {
      return true;
    }
    return false;
  }

  /// @dev Validate that the version being released has not already been released.
  /// @param packageDb The address of the PackageDB
  /// @param releaseDb The address of the ReleaseDB
  /// @param name The name of the package.
  /// @param version The version string for the release
  function validateIsNewRelease(
    PackageDB packageDb,
    ReleaseDB releaseDb,
    string name,
    string version
  )
    public
    view
    returns (bool)
  {
    bytes32 nameHash = packageDb.hashName(name);
    bytes32 versionHash = releaseDb.hashVersion(version);
    bytes32 releaseHash = releaseDb.hashRelease(nameHash, versionHash);
    return !releaseDb.releaseExists(releaseHash) && !releaseDb.releaseExisted(releaseHash);
  }

  uint constant DIGIT_0 = uint(bytes1("0"));
  uint constant DIGIT_9 = uint(bytes1("9"));
  uint constant LETTER_a = uint(bytes1("a"));
  uint constant LETTER_z = uint(bytes1("z"));
  bytes1 constant DASH = bytes1("-");

  /// @dev Returns boolean whether the provided package name is valid.
  /// @param packageDb The address of the PackageDB
  /// @param name The name of the package.
  function validatePackageName(PackageDB packageDb, string name)
    public
    view
    returns (bool)
  {
    bytes32 nameHash = packageDb.hashName(name);

    if (packageDb.packageExists(nameHash)) {
      // existing names are always valid.
      return true;
    }

    if (bytes(name).length < 2 || bytes(name).length > 255) {
      return false;
    }
    for (uint i = 0; i < bytes(name).length; i++) {
      if (bytes(name)[i] == DASH && i > 0) {
        continue;
      } else if (i > 0 && uint(bytes(name)[i]) >= DIGIT_0 && uint(bytes(name)[i]) <= DIGIT_9) {
        continue;
      } else if (uint(bytes(name)[i]) >= LETTER_a && uint(bytes(name)[i]) <= LETTER_z) {
        continue;
      } else {
        return false;
      }
    }
    return true;
  }

  /// @dev Returns boolean whether the input string has a length
  /// @param value The string to validate.
  function validateStringIdentifier(string value)
    public
    pure
    returns (bool)
  {
    if (bytes(value).length == 0) {
      return false;
    }
    return true;
  }
}
