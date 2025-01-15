# Flask Server Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only requirements file initially for better caching
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Command to run the Flask server
CMD ["python3", "app.py"]
