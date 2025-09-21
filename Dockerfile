# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get -y install gcc
RUN pip install -r requirements.txt

# Copy the entire application code
COPY . .

# set environement variable for Flask CLI
ENV FLASK_APP=hello.py

# Ruen flask application on all network interfaces
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

