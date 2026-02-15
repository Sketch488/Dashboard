import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import yfinance as yf
import os

tickers = ["5253.T", "5032.T"]
column_names = ["ANYCOLOR Inc", "COVER Corperation"]

filepath = "StockInfo.xlsx"

data = yf.download(tickers, period= "6mo", interval="1d")
price = data['Close'].reset_index()
price.columns = ["Date"] + column_names

if os.path.exists(filepath):
    existing = pd.read_excel(filepath)
    combined = existing.set_index("Date").combine_first(price.set_index("Date")).reset_index()
 
else:
    combined = price

combined["Date"] = pd.to_datetime(combined["Date"]).dt.strftime("%Y-%m-%d")
combined.to_excel(filepath, index=False)

st.title("Stock Prediction Dashboard")

st.write(combined)
