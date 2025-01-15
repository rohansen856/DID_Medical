# Recommendation System Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /recommendation_system

# Copy the requirements file and install dependencies
COPY recommendation_system/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the code for the recommendation system
COPY recommendation_system/ .

# Command to run the AI model
CMD ["python3", "main.py"]
