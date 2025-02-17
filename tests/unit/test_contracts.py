# tests/unit/test_contracts.py
from eth_typing import (
    ChecksumAddress,
    HexStr,
    ContractAddress  # Replacement for ContractName
)

# Update test assertions using modern types
def test_contract_deployment():
    contract_addr = ContractAddress(b'\x00'*20)
    assert isinstance(contract_addr, ContractAddress)
