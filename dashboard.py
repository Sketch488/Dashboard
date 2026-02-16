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

ANYCOLOR, COVER = st.columns(2)

with ANYCOLOR:
    if st.button("ANYCOLOR Inc."):
        st.write("ANYCOLOR Inc:", Anycolor_data)

with COVER:
    if st.button("COVER Corporation"):
       st.write("COVER Corporation:", Cover_data)