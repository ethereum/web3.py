// This contract is meant to test CCIP Read / Offchain Lookup functionality as part of EIP-3668. Multiple functions
// may be added here for testing and the contract can be recompiled for `test_offchain_lookup.py` and other tests.

pragma solidity ^0.8.13;

contract OffchainLookup {
    string[] urls = ["https://web3.py/gateway/{sender}/{data}.json", "https://web3.py/gateway"];

    error OffchainLookup(address sender, string[] urls, bytes callData, bytes4 callbackFunction, bytes extraData);

    // This function is meant to test the offchain lookup functionality specified in EIP-3668.
    function testOffchainLookup(bytes calldata specifiedDataFromTest) external returns(bytes memory) {
        // assert that the test specifies "offchain lookup test" to start the test
        string memory dataFromTestAsString = abi.decode(specifiedDataFromTest, (string));
        require(keccak256(abi.encodePacked(dataFromTestAsString)) == keccak256("test offchain lookup"), "test data validation failed.");

        revert OffchainLookup(
            address(this),
            urls,
            specifiedDataFromTest,
            this.testOffchainLookupWithProof.selector,
            specifiedDataFromTest
        );
    }

    function testOffchainLookupWithProof(bytes calldata result, bytes calldata extraData) external returns(bytes memory) {
        // assert the result came from the mocked response from our tests... must mock in tests with the appropriate
        // value and validate the assertion here.
        string memory resultAsString = abi.decode(result, (string));
        require(keccak256(abi.encodePacked(resultAsString)) == keccak256("web3py"), "http request result validation failed.");

        // assert this `extraData` value is the same test-provided value from the original revert at `testOffchainLookup()`
        string memory extraDataAsString = abi.decode(extraData, (string));
        require(keccak256(abi.encodePacked(extraDataAsString)) == keccak256("test offchain lookup"), "extraData validation failed.");

        return result;
    }

    // This function is meant to test that continuous OffchainLookup reverts raise an exception after too many
    // redirects. This example technically breaks the flow described in EIP-3668 but this is solely meant to trigger
    // continuous OffchainLookup reverts and test that we catch this sort of activity and stop it. Currently this limit
    // is set to 4 redirects.
    function continuousOffchainLookup() external returns(bytes memory) {
        bytes memory _callData;

        revert OffchainLookup(
            address(this),
            urls,
            _callData,
            this.continuousOffchainLookup.selector,
            _callData
        );
    }
}
