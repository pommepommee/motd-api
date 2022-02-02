#!/bin/bash

# Docker Hub
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME"