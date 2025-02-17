from web3 import Web3
from eth_account import Account

class MetaMaskConnector:
    def __init__(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.account = None
        
    def connect(self, private_key=None):
        """Connect MetaMask wallet"""
        if private_key:
            self.account = Account.from_key(private_key)
        else:
            # Simulate browser extension connection
            self.account = Account.create()
        return self.account.address

    def sign_transaction(self, tx_params):
        """Sign Ethereum transaction"""
        return self.web3.eth.account.sign_transaction(tx_params, self.account.key)
