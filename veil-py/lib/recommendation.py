import google.generativeai as genai
import random
from typing import List, TypedDict
from dotenv import load_dotenv
import os
import json

load_dotenv()

genai.configure(api_key=os.getenv("gemini"))

model = genai.GenerativeModel("gemini-1.5-flash")


class Doctor(TypedDict):
    id: int
    userId: str
    phoneNumber: str
    aadharNumber: str
    mbbsId: str
    specialty: str
    verified: bool
    blockId: str
    appointments: list
    Prescription: list
    user: dict


# Fetch doctor data from database
def fetch_doctors_from_database() -> List[Doctor]:
    return [
        {
            "id": 1,
            "userId": "user123",
            "phoneNumber": "1234567890",
            "aadharNumber": "123456789012",
            "mbbsId": "MBBS123",
            "specialty": "Orthopedic",
            "verified": True,
            "blockId": "block1",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 1,
                "name": "Dr. Robert Smith",
                "email": "dr.robertsmith@example.com",
            },
        },
        {
            "id": 2,
            "userId": "user456",
            "phoneNumber": "9876543210",
            "aadharNumber": "987654321012",
            "mbbsId": "MBBS456",
            "specialty": "Neurosurgeon",
            "verified": True,
            "blockId": "block2",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 2,
                "name": "Dr. Jane Doe",
                "email": "dr.janedoe@example.com",
            },
        },
        {
            "id": 3,
            "userId": "user789",
            "phoneNumber": "5551234567",
            "aadharNumber": "555123456789",
            "mbbsId": "MBBS789",
            "specialty": "Orthopedic",
            "verified": True,
            "blockId": "block3",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 3,
                "name": "Dr. John Brown",
                "email": "dr.johnbrown@example.com",
            },
        },
        {
            "id": 4,
            "userId": "user101",
            "phoneNumber": "1231231234",
            "aadharNumber": "123123123456",
            "mbbsId": "MBBS101",
            "specialty": "Cardiologist",
            "verified": True,
            "blockId": "block4",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 4,
                "name": "Dr. Alice White",
                "email": "dr.alicewhite@example.com",
            },
        },
        {
            "id": 5,
            "userId": "user102",
            "phoneNumber": "7897897890",
            "aadharNumber": "789789789012",
            "mbbsId": "MBBS102",
            "specialty": "Dermatologist",
            "verified": True,
            "blockId": "block5",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 5,
                "name": "Dr. Samuel Green",
                "email": "dr.samuelgreen@example.com",
            },
        },
        {
            "id": 6,
            "userId": "user103",
            "phoneNumber": "4564564567",
            "aadharNumber": "456456456789",
            "mbbsId": "MBBS103",
            "specialty": "Pediatrician",
            "verified": True,
            "blockId": "block6",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 6,
                "name": "Dr. Laura Adams",
                "email": "dr.lauraadams@example.com",
            },
        },
        {
            "id": 7,
            "userId": "user104",
            "phoneNumber": "1234567899",
            "aadharNumber": "123456789911",
            "mbbsId": "MBBS104",
            "specialty": "General Physician",
            "verified": True,
            "blockId": "block7",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 7,
                "name": "Dr. Michael Johnson",
                "email": "dr.michaeljohnson@example.com",
            },
        },
        {
            "id": 8,
            "userId": "user105",
            "phoneNumber": "5675675670",
            "aadharNumber": "567567567890",
            "mbbsId": "MBBS105",
            "specialty": "Cardiologist",
            "verified": True,
            "blockId": "block8",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 8,
                "name": "Dr. Karen Black",
                "email": "dr.karenblack@example.com",
            },
        },
        {
            "id": 9,
            "userId": "user106",
            "phoneNumber": "1112223334",
            "aadharNumber": "111222333444",
            "mbbsId": "MBBS106",
            "specialty": "Oncologist",
            "verified": True,
            "blockId": "block9",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 9,
                "name": "Dr. Tom Lee",
                "email": "dr.tomlee@example.com",
            },
        },
        {
            "id": 10,
            "userId": "user107",
            "phoneNumber": "4445556667",
            "aadharNumber": "444555666777",
            "mbbsId": "MBBS107",
            "specialty": "Gastroenterologist",
            "verified": True,
            "blockId": "block10",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 10,
                "name": "Dr. Angela Brown",
                "email": "dr.angelabrown@example.com",
            },
        },
        {
            "id": 11,
            "userId": "user108",
            "phoneNumber": "7891234560",
            "aadharNumber": "789123456789",
            "mbbsId": "MBBS108",
            "specialty": "Orthopedic",
            "verified": True,
            "blockId": "block11",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 11,
                "name": "Dr. Jacob Martinez",
                "email": "dr.jacobmartinez@example.com",
            },
        },
        {
            "id": 12,
            "userId": "user109",
            "phoneNumber": "9998887776",
            "aadharNumber": "999888777666",
            "mbbsId": "MBBS109",
            "specialty": "Neurologist",
            "verified": True,
            "blockId": "block12",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 12,
                "name": "Dr. Emily Davis",
                "email": "dr.emilydavis@example.com",
            },
        },
        {
            "id": 13,
            "userId": "user110",
            "phoneNumber": "3332221110",
            "aadharNumber": "333222111000",
            "mbbsId": "MBBS110",
            "specialty": "Pediatrician",
            "verified": True,
            "blockId": "block13",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 13,
                "name": "Dr. Sophia Garcia",
                "email": "dr.sophiagarcia@example.com",
            },
        },
        {
            "id": 14,
            "userId": "user111",
            "phoneNumber": "1212121212",
            "aadharNumber": "121212121212",
            "mbbsId": "MBBS111",
            "specialty": "Dermatologist",
            "verified": True,
            "blockId": "block14",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 14,
                "name": "Dr. David Anderson",
                "email": "dr.davidanderson@example.com",
            },
        },
        {
            "id": 15,
            "userId": "user112",
            "phoneNumber": "2323232323",
            "aadharNumber": "232323232323",
            "mbbsId": "MBBS112",
            "specialty": "ENT Specialist",
            "verified": True,
            "blockId": "block15",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 15,
                "name": "Dr. Olivia Wilson",
                "email": "dr.oliviawilson@example.com",
            },
        },
        {
            "id": 16,
            "userId": "user113",
            "phoneNumber": "3453453456",
            "aadharNumber": "345345345678",
            "mbbsId": "MBBS113",
            "specialty": "Orthopedic",
            "verified": True,
            "blockId": "block16",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 16,
                "name": "Dr. William Lewis",
                "email": "dr.williamlewis@example.com",
            },
        },
        {
            "id": 17,
            "userId": "user114",
            "phoneNumber": "4564564567",
            "aadharNumber": "456456456789",
            "mbbsId": "MBBS114",
            "specialty": "Gastroenterologist",
            "verified": True,
            "blockId": "block17",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 17,
                "name": "Dr. Chloe Martinez",
                "email": "dr.chloemartinez@example.com",
            },
        },
        {
            "id": 18,
            "userId": "user115",
            "phoneNumber": "5675675678",
            "aadharNumber": "567567567890",
            "mbbsId": "MBBS115",
            "specialty": "Cardiologist",
            "verified": True,
            "blockId": "block18",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 18,
                "name": "Dr. Daniel Clark",
                "email": "dr.danielclark@example.com",
            },
        },
        {
            "id": 19,
            "userId": "user116",
            "phoneNumber": "6786786789",
            "aadharNumber": "678678678901",
            "mbbsId": "MBBS116",
            "specialty": "General Physician",
            "verified": True,
            "blockId": "block19",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 19,
                "name": "Dr. Grace Adams",
                "email": "dr.graceadams@example.com",
            },
        },
        {
            "id": 20,
            "userId": "user117",
            "phoneNumber": "7897897890",
            "aadharNumber": "789789789012",
            "mbbsId": "MBBS117",
            "specialty": "Orthopedic",
            "verified": True,
            "blockId": "block20",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 20,
                "name": "Dr. Henry Morgan",
                "email": "dr.henrymorgan@example.com",
            },
        },
        {
            "id": 21,
            "userId": "user118",
            "phoneNumber": "3213213210",
            "aadharNumber": "321321321098",
            "mbbsId": "MBBS118",
            "specialty": "Pulmonologist",
            "verified": True,
            "blockId": "block21",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 21,
                "name": "Dr. Peter Walker",
                "email": "dr.peterwalker@example.com",
            },
        },
        {
            "id": 22,
            "userId": "user119",
            "phoneNumber": "4443332221",
            "aadharNumber": "444333222111",
            "mbbsId": "MBBS119",
            "specialty": "Nephrologist",
            "verified": True,
            "blockId": "block22",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 22,
                "name": "Dr. Linda Nguyen",
                "email": "dr.lindanguyen@example.com",
            },
        },
        {
            "id": 23,
            "userId": "user120",
            "phoneNumber": "5556667778",
            "aadharNumber": "555666777888",
            "mbbsId": "MBBS120",
            "specialty": "General Physician",
            "verified": True,
            "blockId": "block23",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 23,
                "name": "Dr. James Robinson",
                "email": "dr.jamesrobinson@example.com",
            },
        },
        {
            "id": 24,
            "userId": "user121",
            "phoneNumber": "8765432109",
            "aadharNumber": "876543210987",
            "mbbsId": "MBBS121",
            "specialty": "Pediatrician",
            "verified": True,
            "blockId": "block24",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 24,
                "name": "Dr. Patricia Bell",
                "email": "dr.patriciabell@example.com",
            },
        },
        {
            "id": 25,
            "userId": "user122",
            "phoneNumber": "6665554443",
            "aadharNumber": "666555444333",
            "mbbsId": "MBBS122",
            "specialty": "Dermatologist",
            "verified": True,
            "blockId": "block25",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 25,
                "name": "Dr. Christopher Lopez",
                "email": "dr.christopherlopez@example.com",
            },
        },
        {
            "id": 26,
            "userId": "user1234",
            "phoneNumber": "7654321987",
            "aadharNumber": "765432198765",
            "mbbsId": "MBBS1234",
            "specialty": "Cardiologist",
            "verified": True,
            "blockId": "block26",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 26,
                "name": "Dr. Richard Clark",
                "email": "dr.richardclark@example.com",
            },
        },
        {
            "id": 27,
            "userId": "user125",
            "phoneNumber": "3453451234",
            "aadharNumber": "345345123456",
            "mbbsId": "MBBS125",
            "specialty": "ENT Specialist",
            "verified": True,
            "blockId": "block27",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 27,
                "name": "Dr. Megan Scott",
                "email": "dr.meganscott@example.com",
            },
        },
        {
            "id": 28,
            "userId": "user126",
            "phoneNumber": "9876544321",
            "aadharNumber": "987654432198",
            "mbbsId": "MBBS126",
            "specialty": "Orthopedic",
            "verified": True,
            "blockId": "block28",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 28,
                "name": "Dr. Olivia Carter",
                "email": "dr.oliviacarter@example.com",
            },
        },
        {
            "id": 29,
            "userId": "user127",
            "phoneNumber": "1212123434",
            "aadharNumber": "121212343434",
            "mbbsId": "MBBS127",
            "specialty": "Neurosurgeon",
            "verified": True,
            "blockId": "block29",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 29,
                "name": "Dr. Henry White",
                "email": "dr.henrywhite@example.com",
            },
        },
        {
            "id": 30,
            "userId": "user128",
            "phoneNumber": "2323234545",
            "aadharNumber": "232323454545",
            "mbbsId": "MBBS128",
            "specialty": "Pediatrician",
            "verified": True,
            "blockId": "block30",
            "appointments": [],
            "Prescription": [],
            "user": {
                "id": 30,
                "name": "Dr. Emily Stewart",
                "email": "dr.emilystewart@example.com",
            },
        },
    ]


def get_doctors_by_specialty(specialty: str, doctors: List[Doctor]) -> List[Doctor]:
    specialty = specialty.lower() 
    return [doctor for doctor in doctors if specialty in doctor["specialty"].lower()]


def generate_prompt(problem: str) -> str:
    return f"""
    A patient is experiencing the following problem: {problem}
    Suggest the type of doctor they should visit and recommend some doctors by name from that specialty.
    """


def post_process(text: str):
    result = model.generate_content(
        text,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        ),
    )
    
    print(result.text)  

    
    try:
        med_data = json.loads(result.text)  
        return med_data
    except json.JSONDecodeError:
        return {"error": "Failed to parse response from the model"}, 500


def recommend_doctor(problem: str):
    doctors = fetch_doctors_from_database()
    prompt = generate_prompt(problem)

    try:
        response = post_process(prompt)
    except Exception as e:
        return {"error": str(e)}, 500

    print("Model Response:", response)  

    if "error" in response:
        return response, 500

    try:
        specialty = response.get("doctor_type")  
        doctor_names = response.get("doctors")
    except KeyError:
        return {"error": "Could not determine a suitable doctor specialty."}, 400

    print("Extracted Specialty:", specialty)  

    if not specialty or not doctor_names:
        return {"error": f"No doctors found for the specialty {specialty}"}, 404

   
    matching_doctors = get_doctors_by_specialty(specialty, doctors)
    doctor_info = {
        "doctor_type": specialty,
        "doctors": [doctor["user"]["name"] for doctor in matching_doctors]
    }

    return doctor_info



