# BullX Institutional Trading System

![Institutional Grade](https://img.shields.io/badge/Level-Institutional-blue)

## Features

- **Multi-Chain Execution**: Solana & Ethereum support
- **Risk Management Framework**:
  - Dynamic position sizing
  - Portfolio-wide risk limits
  - Blacklist monitoring
- **Institutional Security**:
  - HSM Integration
  - FIPS 140-2 compliant encryption
  - Hardware wallet support

## Trading Conditions Configuration

Edit `config/trading_conditions.yaml.enc` (encrypted):

```yaml
position_sizing:
  default_amount: 5000.0    # USD per position
  max_simultaneous: 5       # Concurrent trades

risk_management:
  take_profit: 15.0         # Target profit percentage
  stop_loss: 5.0            # Max loss percentage

allocation_rules:
  max_portfolio_risk: 2.0   # Total portfolio exposure
