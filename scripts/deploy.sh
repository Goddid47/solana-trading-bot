#!/bin/bash

# Institutional Deployment Script
set -e

# Initialize HSM
if [ ! -d "/opt/hsm" ]; then
    mkdir /opt/hsm
    chmod 700 /opt/hsm
fi

# Install dependencies
apt-get update && apt-get install -y \
    docker.io \
    docker-compose \
    nginx \
    python3.10-venv \
    libpkcs11-dev  # For HSM support

# Setup Docker
systemctl enable docker
systemctl start docker

# Configure firewall
ufw allow 443/tcp
ufw allow 80/tcp
ufw enable

# Deploy containers
docker-compose -f docker-compose.prod.yml up -d --build

# Initialize database
docker exec -it bullx-core python manage.py migrate

# Setup monitoring
docker stack deploy -c monitoring/docker-compose.yml bullx-monitor

echo "✅ Institutional Deployment Complete"
