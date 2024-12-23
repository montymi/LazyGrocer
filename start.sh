#!/bin/bash

# Function to show usage
show_usage() {
    echo "Usage: $0 [-i]"
    echo "  -i    Run the application in interactive mode"
    exit 1
}

# Parse command-line options
INTERACTIVE_MODE=false
while getopts "i" opt; do
    case ${opt} in
        i )
            INTERACTIVE_MODE=true
            ;;
        * )
            show_usage
            ;;
    esac
done

# Stop and remove any existing containers
echo "Stopping and removing existing containers..."
docker compose down

# Build the Docker images
echo "Building Docker images..."
docker compose build | tee build.log
echo "Docker images built."

# Start up the application stack
if [ "$INTERACTIVE_MODE" = true ]; then
    echo "Starting up the application stack in interactive mode..."
    docker compose up db -d
    echo "Waiting for MySQL to start..."
    until docker exec lazygrocer-db-1 mysqladmin ping --silent; do
        sleep 1
    done
    echo "MySQL started."
    docker compose run --rm -it app
else
    echo "Starting up the application stack in detached mode..."
    docker compose up -d
    echo "Application stack started."
    echo "Waiting for MySQL to start..."
    until docker exec lazygrocer-db-1 mysqladmin ping --silent; do
        sleep 1
    done
    echo "MySQL started."
    echo "Following logs..."
    docker compose logs -f
fi