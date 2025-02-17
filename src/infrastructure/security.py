from cryptography.fernet import Fernet
from eth_account.messages import encode_defunct
from solders.signature import Signature

class InstitutionalSecurity:
    def __init__(self, encryption_key):
        self.cipher = Fernet(encryption_key)
        
    def encrypt_config(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt_config(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()

    def verify_transaction(self, chain, tx, signature):
        if chain == 'ethereum':
            return self._verify_eth_tx(tx, signature)
        elif chain == 'solana':
            return self._verify_solana_tx(tx, signature)

    def _verify_eth_tx(self, tx, sig):
        message = encode_defunct(text=tx['message'])
        return Web3().eth.account.recover_message(message, signature=sig)

    def _verify_solana_tx(self, tx, sig):
        return Signature.from_string(sig).verify(tx['public_key'])
