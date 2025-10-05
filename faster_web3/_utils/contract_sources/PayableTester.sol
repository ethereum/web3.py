pragma solidity >=0.6.0;


contract PayableTesterContract {
  bool public wasCalled;

  function doNoValueCall() external {
      wasCalled = true;
  }
}
