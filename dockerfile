FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory in the container
WORKDIR /src

# Install system dependencies for MySQL client and MySQL server
RUN apt-get update && apt-get install -y --no-install-recommends \
default-libmysqlclient-dev build-essential && \
rm -rf /var/lib/apt/lists/*

# Copy only requirements to leverage Docker cache
COPY requirements.txt /src/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container (only the src folder)
COPY src/ /src/

# Expose the port the app runs on (optional)
EXPOSE 8000

# Define a volume for persistent data
VOLUME /src/data

# Start MySQL service and run the application
CMD ["python", "./main.py"]