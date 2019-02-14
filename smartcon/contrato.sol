pragma solidity 0.4.21;

contract contar {

	int private count = 0;
	address owner 0x1e09A112E4ed183aa3083082749383f209bb7785;
	uint cliente = 1;
	bytes32 name "Contrato";

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