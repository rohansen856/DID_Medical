import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const HealthTokenModule = buildModule("HealthTokenModule", (m) => {

  const HealthToken = m.contract("HealthToken", []);

  return { HealthToken };
});

export default HealthTokenModule;
