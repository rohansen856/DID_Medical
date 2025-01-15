import json
import os
from enum import Enum

import google.generativeai as genai
import typing_extensions as typing
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("gemini"))

model = genai.GenerativeModel("gemini-1.5-flash")

class Cert(typing.TypedDict):
    name: str
    dob: str
    reg_no: int

def post_process_cert(text: str) -> Cert:
    result = model.generate_content(
    ["I'll give you an OCR of a certificate, your return json schema will be used to verify with usual input data",text],
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=Cert
    ),)

    print(result.text)
    cert_data = json.loads(result.text)
    
    return cert_data