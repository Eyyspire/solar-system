#!/bin/bash

# Define the container and image names
CONTAINER_NAME="solar-system-container"
IMAGE_NAME="solar-system-image"
DOCKERFILE_PATH="."

# Function to build the Docker image
build_image() {
    echo "Building Docker image $IMAGE_NAME..."
    docker build -t "$IMAGE_NAME" "$DOCKERFILE_PATH"
}

# Check if the Docker image exists
if ! docker image ls --format '{{.Repository}}:{{.Tag}}' | grep -q "^${IMAGE_NAME}:latest$"; then
    build_image
else
    echo "Docker image $IMAGE_NAME already exists."
fi

# Check if the container already exists
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "Container $CONTAINER_NAME already exists. Removing it..."
    docker rm -f "$CONTAINER_NAME"
fi

# Run the new container
docker run -e DISPLAY="$DISPLAY" \
           -v /tmp/.X11-unix/:/tmp/.X11-unix/ \
           --name "$CONTAINER_NAME" \
           "$IMAGE_NAME"
