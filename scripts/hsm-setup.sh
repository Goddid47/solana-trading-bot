#!/bin/bash
# Install PKCS#11 base libraries
wget https://github.com/OpenSC/OpenSC/releases/download/0.24.0/opensc-0.24.0.tar.gz
tar xvf opensc-*.tar.gz
cd opensc-0.24.0 && ./bootstrap && ./configure && make && sudo make install

# Configure HSM
sudo ldconfig
sudo mkdir -p /opt/hsm/{config,certs}
sudo chmod 700 -R /opt/hsm
