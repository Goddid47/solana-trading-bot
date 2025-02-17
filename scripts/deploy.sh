#!/bin/bash

# Institutional Deployment (No HSM)
set -e

# Install core dependencies
apt-get update && apt-get install -y \
    docker.io \
    python3.10-venv \
    nginx \
    fail2ban

# Configure firewall
ufw allow 443/tcp
ufw allow 80/tcp
ufw enable

# Deploy stack
docker-compose -f docker-compose.yml up -d --build

echo "✅ Institutional Deployment Complete"
