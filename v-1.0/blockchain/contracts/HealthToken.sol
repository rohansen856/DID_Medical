// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

abstract contract HealthToken is ERC20, Ownable {
    constructor() ERC20("HealthToken", "HLTH") {}

    // Function to mint tokens, for example, when a patient buys tokens
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    // Function for patients to buy tokens by sending ETH
    function buyTokens() public payable {
        uint256 amountToMint = msg.value * 100; // Assuming 1 ETH = 100 HLTH
        _mint(msg.sender, amountToMint);
    }
}
