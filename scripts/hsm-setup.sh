#!/bin/bash
# Institutional HSM Configuration

# 1. Install system dependencies
sudo apt-get install -y \
    libpkcs11-helper1 \
    pkcs11-helper \
    opensc \
    libengine-pkcs11-openssl

# 2. Configure PKCS#11 modules
sudo mkdir -p /etc/pkcs11/modules
echo "module: /usr/lib/opensc-pkcs11.so" | sudo tee /etc/pkcs11/modules/opensc.conf

# 3. Verify installation
pkcs11-tool --module /usr/lib/opensc-pkcs11.so -L
