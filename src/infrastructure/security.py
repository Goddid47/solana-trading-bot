from cryptography.fernet import Fernet
from eth_account.messages import encode_defunct
from web3 import Web3

class InstitutionalSecurity:
    def __init__(self, encryption_key):
        self.cipher = Fernet(encryption_key)
    
    def encrypt_config(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt_config(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()

    def verify_eth_transaction(self, tx, signature):
        message = encode_defunct(text=tx['message'])
        return Web3().eth.account.recover_message(message, signature=signature)
