// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./HealthToken.sol";

contract MedicalContract {
    HealthToken public healthToken;

    struct Doctor {
        address doctorAddress;
        string name;
        string speciality;
        uint256 fees; // Fee amount in HealthToken
        uint256 tokenBalance; // Balance of HealthTokens for each doctor
        bool verified;
    }

    struct Patient {
        address patientAddress;
        string name;
    }

    struct Medication {
        string name;
        string dosage;
        uint256 duration; // in days
        string additionalInstructions;
    }

    struct PrescriptionData {
        uint256 id;
        address doctorAddress;
        address patientAddress;
        Medication[] medications;
        uint256 issueDate;
        string diagnosis; // New field for diagnosis
        bool active;
    }

    mapping(address => Doctor) public doctors;
    mapping(address => Patient) public patients;
    mapping(uint256 => PrescriptionData) public prescriptions;
    uint256 public prescriptionCounter;

    event DoctorRegistered(address doctorAddress, string name, uint256 fees);
    event PrescriptionIssued(uint256 id, address doctorAddress, address patientAddress, string diagnosis);
    event PaymentReceived(address indexed patient, address indexed doctor, uint256 amount);
    event TokensWithdrawn(address indexed doctor, uint256 tokenAmount, uint256 ethAmount);

    modifier onlyVerifiedDoctor() {
        require(doctors[msg.sender].verified, "Not a verified doctor");
        _;
    }

    modifier doctorExists(address doctorAddress) {
        require(doctors[doctorAddress].verified, "Doctor is not registered or verified");
        _;
    }

    modifier patientExists(address patientAddress) {
        require(patients[patientAddress].patientAddress != address(0), "Patient is not registered");
        _;
    }

    // Constructor to set the HealthToken contract address
    constructor(address _healthTokenAddress) {
        healthToken = HealthToken(_healthTokenAddress);
    }

    // Register a doctor with a specified fee in HealthTokens
    function registerDoctor(string memory name, string memory speciality, uint256 fees) public {
        require(!doctors[msg.sender].verified, "Doctor already registered");
        doctors[msg.sender] = Doctor(msg.sender, name, speciality, fees, 0, true);
        emit DoctorRegistered(msg.sender, name, fees);
    }

    // Register a patient
    function registerPatient(string memory name) public {
        require(bytes(name).length > 0, "Name required");
        patients[msg.sender] = Patient(msg.sender, name);
    }

    // Issue a prescription with a diagnosis
    function issuePrescription(
        address patientAddress,
        Medication[] memory medications,
        string memory diagnosis
    ) public onlyVerifiedDoctor patientExists(patientAddress) {
        prescriptionCounter++;
        PrescriptionData storage newPrescription = prescriptions[prescriptionCounter];
        newPrescription.id = prescriptionCounter;
        newPrescription.doctorAddress = msg.sender;
        newPrescription.patientAddress = patientAddress;
        newPrescription.issueDate = block.timestamp;
        newPrescription.diagnosis = diagnosis; // Set the diagnosis
        newPrescription.active = true;

        for (uint i = 0; i < medications.length; i++) {
            newPrescription.medications.push(medications[i]);
        }

        emit PrescriptionIssued(prescriptionCounter, msg.sender, patientAddress, diagnosis);
    }

    // Patient pays the doctor in HealthTokens
    function payDoctor(address doctorAddress, uint256 amount) public doctorExists(doctorAddress) patientExists(msg.sender) {
        Doctor storage doctor = doctors[doctorAddress];
        require(amount >= doctor.fees, "Insufficient payment amount");

        // Transfer HealthTokens from patient to the doctor
        require(healthToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the doctor's token balance
        doctor.tokenBalance += amount;

        emit PaymentReceived(msg.sender, doctorAddress, amount);
    }

    // Doctor withdraws tokens for ETH
    function withdrawTokens(uint256 tokenAmount) public onlyVerifiedDoctor {
        Doctor storage doctor = doctors[msg.sender];
        require(doctor.tokenBalance >= tokenAmount, "Insufficient token balance");

        // Calculate ETH equivalent (assuming 1 ETH = 100 HLTH)
        uint256 ethAmount = tokenAmount / 100;
        
        // Update doctor’s token balance
        doctor.tokenBalance -= tokenAmount;

        // Transfer tokens back to the HealthToken contract for burning
        require(healthToken.transfer(address(healthToken), tokenAmount), "Token transfer failed");

        // Transfer ETH to the doctor
        payable(doctor.doctorAddress).transfer(ethAmount);

        emit TokensWithdrawn(msg.sender, tokenAmount, ethAmount);
    }

    // Get doctor fee in HealthToken
    function getDoctorFee(address doctorAddress) public view doctorExists(doctorAddress) returns (uint256) {
        return doctors[doctorAddress].fees;
    }
}
