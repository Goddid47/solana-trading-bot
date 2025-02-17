import yaml
from cryptography.fernet import Fernet
from pathlib import Path

def load_trading_conditions():
    """Load encrypted trading parameters"""
    config_path = Path(__file__).parent.parent / 'config' / 'trading_conditions.yaml.enc'
    key = os.getenv('CONFIG_KEY').encode()
    
    cipher = Fernet(key)
    with open(config_path, 'rb') as f:
        decrypted = cipher.decrypt(f.read())
    
    return yaml.safe_load(decrypted)

def save_trading_conditions(config):
    """Securely save trading parameters"""
    key = os.getenv('CONFIG_KEY').encode()
    cipher = Fernet(key)
    
    encrypted = cipher.encrypt(yaml.dump(config).encode())
    config_path = Path(__file__).parent.parent / 'config' / 'trading_conditions.yaml.enc'
    
    with open(config_path, 'wb') as f:
        f.write(encrypted)
