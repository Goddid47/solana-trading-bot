from solana.rpc.commitment import Confirmed

class SolanaRPCManager:
    def __init__(self, rpc_url):
        self.client = AsyncClient(rpc_url, commitment=Confirmed)
        
    async def verify_transaction(self, tx_sig):
        """Verify Solana transaction"""
        result = await self.client.get_transaction(tx_sig)
        return result.value.transaction.meta.err is None

    async def get_balance(self, public_key):
        """Get SOL balance"""
        return await self.client.get_balance(Pubkey.from_string(public_key))
