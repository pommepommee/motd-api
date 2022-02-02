#!/bin/bash

# Docker Hub
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME"
docker build -t tgigout/motd-api
docker push tgigout/motd-api

# Gcloud
kubectl apply -f deploy.yaml