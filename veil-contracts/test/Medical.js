const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("MedicalContract", function () {
  let HealthToken, healthToken, MedicalContract, medicalContract;
  let owner, doctor, patient;

  beforeEach(async function () {
    [owner, doctor, patient] = await ethers.getSigners();

    // Deploy HealthToken contract
    HealthToken = await ethers.getContractFactory("HealthTokenImpl"); // Use the implementation we discussed
    healthToken = await HealthToken.deploy();
    await healthToken.deployed();

    // Deploy MedicalContract with the address of HealthToken
    MedicalContract = await ethers.getContractFactory("MedicalContract");
    medicalContract = await MedicalContract.deploy(healthToken.address);
    await medicalContract.deployed();

    // Mint some HealthTokens to the patient for testing
    await healthToken.mint(patient.address, ethers.utils.parseUnits("1000", 18)); // 1000 HLTH tokens
  });

  describe("Doctor and Patient Registration", function () {
    it("Should allow a doctor to register", async function () {
      await expect(
        medicalContract.connect(doctor).registerDoctor("Dr. Smith", "Cardiology", ethers.utils.parseUnits("100", 18))
      )
        .to.emit(medicalContract, "DoctorRegistered")
        .withArgs(doctor.address, "Dr. Smith", ethers.utils.parseUnits("100", 18));

      const registeredDoctor = await medicalContract.doctors(doctor.address);
      expect(registeredDoctor.name).to.equal("Dr. Smith");
      expect(registeredDoctor.speciality).to.equal("Cardiology");
      expect(registeredDoctor.fees.toString()).to.equal(ethers.utils.parseUnits("100", 18).toString());
      expect(registeredDoctor.verified).to.be.true;
    });

    it("Should allow a patient to register", async function () {
      await medicalContract.connect(patient).registerPatient("John Doe");
      const registeredPatient = await medicalContract.patients(patient.address);
      expect(registeredPatient.name).to.equal("John Doe");
    });
  });

  describe("Issuing Prescriptions", function () {
    it("Should allow a verified doctor to issue a prescription", async function () {
      await medicalContract.connect(doctor).registerDoctor("Dr. Smith", "Cardiology", ethers.utils.parseUnits("100", 18));

      const medications = [
        { name: "Medication A", dosage: "10mg", duration: 30, additionalInstructions: "Take with food" },
        { name: "Medication B", dosage: "20mg", duration: 15, additionalInstructions: "Avoid sunlight" }
      ];

      await expect(medicalContract.connect(doctor).issuePrescription(patient.address, medications))
        .to.emit(medicalContract, "PrescriptionIssued")
        .withArgs(1, doctor.address, patient.address);

      const prescription = await medicalContract.prescriptions(1);
      expect(prescription.doctorAddress).to.equal(doctor.address);
      expect(prescription.patientAddress).to.equal(patient.address);
      expect(prescription.active).to.be.true;
    });

    it("Should revert if a non-verified doctor tries to issue a prescription", async function () {
      const medications = [{ name: "Medication A", dosage: "10mg", duration: 30, additionalInstructions: "Take with food" }];
      await expect(medicalContract.connect(doctor).issuePrescription(patient.address, medications)).to.be.revertedWith("Not a verified doctor");
    });
  });

  describe("Paying Doctor", function () {
    beforeEach(async function () {
      await medicalContract.connect(doctor).registerDoctor("Dr. Smith", "Cardiology", ethers.utils.parseUnits("100", 18));
      await healthToken.connect(patient).approve(medicalContract.address, ethers.utils.parseUnits("100", 18));
    });

    it("Should allow a patient to pay a doctor in HealthTokens", async function () {
      await expect(medicalContract.connect(patient).payDoctor(doctor.address, ethers.utils.parseUnits("100", 18)))
        .to.emit(medicalContract, "PaymentReceived")
        .withArgs(patient.address, doctor.address, ethers.utils.parseUnits("100", 18));

      const doctorData = await medicalContract.doctors(doctor.address);
      expect(doctorData.tokenBalance.toString()).to.equal(ethers.utils.parseUnits("100", 18).toString());
    });

    it("Should revert if payment is below the doctor's fees", async function () {
      await expect(medicalContract.connect(patient).payDoctor(doctor.address, ethers.utils.parseUnits("50", 18))).to.be.revertedWith("Insufficient payment amount");
    });
  });

  describe("Withdrawing Tokens", function () {
    beforeEach(async function () {
      await medicalContract.connect(doctor).registerDoctor("Dr. Smith", "Cardiology", ethers.utils.parseUnits("100", 18));
      await healthToken.connect(patient).approve(medicalContract.address, ethers.utils.parseUnits("200", 18));
      await medicalContract.connect(patient).payDoctor(doctor.address, ethers.utils.parseUnits("200", 18)); // Pay doctor 200 HLTH
    });

    it("Should allow a verified doctor to withdraw tokens for ETH", async function () {
      const initialEthBalance = await ethers.provider.getBalance(doctor.address);

      await expect(medicalContract.connect(doctor).withdrawTokens(ethers.utils.parseUnits("100", 18)))
        .to.emit(medicalContract, "TokensWithdrawn")
        .withArgs(doctor.address, ethers.utils.parseUnits("100", 18), ethers.utils.parseEther("1")); // Assuming 1 ETH = 100 HLTH

      const finalEthBalance = await ethers.provider.getBalance(doctor.address);
      expect(finalEthBalance.sub(initialEthBalance)).to.equal(ethers.utils.parseEther("1"));

      const doctorData = await medicalContract.doctors(doctor.address);
      expect(doctorData.tokenBalance.toString()).to.equal(ethers.utils.parseUnits("100", 18).toString()); // 200 - 100 withdrawn
    });

    it("Should revert if a doctor tries to withdraw more tokens than their balance", async function () {
      await expect(medicalContract.connect(doctor).withdrawTokens(ethers.utils.parseUnits("300", 18))).to.be.revertedWith("Insufficient token balance");
    });
  });
});
