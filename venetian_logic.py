import streamlit as st
import pandas as pd
import plotly.express as px

# --- ARCHITECTURAL HEADER ---
# SME Profile: Financial Systems & Applied Logic
# Concept: The Venetian Shadow Ledger - Exposing the fractional reserve 'Alchemy'
# Author: V. Pozza (Vitor Pozza)
# License: MIT
# Copyright (c) 2026 V. Pozza
# -----------------------------------------------------------------------------

st.set_page_config(page_title="Venetian Shadow Ledger", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #4B5563; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ The Venetian Protocol: Shadow Ledger Dashboard")
st.subheader("Exposing the Global Fractional Reserve Architecture")

# --- STEP 1: HISTORICAL CONTEXT (THE SME NARRATIVE) ---
st.info("""
    **Analytical Thesis:** This system, perfected by the Venetian 'Black Nobility', 
    institutionalized the 'Money Multiplier'. It allows a single physical asset (Gold/Land) 
    to be leveraged into a multi-layered web of systemic debt, effectively diluting the 
    sovereignty of the original holder.
""")

# --- STEP 2: USER INPUTS (THE PARAMETERS) ---
with st.sidebar:
    st.header("⚙️ System Variables")
    st.write("Adjust these to simulate different banking eras.")
    
    initial_asset = st.number_input(
        "Initial Tangible Wealth (The '1x' Base)", 
        value=100000, 
        help="The amount of physical gold or land that serves as the system's original ballast."
    )
    
    reserve_ratio_pct = st.slider(
        "Reserve Ratio (%)", 
        min_value=1.0, 
        max_value=100.0, 
        value=10.0,
        help="The 'Basel Standard' - How much the bank MUST keep. Modern banks often operate below 10%."
    )
    reserve_ratio = reserve_ratio_pct / 100
    
    cycles = st.sidebar.slider(
        "Re-circulation Cycles", 
        min_value=1, 
        max_value=20, 
        value=12,
        help="The frequency with which debt is redeposited and re-lent as 'New Money'."
    )

# --- STEP 3: THE CORE LOGIC (STEP-BY-STEP CALCULATION) ---
# Here we apply the logic: New Money = (Previous Deposit) * (1 - Reserve Ratio)
data_log = []
current_liquidity = initial_asset # The gold that starts it all
total_fiat_supply = initial_asset # Total supply starts with the asset
total_debt = 0.0

for cycle in range(1, cycles + 1):
    # STEP 3.1: The Banking Multiplier - Lending what isn't reserved
    credit_created = current_liquidity * (1 - reserve_ratio)
    
    # STEP 3.2: Accumulation - Debt injection into the economy
    total_debt += credit_created
    total_fiat_supply += credit_created
    
    # STEP 3.3: Metrics - Calculating the erosion of the physical ballast
    collateral_ratio = (initial_asset / total_fiat_supply) * 100
    
    data_log.append({
        "Cycle": cycle,
        "New_Credit_Created": round(credit_created, 2),
        "Cumulative_Money_Supply": round(total_fiat_supply, 2),
        "Asset_Dilution_Ratio_%": round(collateral_ratio, 2),
        "System_Leverage": round(total_fiat_supply / initial_asset, 2)
    })
    
    # STEP 3.4: Re-depositing - The debt returns as a 'New Deposit' for the next cycle
    current_liquidity = credit_created

df = pd.DataFrame(data_log)

# --- STEP 4: REAL-TIME METRICS (SME DASHBOARD) ---
col1, col2, col3 = st.columns(3)
col1.metric("Final System Supply", f"{df['Cumulative_Money_Supply'].iloc[-1]:,.2f}")
col2.metric("Total System Leverage", f"{df['System_Leverage'].iloc[-1]:.2f}x")
col3.metric("Final Backing Integrity", f"{df['Asset_Dilution_Ratio_%'].iloc[-1]:.2f}%")

st.divider()

# --- STEP 5: VISUAL ANALYSIS ---
left_chart, right_chart = st.columns(2)

with left_chart:
    st.write("### 📈 The Expansion of Systemic Illusion")
    fig_supply = px.line(
        df, x="Cycle", y="Cumulative_Money_Supply", 
        labels={"Cumulative_Money_Supply": "Total Fiat Supply"},
        markers=True, template="plotly_dark"
    )
    st.plotly_chart(fig_supply, use_container_width=True)

with right_chart:
    st.write("### 📉 The Erosion of Sovereignty")
    fig_dilution = px.area(
        df, x="Cycle", y="Asset_Dilution_Ratio_%", 
        labels={"Asset_Dilution_Ratio_%": "Collateral Integrity %"},
        template="plotly_dark", color_discrete_sequence=['#FF4B4B']
    )
    st.plotly_chart(fig_dilution, use_container_width=True)

# --- STEP 6: DATA EXPOSÉ ---
with st.expander("🔍 View Raw Financial Ledger (Technical Audit)"):
    st.write("This table shows exactly how each cycle dilutes the underlying asset.")
    st.dataframe(df, use_container_width=True)

st.success(f"**SME Conclusion:** By the end of {cycles} cycles, the original asset of {initial_asset:,.2f} has been leveraged {df['System_Leverage'].iloc[-1]:.1f} times. Sovereignty has effectively vanished.")

with st.sidebar:
    st.divider() 
    st.caption("© 2026 V. Pozza")
    st.caption("SME: Financial Systems & Applied Logic")