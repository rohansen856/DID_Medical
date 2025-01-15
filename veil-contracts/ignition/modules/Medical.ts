import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const MedicalModule = buildModule("MedicalModule", (m) => {

  const Medical = m.contract("MedicalContract", [process.env.TOKEN_ADDRESS!]);

  return { Medical };
});

export default MedicalModule;
