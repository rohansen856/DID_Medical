from datetime import datetime
from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field, field_validator


class Address(BaseModel):
    street: str
    city: str
    state: str
    postalCode: str
    country: str


class Clinic(BaseModel):
    name: str
    address: Address


class Surgery(BaseModel):
    name: str
    date: datetime
    hospital: str
    notes: Optional[str]


class Hospitalization(BaseModel):
    reason: str
    startDate: datetime
    endDate: datetime
    hospital: str
    notes: Optional[str]


class FamilyMedicalHistory(BaseModel):
    condition: str
    relationship: str
    ageAtDiagnosis: int
    notes: Optional[str]


class Allergy(BaseModel):
    name: str
    reaction: str
    severity: str
    diagnosedDate: datetime
    notes: Optional[str]


class Medication(BaseModel):
    name: str
    dosage: str
    frequency: str
    route: str
    startDate: datetime
    endDate: Optional[datetime]
    effectiveness: str
    sideEffects: List[str]
    notes: Optional[str]


class Diagnosis(BaseModel):
    condition: str
    severity: str
    dateDiagnosed: datetime
    notes: Optional[str]


class Treatment(BaseModel):
    type: str
    description: str
    duration: str
    prescribedMedication: List[Medication]
    notes: Optional[str]


class Visit(BaseModel):
    visitId: ObjectId
    date: datetime
    reason: str
    clinic: Clinic
    diagnosis: List[Diagnosis]
    treatments: List[Treatment]
    followUpDate: Optional[datetime]
    notes: Optional[str]


class Laboratory(BaseModel):
    name: str
    address: Address


class Test(BaseModel):
    testName: str
    datePerformed: datetime
    result: str
    normalRange: str
    units: str
    notes: Optional[str]
    laboratory: Laboratory


class RefillInfo(BaseModel):
    refillsRemaining: int
    lastRefillDate: datetime
    nextRefillDate: datetime


class Prescription(BaseModel):
    medication: Medication
    prescribedDate: datetime
    dosageInstructions: str
    duration: str
    refillInfo: RefillInfo
    notes: Optional[str]


class Immunization(BaseModel):
    vaccineName: str
    dateAdministered: datetime
    doseNumber: int
    totalDoses: int
    site: str
    notes: Optional[str]


class CoverageDetail(BaseModel):
    type: str
    description: str
    copay: float
    deductible: float


class InsuranceInfo(BaseModel):
    provider: str
    policyNumber: str
    coverageDetails: List[CoverageDetail]
    validUntil: datetime
    createdAt: datetime
    updatedAt: datetime


class EmergencyContact(BaseModel):
    relationship: str
    phone: str
    address: Address
    notes: Optional[str]


class PatientDemographics(BaseModel):
    userId: ObjectId
    gender: str
    dateOfBirth: datetime
    bloodType: str
    maritalStatus: str
    occupation: str
    race: str
    ethnicity: str
    language: str
    religion: str
    disabilityStatus: str
    createdAt: datetime
    updatedAt: datetime


class MedicalHistory(BaseModel):
    userId: ObjectId
    chronicDiseases: List[str]
    pastIllnesses: List[str]
    surgeries: List[Surgery]
    hospitalizations: List[Hospitalization]
    familyMedicalHistory: List[FamilyMedicalHistory]
    createdAt: datetime
    updatedAt: datetime


class Allergies(BaseModel):
    userId: ObjectId
    allergies: List[Allergy]
    createdAt: datetime
    updatedAt: datetime


class Medications(BaseModel):
    userId: ObjectId
    medications: List[Medication]
    createdAt: datetime
    updatedAt: datetime


class Visits(BaseModel):
    userId: ObjectId
    visits: List[Visit]
    createdAt: datetime
    updatedAt: datetime


class Tests(BaseModel):
    userId: ObjectId
    tests: List[Test]
    createdAt: datetime
    updatedAt: datetime


class Prescriptions(BaseModel):
    userId: ObjectId
    prescriptions: List[Prescription]
    createdAt: datetime
    updatedAt: datetime


class Immunizations(BaseModel):
    userId: ObjectId
    immunizations: List[Immunization]
    createdAt: datetime
    updatedAt: datetime


class EmergencyContacts(BaseModel):
    userId: ObjectId
    emergencyContacts: List[EmergencyContact]
    createdAt: datetime
    updatedAt: datetime


class PatientHistoryData(BaseModel):
    demographics: PatientDemographics
    medicalHistory: MedicalHistory
    allergies: Allergies
    medications: Medications
    visits: Visits
    tests: Tests
    prescriptions: Prescriptions
    immunizations: Immunizations
    insuranceInfo: InsuranceInfo
    emergencyContacts: EmergencyContacts

    # Custom validator example
    @field_validator('*', pre=True, each_item=True)
    def check_dates(cls, value):
        if isinstance(value, datetime):
            return value
        raise ValueError("Dates must be in datetime format")
