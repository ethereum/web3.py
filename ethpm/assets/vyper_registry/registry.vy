# Vyper Reference Implementation of ERC1319

# Structs
struct Package:
	exists: bool
	createdAt: timestamp
	updatedAt: timestamp
	name: bytes32
	releaseCount: int128

struct Release:
	exists: bool
	createdAt: timestamp
	packageId: bytes32
	version: bytes32
	uri: bytes[1000]

	
# Events
VersionRelease: event({_package: indexed(bytes32), _version: bytes32, _uri: bytes[1000]})

owner: public(address)

# Package Data: (package_id => value)
packages: public(map(bytes32, Package))

#  Release Data: (release_id => value)
releases: public(map(bytes32, Release))


# package_id#release_count => release_id
packageReleaseIndex: map(bytes32, bytes32)
# Total number of packages in registry
packageCount: public(int128)
# Total number of releases in registry
releaseCount: public(int128)
# Total package number (int128) => package_id (bytes32)
packageIds: map(int128, bytes32)
# Total release number (int128) => release_id (bytes32)
releaseIds: map(int128, bytes32)

EMPTY_BYTES: bytes32


@public
def __init__():
    self.owner = msg.sender


@public
def transferOwner(newOwner: address):
    assert self.owner == msg.sender
    self.owner = newOwner


@public
def getReleaseId(packageName: bytes32, version: bytes32) -> bytes32:
    releaseConcat: bytes[64] = concat(packageName, version)
    releaseId: bytes32 = sha3(releaseConcat)
    assert self.releases[releaseId].exists
    return releaseId


@public
def generateReleaseId(packageName: bytes32, version: bytes32) -> bytes32:
    releaseConcat: bytes[64] = concat(packageName, version)
    releaseId: bytes32 = sha3(releaseConcat)
    return releaseId


@public
def getPackageName(packageId: bytes32) -> bytes32:
    assert self.packages[packageId].exists
    return self.packages[packageId].name


@public
def getPackageData(packageName: bytes32) -> (bytes32, bytes32, int128):
    packageId: bytes32 = sha3(packageName)
    assert self.packages[packageId].exists
    return (
        self.packages[packageId].name,
        packageId,
        self.packages[packageId].releaseCount,
    )


@public
def numPackageIds() -> int128:
    return self.packageCount


@public
def numReleaseIds(packageName: bytes32) -> int128:
    packageId: bytes32 = sha3(packageName)
    assert self.packages[packageId].exists
    return self.packages[packageId].releaseCount


@public
def getAllPackageIds(
    offset: uint256, length: uint256
) -> (bytes32, bytes32, bytes32, bytes32, bytes32):
    offset_int: int128 = convert(offset, int128)
    length_int: int128 = convert(length, int128)
    assert length_int == 5
    assert offset_int <= self.packageCount
    ids: bytes32[5]
    for idx in range(offset_int, offset_int + 4):
        if idx <= self.packageCount:
            packageId: bytes32 = self.packageIds[idx]
            ids[(idx - offset_int)] = packageId
        else:
            ids[(idx - offset_int)] = self.EMPTY_BYTES
    return (ids[0], ids[1], ids[2], ids[3], ids[4])


@private
def generatePackageReleaseId(packageId: bytes32, count: int128) -> bytes32:
    countBytes: bytes32 = convert(count, bytes32)
    packageReleaseTag: bytes[64] = concat(packageId, countBytes)
    packageReleaseId: bytes32 = sha3(packageReleaseTag)
    return packageReleaseId


@public
def getAllReleaseIds(
    packageName: bytes32, offset: uint256, length: uint256
) -> (bytes32, bytes32, bytes32, bytes32, bytes32):
    offset_int: int128 = convert(offset, int128)
    length_int: int128 = convert(length, int128)
    assert length_int == 5
    packageId: bytes32 = sha3(packageName)
    assert self.packages[packageId].exists
    assert offset_int <= self.packages[packageId].releaseCount
    ids: bytes32[5]
    for idx in range(offset_int, offset_int + 4):
        if idx <= self.packages[packageId].releaseCount:
            packageReleaseId: bytes32 = self.generatePackageReleaseId(
                packageId, (idx + 1)
            )
            releaseId: bytes32 = self.packageReleaseIndex[packageReleaseId]
            ids[(idx - offset_int)] = releaseId
        else:
            ids[(idx - offset_int)] = self.EMPTY_BYTES
    return (ids[0], ids[1], ids[2], ids[3], ids[4])


@public
def getReleaseData(releaseId: bytes32) -> (bytes32, bytes32, bytes[1000]):
    assert self.releases[releaseId].exists
    packageId: bytes32 = self.releases[releaseId].packageId
    return (
        self.packages[packageId].name,
        self.releases[releaseId].version,
        self.releases[releaseId].uri,
    )


@private
def cutRelease(
    releaseId: bytes32,
    packageId: bytes32,
    version: bytes32,
    uri: bytes[1000],
    name: bytes32,
):
    self.releases[releaseId] = Release({
        exists: True,
        createdAt: block.timestamp,
        packageId: packageId,
        version: version,
        uri: uri,
    })
    self.packages[packageId].releaseCount += 1
    self.releaseIds[self.releaseCount] = releaseId
    self.releaseCount += 1
    packageReleaseId: bytes32 = self.generatePackageReleaseId(
        packageId, self.packages[packageId].releaseCount
    )
    self.packageReleaseIndex[packageReleaseId] = releaseId
    log.VersionRelease(name, version, uri)


@public
def release(packageName: bytes32, version: bytes32, manifestURI: bytes[1000]):
    assert packageName != self.EMPTY_BYTES
    assert version != self.EMPTY_BYTES
    assert len(manifestURI) > 0
    assert self.owner == msg.sender


    packageId: bytes32 = sha3(packageName)
    releaseId: bytes32 = self.generateReleaseId(packageName, version)

    if self.packages[packageId].exists == True:
        self.packages[packageId] = Package({
            exists: True,
            createdAt: self.packages[packageId].createdAt,
            updatedAt: block.timestamp,
            name: packageName,
            releaseCount: self.packages[packageId].releaseCount,
        })
        assert self.releases[releaseId].exists == False
        self.cutRelease(releaseId, packageId, version, manifestURI, packageName)
    else:
        self.packages[packageId] = Package({
            exists: True,
            createdAt: block.timestamp,
            updatedAt: block.timestamp,
            name: packageName,
            releaseCount: 0,
        })
        self.packageIds[self.packageCount] = packageId
        self.packageCount += 1
        self.cutRelease(releaseId, packageId, version, manifestURI, packageName)
