import pytest
from src.utils.config_manager import load_trading_conditions

class TestTradingConditions:
    def test_position_sizing(self):
        config = load_trading_conditions()
        assert config['position_sizing']['default_amount'] >= 100
        assert config['position_sizing']['max_simultaneous'] > 0

    def test_risk_parameters(self):
        config = load_trading_conditions()
        assert config['risk_management']['take_profit'] > config['risk_management']['stop_loss']
        assert config['allocation_rules']['max_portfolio_risk'] < 100
