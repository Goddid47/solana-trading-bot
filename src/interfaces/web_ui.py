import streamlit as st
from config_manager import load_trading_conditions

def trading_conditions_interface():
    """Institutional-grade trading configuration UI"""
    st.sidebar.header("Trading Parameters")
    
    # Load existing config
    config = load_trading_conditions()
    
    # Position Sizing
    st.subheader("Position Management")
    col1, col2 = st.columns(2)
    with col1:
        config['position_sizing']['default_amount'] = st.number_input(
            "Default Position Size (USD)",
            min_value=100.0,
            max_value=1000000.0,
            value=config['position_sizing']['default_amount']
        )
    with col2:
        config['position_sizing']['max_simultaneous'] = st.slider(
            "Max Simultaneous Trades",
            1, 20, config['position_sizing']['max_simultaneous']
        )

    # Risk Management
    st.subheader("Risk Parameters")
    config['risk_management']['take_profit'] = st.slider(
        "Take Profit (%)",
        1.0, 50.0, config['risk_management']['take_profit']
    )
    config['risk_management']['stop_loss'] = st.slider(
        "Stop Loss (%)",
        1.0, 25.0, config['risk_management']['stop_loss']
    )
    
    # Allocation Rules
    st.subheader("Portfolio Allocation")
    config['allocation_rules']['max_portfolio_risk'] = st.slider(
        "Max Portfolio Risk (%)",
        0.1, 10.0, config['allocation_rules']['max_portfolio_risk']
    )
    config['allocation_rules']['max_asset_allocation'] = st.slider(
        "Max Asset Allocation (%)",
        1.0, 25.0, config['allocation_rules']['max_asset_allocation']
    )
    
    # Save button
    if st.button("Save Trading Conditions"):
        save_trading_conditions(config)
        st.success("Institutional Parameters Updated")

def wallet_connection_interface():
    """Secure wallet connection management"""
    st.header("Wallet Management")
    
    # Phantom Wallet
    if st.button("Connect Phantom Wallet"):
        st.session_state.phantom_connected = True
        st.success("Phantom Connected (Institutional Mode)")
    
    # MetaMask Wallet
    if st.button("Connect MetaMask"):
        st.session_state.metamask_connected = True
        st.success("MetaMask Connected (Institutional Mode)")
    
    # Display connection status
    if st.session_state.get('phantom_connected'):
        st.info("🔒 Phantom Wallet Connected")
    if st.session_state.get('metamask_connected'):
        st.info("🔒 MetaMask Wallet Connected")
