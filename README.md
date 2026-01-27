# 🏛️ The Venetian Protocol: Shadow Ledger Dashboard

## 📊 Overview
This project is a technical exposé on the **Fractional Reserve Banking** system, modeled after the credit expansion protocols historically utilized by European banking dynasties (the 'Black Nobility').

The core objective is to demonstrate how a 10% reserve requirement (Basel Standard) acts as a money multiplier, creating systemic liquidity while simultaneously diluting the sovereignty of the underlying physical asset.

## 🌐 Live Application
You can access the real-time simulation here:  
👉 **[Venetian Shadow Ledger Dashboard](https://venetian-shadow-ledger.streamlit.app/)**

## 🛠️ Technical Stack
* **Language:** Python 3.13.1
* **Interface:** Streamlit (Cloud Deployment)
* **Analytics:** Pandas for recursive data modeling
* **Visualization:** Plotly Express for real-time leverage tracking
* **Version Control:** Git CLI (Command Line Interface)

## 🧬 Applied Financial Logic
The model follows a recursive lending cycle where:  
`New Money = (Previous Deposit) × (1 − Reserve Ratio)`

Each cycle calculates the **Asset Dilution Ratio**, showing the exact point where the system transitions from asset-backed to purely fiat-driven.

## 🚀 How to Run Locally
1. Clone the repo:  
   `git clone https://github.com/pz-computing-sme/venetian-shadow-ledger.git`
2. Install requirements:  
   `pip install -r requirements.txt`
3. Run the dashboard:  
   `streamlit run venetian_logic.py`

---
*Developed as a demonstration of Applied Logic, Financial Engineering, and Quantitative Analysis by **Vitor Pozza**.*