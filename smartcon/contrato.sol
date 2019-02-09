pragma solidity 0.4.21;

contract contar {

	int private count = 0;
	address owner 0x928783707f0a4ed28D3e9C78eC68BBF2378bDFc8;
	uint cliente = 35;
	bytes32 name "contrato um";

	function incrementCounter() public {
		count += 1;
	}
	function decrementCounter() public {
		count -= 1;
	}
	function getCount() public constant returns (int) {
		return count;
	}
}