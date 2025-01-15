import argparse
import os
import shutil
from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings

CHROMA_PATH = "chroma"
DATA_PATH = "data"

# Sample JSON data
JSON_DATA = [{"demographics":{"_id":{"$oid":"67237fccaa12a81b3329dc04"},"bloodType":"O+","createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"dateOfBirth":{"$date":"1990-05-20T00:00:00Z"},"disabilityStatus":"None","ethnicity":"Indian","gender":"Male","language":"English","maritalStatus":"Single","occupation":"Engineer","race":"Asian","religion":"Hindu","updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"}}},{"visits":{"_id":{"$oid":"67237fccaa12a81b3329dc08"},"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"},"visits":[{"clinic":{"address":{"city":"Metropolis","country":"Countryland","postalCode":"12345","state":"MT","street":"123 Health St"},"name":"Health Clinic"},"date":{"$date":"2023-02-15T00:00:00Z"},"diagnosis":[{"condition":"Mild Hypertension","dateDiagnosed":{"$date":"2023-02-15T00:00:00Z"},"notes":"Recommended lifestyle changes","severity":"Moderate"}],"followUpDate":{"$date":"2023-08-15T00:00:00Z"},"notes":"Next visit in 6 months","reason":"Routine check-up","treatments":[{"description":"Blood pressure control","duration":"6 months","notes":"Monitor blood pressure weekly","prescribedMedication":[{"dosage":"10mg","frequency":"Once daily","name":"Lisinopril","route":"Oral"}],"type":"Medication"}],"visitId":{"$oid":"67237fccaa12a81b3329dc03"}}]}},{"insuranceInfo":{"_id":{"$oid":"67237fccaa12a81b3329dc0c"},"coverageDetails":[{"copay":20,"deductible":500,"description":"Covers hospital and physician fees","type":"Medical"}],"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"policyNumber":"H123456789","provider":"Health Insurance Co.","updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"},"validUntil":{"$date":"2024-12-31T00:00:00Z"}}},{"emergencyContacts":{"_id":{"$oid":"67237fccaa12a81b3329dc0d"},"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"emergencyContacts":[{"address":{"city":"Metropolis","country":"Countryland","postalCode":"12345","state":"MT","street":"789 Family Rd"},"notes":"Primary emergency contact","phone":"123-456-7890","relationship":"Mother"}],"updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"}}},{"medications":{"_id":{"$oid":"67237fccaa12a81b3329dc07"},"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"medications":[{"dosage":"10mg","effectiveness":"Effective","endDate":{"$date":"2023-01-10T00:00:00Z"},"frequency":"Once daily","name":"Lisinopril","notes":"Take in the morning","route":"Oral","sideEffects":["Mild dizziness"],"startDate":{"$date":"2022-01-10T00:00:00Z"}}],"updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"}}},{"immunizations":{"_id":{"$oid":"67237fccaa12a81b3329dc0b"},"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"immunizations":[{"dateAdministered":{"$date":"2023-10-01T00:00:00Z"},"doseNumber":1,"notes":"Annual flu shot","site":"Left arm","totalDoses":1,"vaccineName":"Influenza"}],"updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"}}},{"patientHistory":None},{"allergies":{"_id":{"$oid":"67237fccaa12a81b3329dc06"},"allergies":[{"diagnosedDate":{"$date":"2000-04-12T00:00:00Z"},"name":"Peanuts","notes":"Carries an epinephrine auto-injector","reaction":"Anaphylaxis","severity":"Severe"}],"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"}}},{"prescriptions":{"_id":{"$oid":"67237fccaa12a81b3329dc0a"},"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"prescriptions":[{"dosageInstructions":"Take with food","duration":"5 days","medication":{"dosage":"200mg","frequency":"As needed","name":"Ibuprofen","route":"Oral"},"notes":"For pain relief only","prescribedDate":{"$date":"2023-02-15T00:00:00Z"},"refillInfo":{"lastRefillDate":{"$date":"2023-03-01T00:00:00Z"},"nextRefillDate":{"$date":"2023-03-30T00:00:00Z"},"refillsRemaining":2}}],"updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"}}},{"medicalHistory":{"_id":{"$oid":"67237fccaa12a81b3329dc05"},"chronicDiseases":["Hypertension"],"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"familyMedicalHistory":[{"ageAtDiagnosis":50,"condition":"Diabetes","notes":"Controlled by medication","relationship":"Father"}],"hospitalizations":[{"endDate":{"$date":"2022-06-15T00:00:00Z"},"hospital":"General Hospital","notes":"Intensive care required","reason":"Severe Asthma Attack","startDate":{"$date":"2022-06-10T00:00:00Z"}}],"pastIllnesses":["Chickenpox"],"surgeries":[{"date":{"$date":"2015-03-15T00:00:00Z"},"hospital":"City Hospital","name":"Appendectomy","notes":"Routine procedure"}],"updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"}}},{"tests":{"_id":{"$oid":"67237fccaa12a81b3329dc09"},"createdAt":{"$date":"2024-10-31T13:02:04.139Z"},"tests":[{"datePerformed":{"$date":"2023-02-15T00:00:00Z"},"laboratory":{"address":{"city":"Metropolis","country":"Countryland","postalCode":"54321","state":"MT","street":"45 Lab Road"},"name":"Health Lab"},"normalRange":"4.5-11 x10^9/L","notes":"Within normal limits","result":"Normal","testName":"Complete Blood Count","units":"x10^9/L"}],"updatedAt":{"$date":"2024-10-31T13:02:04.139Z"},"userId":{"$oid":"67237fccaa12a81b3329dc02"}}}]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Load, split, and add documents to ChromaDB
    documents = load_documents()
    chunks = split_documents(documents)
    add_to_chroma(chunks)


def load_documents():
    # Load documents from structured `data` array
    documents = []
    for idx, item in enumerate(JSON_DATA):
        # Process each dictionary in `data`
        for key, content in item.items():
            doc = Document(
                page_content=str(content),  # Convert content to string
                metadata={
                    "category": key,
                    "id": f"{key}:{idx}"
                }
            )
            documents.append(doc)
    return documents

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="llama3.1")
    return embeddings

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or update documents
    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    new_chunks = [chunk for chunk in chunks_with_ids if chunk.metadata["id"] not in existing_ids]
    if new_chunks:
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
    else:
        print("✅ No new documents to add")
    print("data in database:")
    print(db.get()['documents'])

def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        category = chunk.metadata.get("category")
        current_page_id = f"{category}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id
        chunk.metadata["id"] = chunk_id

    return chunks

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

if __name__ == "__main__":
    main()