import pytest
from solders.keypair import Keypair
from src.core.main import BullXTradingBot

class TestSolanaIntegration:
    @pytest.fixture
    def bot(self):
        return BullXTradingBot()

    def test_solana_trade_execution(self, bot):
        test_tx = {
            'receiver': Keypair().pubkey(),
            'amount': 1000000  # 1 SOL in lamports
        }
        
        result = asyncio.run(bot.execute_trade('solana', test_tx))
        assert result.value.error is None
        assert len(result.value.transaction.signatures) == 1
