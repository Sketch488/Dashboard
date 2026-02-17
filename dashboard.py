from turtle import width
import streamlit as st
import subprocess
import pandas as pd
from numpy.random import default_rng

subprocess.run(["python", "data to excel.py"])
# subprocess.run(["python", "prediction.py"])
# subprocess.run(["python", "results to excel.py"])
# subprocess.run(["python", ".py"])

Anycolor_data = pd.read_excel("ANYCOLOR Inc.xlsx")
Cover_data = pd.read_excel("COVER Corporation.xlsx")

st.title("Stock Prediction Dashboard")

select_company = st.selectbox(
    "Select a company", ["ANYCOLOR Inc.", "COVER Corporation"]
    )
if select_company == "ANYCOLOR Inc.":
    st.subheader("ANYCOLOR Inc. Stock Data")
    st.dataframe(Anycolor_data)
elif select_company == "COVER Corporation":
    st.subheader("COVER Corporation Stock Data")
    st.dataframe(Cover_data)

uploaded_file = st.sidebar.file_uploader(
    "Upload a file", accept_multiple_files=True, type=["xlsx", "csv"])
if uploaded_file is not None:
    st.stop()
       