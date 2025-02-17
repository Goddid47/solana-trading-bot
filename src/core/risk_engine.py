```python
class InstitutionalRiskEngine:
    def __init__(self, config):
        self.config = config
        self.open_positions = []
        
    def calculate_position_size(self, portfolio_value):
        """Dynamic position sizing based on risk rules"""
        max_risk_amount = portfolio_value * (self.config['allocation_rules']['max_portfolio_risk'] / 100)
        position_size = min(
            self.config['position_sizing']['default_amount'],
            max_risk_amount
        )
        return position_size * self.risk_adjustment_factor()
    
    def risk_adjustment_factor(self):
        """Adjust based on market volatility"""
        if self.high_volatility_conditions():
            return 0.5
        return 1.0
    
    def validate_trade(self, symbol, amount):
        """Institutional compliance checks"""
        return (
            len(self.open_positions) < self.config['position_sizing']['max_simultaneous'] and
            amount <= self.config['allocation_rules']['max_asset_allocation']
        )
