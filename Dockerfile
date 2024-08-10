# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install dependencies
RUN apt update && apt install -y make xvfb

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the application using a virtual display (Xvfb)
CMD ["python", "src/main.py"]
