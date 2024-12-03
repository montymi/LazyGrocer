# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory in the container
WORKDIR /src

# Install system dependencies for MySQL client
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy the application code to the container
COPY . /src/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (optional)
EXPOSE 8000

# Command to run the application
CMD ["python", "src/main.py"]
