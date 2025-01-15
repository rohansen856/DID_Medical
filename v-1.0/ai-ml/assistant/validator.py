import json
from pydantic import ValidationError
from datetime import datetime
from bson import ObjectId

# Import the models (assuming the previous code is in a module named `models`)
from models import PatientHistoryData

def load_patient_data(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def validate_patient_data(data: dict) -> PatientHistoryData:
    # Convert string ObjectIds to actual ObjectId instances
    data['_id'] = ObjectId(data['_id'])
    data['userId'] = ObjectId(data['userId'])
    
    data['demographics']['_id'] = ObjectId(data['demographics']['_id'])
    data['demographics']['userId'] = ObjectId(data['demographics']['userId'])
    
    data['medicalHistory']['_id'] = ObjectId(data['medicalHistory']['_id'])
    data['medicalHistory']['userId'] = ObjectId(data['medicalHistory']['userId'])

    data['allergies']['_id'] = ObjectId(data['allergies']['_id'])
    data['allergies']['userId'] = ObjectId(data['allergies']['userId'])

    data['medications']['_id'] = ObjectId(data['medications']['_id'])
    data['medications']['userId'] = ObjectId(data['medications']['userId'])

    data['visits']['_id'] = ObjectId(data['visits']['_id'])
    data['visits']['userId'] = ObjectId(data['visits']['userId'])

    data['tests']['_id'] = ObjectId(data['tests']['_id'])
    data['tests']['userId'] = ObjectId(data['tests']['userId'])

    data['prescriptions']['_id'] = ObjectId(data['prescriptions']['_id'])
    data['prescriptions']['userId'] = ObjectId(data['prescriptions']['userId'])

    data['immunizations']['_id'] = ObjectId(data['immunizations']['_id'])
    data['immunizations']['userId'] = ObjectId(data['immunizations']['userId'])

    data['insuranceInfo']['_id'] = ObjectId(data['insuranceInfo']['_id'])
    data['insuranceInfo']['userId'] = ObjectId(data['insuranceInfo']['userId'])

    data['emergencyContacts']['_id'] = ObjectId(data['emergencyContacts']['_id'])
    data['emergencyContacts']['userId'] = ObjectId(data['emergencyContacts']['userId'])

    # Convert string dates to datetime instances
    for key in ['createdAt', 'updatedAt']:
        data[key] = datetime.fromisoformat(data[key].replace("Z", "+00:00"))
    
    # Validate data
    return PatientHistoryData(**data)

if __name__ == "__main__":
    json_file_path = 'seed2.json'
    patient_data = load_patient_data(json_file_path)

    try:
        validated_data = validate_patient_data(patient_data)
        print("Patient data validated successfully!")
        print(validated_data.model_dump_json(indent=2))  # Print the validated data in JSON format
    except ValidationError as e:
        print("Validation error:", e.json())
