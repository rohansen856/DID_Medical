# AI-Based OCR and Doctor Recommendation System

## Overview
This project consists of two primary AI-based models:
1. **OCR and Prescription Processing**: Extracts text from images of prescriptions, processes it, and recommends medicines.
2. **Doctor Recommendation System**: Suggests suitable doctors based on the patient's needs.

The project integrates image processing, generative and custom build AI models, and a database of doctors to create a seamless healthcare support tool.

## Features
- **OCR Model**: Utilizes Optical Character Recognition (OCR) technology to extract text from medical prescription images. The model accurately preprocesses and interprets handwritten and printed prescription data, making it accessible for further analysis. This ensures the system can decipher common medical abbreviations, dosage instructions, and patient-specific notes.

- **Automated Prescription Processing**: Processes the extracted text to identify and cross-reference medications. The system can extract relevant drug names, dosages, and treatment durations. Users can automatically set medication reminders based on the prescribed schedule, enhancing adherence to medical advice. This feature streamlines the process of tracking medications, reducing errors associated with manual input.

- **Medical Certificate Verification**: Provides a robust verification system for medical certificates by extracting key patient information such as name, age, and doctor’s details. The system cross-checks this information against an internal or external database to validate the authenticity of the certificate. This helps healthcare institutions or employers ensure that medical certificates presented are legitimate.


- **Doctor Recommendation System**: Leverages an AI-powered recommendation engine that suggests doctors based on user-entered medical issues and needs. By parsing through a dynamic database of doctor profiles, the system identifies doctors' specialties, matching them with patient symptoms and conditions. This personalized approach ensures that users are directed to specialists best suited for their medical needs, improving the efficiency of finding suitable healthcare providers. The recommendation engine can also filter results based on location, availability, and patient ratings to provide a comprehensive and user-friendly experience.

## Project Structure
- **`ocr.py`**: Contains the OCR logic using `pytesseract` and `PIL` for image processing.
- **`meds.py`**: Processes the extracted prescription text to identify and organize medication data.
- **`cert.py`**: Verifies the patient certificate using a generative AI model.
- **`recommend_doctor.py`**: Recommends a suitable doctor from a list of pre-populated doctor profiles based on patient needs.

## Technologies Used
- **Python** for programming.
- **Pytesseract** for OCR (Optical Character Recognition).
- **PIL (Pillow)** for image manipulation.
- **Generative AI (Gemini Model)** for processing and analyzing text data.
- **dotenv** for environment variable management.
- **Base64** for handling image data in encoded format.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ctrl-Crew/veil-py.git
   cd veil-py
   python3 -m venv venv
   source venv/bin/activate  
   # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Create a `.env` file to contain sensitive information

   ```bash
   gemini=your_gemini_api_key
   ```

3. **For starting the Recommendation model which recommends the user precautions, medications, diets, predicted disease based on the user symptoms:-**

```bash
cd veil-py
cd Recommendation_System
python3 main.py
```

## For installing with Docker for all the models:-

```bash
docker-compose build
docker-compose up
```

## CI/CD Workflow

This project is equipped with a continuous integration and continuous deployment (CI/CD) workflow using GitHub Actions. The workflow helps automate testing and deployment to ensure code quality and streamline the deployment process.

### Workflow Overview:-
- Trigger: The workflow runs on every push and pull request to the main branch.
- Build and Test: The code is checked out, Python dependencies are installed, and tests are run using pytest to verify code functionality.
- Deployment: If the tests pass, the code is deployed to the server using scp for secure file transfer and SSH for executing remote commands to restart the server.

### Benefits:-
- Automated Testing: Ensures that code changes do not break existing functionality.
- Efficient Deployment: Simplifies the process of deploying updates to the server.
- Reliability: Provides a consistent workflow that can be easily monitored and troubleshooted.


## Future Enhancements:-

- Expansion of the doctor database to include more specialties and real-time data fetching.
- Implementation of secure authentication and user management.
- Add more models as deemed necessary to automate a wode range of tasks and to provide the user a rich user experience.


## PROPER TESTING.

![PHOTO-2024-11-10-00-08-36](https://github.com/user-attachments/assets/122498f5-b9f0-4d91-9e86-6a6d255dd9d7)


![PHOTO-2024-11-09-18-14-21](https://github.com/user-attachments/assets/37d22d25-cb86-494c-8937-069bfbfa1948)

