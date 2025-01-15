# Veil Contracts Project

## Overview

The Veil Contracts Project is a blockchain-based medical system built using Solidity and Hardhat. It includes smart contracts for managing a healthcare ecosystem with functionalities such as registering doctors and patients, issuing prescriptions, handling token-based payments, and allowing doctors to withdraw earnings. The system is powered by a custom ERC20 token, `HealthToken (HLTH)`, facilitating secure and efficient transactions within the ecosystem.

## Features

- HealthToken (HLTH)
   - ERC20 Token Contract: Implements the ERC20 standard using OpenZeppelin.
   - Minting: The owner can mint tokens, and patients can buy tokens by sending ETH.
   - Buying Tokens: Patients can convert ETH into HLTH tokens at a rate of 1 ETH = 100 HLTH.
- MedicalContract
    - Doctor Registration: Allows new doctors to register with their details and consultation fees. Each doctor is marked as verified.
    - Patient Registration: Enables patients to register by providing basic information.
   - Prescription Issuance: Verified doctors can issue prescriptions to registered patients, including medication details and a diagnosis.
   - Payment System: Patients can pay doctors for services in HLTH tokens. The token transfer is verified to ensure sufficient balance and successful transfer.
   - Token Withdrawal: Verified doctors can convert their token earnings into ETH and withdraw them. The tokens are transferred back to the contract, and an equivalent amount of ETH is sent to the doctor.

## Smart Contract Breakdown

### `HealthToken.sol`
- Abstract `Contract` extending `ERC20` and Ownable.
- Provides functions:
     - `mint(address to, uint256 amount)`: Allows the contract owner to mint new tokens.
     - `buyTokens()`: Allows users to purchase tokens by sending ETH, minting tokens at a conversion rate of `1 ETH = 100 HLTH`.

### `MedicalContract.sol`
- `State Variables`:
   - `Mappings` to store registered doctors, patients, and prescription data.
   - A `counter` for tracking prescription IDs.
- `Structures`:
   - `Doctor`: Contains information about a doctor, including fees, token balance, and verification status.
   - `Patient`: Basic information about registered patients.
   - `Medication`: Details about prescribed medication.
   - `PrescriptionData`: Contains the prescription details, including medications and a diagnosis.
- `Events`:
   - `DoctorRegistered`: Emitted when a new doctor registers.
   - `PrescriptionIssued`: Emitted when a prescription is created.
   - `PaymentReceived`: Emitted when a patient makes a payment to a doctor.
   - `TokensWithdrawn`: Emitted when a doctor withdraws tokens and receives ETH.
   - `Modifiers`:
        - `onlyVerifiedDoctor`: Restricts certain actions to verified doctors.
        - `doctorExists`: Ensures a doctor is registered and verified.
        - `patientExists`: Ensures a patient is registered.
- `Functions`:
    - `registerDoctor`: Allows new doctors to register with their information.
    - `registerPatient`: Registers a patient with their name.
    - `issuePrescription`: Creates a new prescription record for a patient.
    - `payDoctor`: Handles the payment process from a patient to a doctor in HLTH tokens.
    - `withdrawTokens` : Enables doctors to withdraw tokens and receive ETH equivalent.


## Installation and Setup

Follow the steps below to install and set up the Veil Contracts Project:

### Prerequisites
Ensure you have the following installed:

- Node.js (v14 or higher)
- npm (comes with Node.js)
- Hardhat (Ethereum development framework)
- Ganache (local Ethereum blockchain for testing)
- Metamask (or any other Ethereum-compatible wallet)

### Steps to setup the Project

 Clone the repository:-

```bash
git clone https://github.com/Ctrl-Crew/veil-contracts.git
cd veil-contracts
```

Install Dependencies: Navigate to the project directory and install all required dependencies:

```bash
npm install
```

Compile Smart Contracts: Compile the smart contracts using Hardhat to ensure they are error-free:

```bash
npx hardhat compile
```
Run a Local Ethereum Node: Start a local Ethereum blockchain using Ganache or Hardhat node:

```bash
npx hardhat node
```

Deploy Contracts: Deploy the contracts to your local network (e.g., Ganache) using the Ignition module:

```bash
npx hardhat ignition deploy ./ignition/modules/HealthToken.ts --network ganache
```

Run Tests: Run the test suite to ensure the contracts function as expected:

```bash
npx hardhat test
```

Create a .env file in the project root directory to store environment-specific variables. Include necessary values like network URLs or private keys:

```
NETWORK_URL="http://127.0.0.1:8545"
DEPLOYER_PRIVATE_KEY="your_private_key_here"
PRIVATE_KEY=your_wallet_private_key
```

Running the Project
- Start your local blockchain network (Ganache or Hardhat node).
- Deploy the smart contracts using the command provided above.
- Use Hardhat's console or custom scripts to interact with the contracts.


