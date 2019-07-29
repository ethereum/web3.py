pragma solidity >=0.5.10;

import {PackageRegistryInterface} from "./PackageRegistryInterface.sol";
import {Ownable} from "./Ownable.sol";

/// @title Contract for an ERC1319 Registry, adapted from ethpm/escape-truffle
/// @author Nick Gheorghita <nickg@ethereum.org>
contract PackageRegistry is PackageRegistryInterface, Ownable {
    struct Package {
        bool exists;
        uint createdAt;
        uint updatedAt;
        uint releaseCount;
        string name;
    }

    struct Release {
        bool exists;
        uint createdAt;
        bytes32 packageId;
        string version;
        string manifestURI;
    }

    mapping (bytes32 => Package) public packages;
    mapping (bytes32 => Release) public releases;

    // package_id#release_count => release_id
    mapping (bytes32 => bytes32) packageReleaseIndex;
    // Total package number (int128) => package_id (bytes32)
    mapping (uint => bytes32) allPackageIds;
    // Total release number (int128) => release_id (bytes32)
    mapping (uint => bytes32) allReleaseIds;
    // Total number of packages in registry
    uint public packageCount;
    // Total number of releases in registry
    uint public releaseCount;

    // Events
    event VersionRelease(string packageName, string version, string manifestURI);
    event PackageTransfer(address indexed oldOwner, address indexed newOwner);

    // Modifiers
    modifier onlyIfPackageExists(string memory packageName) {
        require(packageExists(packageName), "package-does-not-exist");
        _;
    }

    modifier onlyIfReleaseExists(string memory packageName, string memory version) {
        require (releaseExists(packageName, version), "release-does-not-exist");
        _;
    }

    //
    // ===============
    // |  Write API  |
    // ===============
    //

    /// @dev Creates a new release for the named package.  If this is the first release for the given
    /// package then this will also create and store the package.  Returns releaseID if successful.
    /// @notice Will create a new release the given package with the given release information.
    /// @param packageName Package name
    /// @param version Version string (ex: '1.0.0')
    /// @param manifestURI The URI for the release manifest for this release.
    function release(
        string memory packageName,
        string memory version,
        string memory manifestURI
    )
        public
        onlyOwner
        returns (bytes32)
    {
        validatePackageName(packageName);
        validateStringIdentifier(version);
        validateStringIdentifier(manifestURI);

        // Compute hashes
        bytes32 packageId = generatePackageId(packageName);
        bytes32 releaseId = generateReleaseId(packageName, version);
        Package storage package = packages[packageId];

        // If the package does not yet exist create it
        if (package.exists == false) {
            package.exists = true;
            package.createdAt = block.timestamp;
            package.updatedAt = block.timestamp;
            package.name = packageName;
            package.releaseCount = 0;
            allPackageIds[packageCount] = packageId;
            packageCount++;
        } else {
            package.updatedAt = block.timestamp;
        }
        cutRelease(packageId, releaseId, packageName, version, manifestURI);
        return releaseId;
    }

    function cutRelease(
        bytes32 packageId,
        bytes32 releaseId,
        string memory packageName,
        string memory version,
        string memory manifestURI
    )
        private
    {
        Release storage newRelease = releases[releaseId];
        require(newRelease.exists == false, "release-already-exists");

        // Store new release data
        newRelease.exists = true;
        newRelease.createdAt = block.timestamp;
        newRelease.packageId = packageId;
        newRelease.version = version;
        newRelease.manifestURI = manifestURI;

        releases[releaseId] = newRelease;
        allReleaseIds[releaseCount] = releaseId;
        releaseCount++;

        // Update package's release count
        Package storage package = packages[packageId];
        bytes32 packageReleaseId = generatePackageReleaseId(packageId, package.releaseCount);
        packageReleaseIndex[packageReleaseId] = releaseId;
        package.releaseCount++;

        // Log the release.
        emit VersionRelease(packageName, version, manifestURI);
    }

    //
    // ==============
    // |  Read API  |
    // ==============
    //

    /// @dev Returns the string name of the package associated with a package id
    /// @param packageId The package id to look up
    function getPackageName(bytes32 packageId)
        public
        view
        returns (string memory packageName)
    {
        Package memory targetPackage = packages[packageId];
        require (targetPackage.exists == true, "package-does-not-exist");
        return targetPackage.name;
    }

    /// @dev Returns a slice of the array of all package ids for the named package.
    /// @param offset The starting index for the slice.
    /// @param limit  The length of the slice
    function getAllPackageIds(uint offset, uint limit)
        public
        view
        returns (
            bytes32[] memory packageIds,
            uint pointer
        )
    {
        bytes32[] memory hashes;                 // Array of package ids to return
        uint cursor = offset;                    // Index counter to traverse DB array
        uint remaining;                          // Counter to collect `limit` packages

        // Is request within range?
        if (cursor < packageCount){

            // Get total remaining records
            remaining = packageCount - cursor;

            // Number of records to collect is lesser of `remaining` and `limit`
            if (remaining > limit ){
                remaining = limit;
            }

            // Allocate return array
            hashes = new bytes32[](remaining);

            // Collect records.
            while(remaining > 0){
                bytes32 hash = allPackageIds[cursor];
                hashes[remaining - 1] = hash;
                remaining--;
                cursor++;
            }
        }
        return (hashes, cursor);
    }

    /// @dev Returns a slice of the array of all release hashes for the named package.
    /// @param packageName Package name
    /// @param offset The starting index for the slice.
    /// @param limit  The length of the slice
    function getAllReleaseIds(string memory packageName, uint offset, uint limit)
        public
        view
        onlyIfPackageExists(packageName)
        returns (
            bytes32[] memory releaseIds,
            uint pointer
        )
    {
        bytes32 packageId = generatePackageId(packageName);
        Package storage package = packages[packageId];
        bytes32[] memory hashes;                                    // Release ids to return
        uint cursor = offset;                                       // Index counter to traverse DB array
        uint remaining;                                             // Counter to collect `limit` packages
        uint numPackageReleases = package.releaseCount;		        // Total number of packages in registry

        // Is request within range?
        if (cursor < numPackageReleases){

            // Get total remaining records
            remaining = numPackageReleases - cursor;

            // Number of records to collect is lesser of `remaining` and `limit`
            if (remaining > limit ){
                remaining = limit;
            }

            // Allocate return array
            hashes = new bytes32[](remaining);

            // Collect records.
            while(remaining > 0){
                bytes32 packageReleaseId = generatePackageReleaseId(packageId, cursor);
                bytes32 hash = packageReleaseIndex[packageReleaseId];
                hashes[remaining - 1] = hash;
                remaining--;
                cursor++;
            }
        }
        return (hashes, cursor);
    }


    /// @dev Returns the package data for a release.
    /// @param releaseId Release id
    function getReleaseData(bytes32 releaseId)
        public
        view
        returns (
            string memory packageName, string memory version,
            string memory manifestURI
        )
    {
        Release memory targetRelease = releases[releaseId];
        Package memory targetPackage = packages[targetRelease.packageId];
        return (targetPackage.name, targetRelease.version, targetRelease.manifestURI);
    }

    /// @dev Returns the release id for a given name and version pair if present on registry.
    /// @param packageName Package name
    /// @param version Version string(ex: '1.0.0')
    function getReleaseId(string memory packageName, string memory version)
        public
        view
        onlyIfPackageExists(packageName)
        onlyIfReleaseExists(packageName, version)
        returns (bytes32 releaseId)
    {
        return generateReleaseId(packageName, version);
    }

    /// @dev Returns the number of packages stored on the registry
    function numPackageIds() public view returns (uint totalCount)
    {
        return packageCount;
    }

    /// @dev Returns the number of releases for a given package name on the registry
    /// @param packageName Package name
    function numReleaseIds(string memory packageName)
        public
        view
        onlyIfPackageExists(packageName)
        returns (uint totalCount)
    {
        bytes32 packageId = generatePackageId(packageName);
        Package storage package = packages[packageId];
        return package.releaseCount;
    }

    /// @dev Returns a bool indicating whether the given release exists in this registry.
    /// @param packageName Package Name
    /// @param version version
    function releaseExists(string memory packageName, string memory version)
        public
        view
        onlyIfPackageExists(packageName)
        returns (bool)
    {
        bytes32 releaseId = generateReleaseId(packageName, version);
        Release storage targetRelease = releases[releaseId];
        return targetRelease.exists;
    }

    /// @dev Returns a bool indicating whether the given package exists in this registry.
    /// @param packageName Package Name
    function packageExists(string memory packageName) public view returns (bool) {
        bytes32 packageId = generatePackageId(packageName);
        return packages[packageId].exists;
    }

    //
    //  ====================
    //  |  Hash Functions  |
    //  ====================
    // 

    /// @dev Returns name hash for a given package name.
    /// @param name Package name
    function generatePackageId(string memory name)
        public
        pure
        returns (bytes32)
    {
        return keccak256(abi.encodePacked(name));
    }

    // @dev Returns release id that *would* be generated for a name and version pair on `release`.
    // @param packageName Package name
    // @param version Version string (ex: '1.0.0')
    function generateReleaseId(
        string memory packageName,
        string memory version
    )
        public
        view
        returns (bytes32)
    {
        return keccak256(abi.encodePacked(packageName, version));
    }

    function generatePackageReleaseId(
        bytes32 packageId,
        uint packageReleaseCount
    )
        private
		pure
        returns (bytes32)
    {
        return keccak256(abi.encodePacked(packageId, packageReleaseCount));
    }


    //
    // ================
    // |  Validation  |
    // ================
    //

    /// @dev Returns boolean whether the provided package name is valid.
    /// @param name The name of the package.
    function validatePackageName(string memory name)
        public
        pure
        returns (bool)
    {
        require (bytes(name).length > 2 && bytes(name).length < 255, "invalid-package-name");
    }

    /// @dev Returns boolean whether the input string has a length
    /// @param value The string to validate.
    function validateStringIdentifier(string memory value)
        public
        pure
        returns (bool)
    {
        require (bytes(value).length != 0, "invalid-string-identifier");
    }
}
