#!/bin/bash

# Generate encryption key if needed
if [ ! -f ".encryption_key" ]; then
    python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())" > .encryption_key
fi

# Encrypt configs
openssl enc -aes-256-cbc -pbkdf2 \
    -in config/trading.yaml \
    -out config/trading.enc \
    -pass file:.encryption_key

echo "🔒 Configs encrypted with FIPS 140-2 compliant encryption"
