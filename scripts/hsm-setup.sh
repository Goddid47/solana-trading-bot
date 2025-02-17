#!/bin/bash
# scripts/hsm-setup.sh

# Install PKCS#11 libraries
wget https://github.com/OpenSC/libp11/releases/download/libp11-0.5.0/libp11-0.5.0.tar.gz
tar xvf libp11-0.5.0.tar.gz
cd libp11-0.5.0 && ./configure && make && sudo make install

# Configure HSM module
sudo mkdir -p /opt/hsm/config
sudo chmod 700 /opt/hsm
