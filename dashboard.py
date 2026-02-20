import streamlit as st
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# subprocess.run(["python", "data to excel.py"])
# subprocess.run(["python", "prediction.py"])
# subprocess.run(["python", "results to excel.py"])
# subprocess.run(["python", ".py"])

ANYCOLOR_data = pd.read_excel("ANYCOLOR Inc.xlsx")
ANYCOLOR_Prediction = pd.read_excel("ANYCOLOR Inc_next_7_days.xlsx")

COVER_data = pd.read_excel("COVER Corporation.xlsx")
COVER_Prediction = pd.read_excel("COVER Corporation_next_7_days.xlsx")

st.title("Stock Prediction Dashboard")

select_company = st.selectbox(
    "Select a company", 
    ["ANYCOLOR Inc.", "COVER Corporation"],
    index = None,
    placeholder = "Choose a company",
    )

show_data = st.checkbox("Show Stock Data", value=False)
if show_data:
    if select_company == "ANYCOLOR Inc.":
        st.subheader("ANYCOLOR Inc. Stock Data")
        st.dataframe(ANYCOLOR_data, height=250)

    elif select_company == "COVER Corporation":
        st.subheader("COVER Corporation Stock Data")    
        st.dataframe(COVER_data, height=250)


if select_company == "ANYCOLOR Inc.":
    st.subheader("ANYCOLOR Inc. Stock Price Prediction In The Next 7 Days", )
    st.dataframe(ANYCOLOR_Prediction, height=250)

    ANYCOLOR_chart_data = ANYCOLOR_Prediction.copy()
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(ANYCOLOR_chart_data["Date"], ANYCOLOR_chart_data["Close"], color="blue", label="Close")
    ax.plot(ANYCOLOR_chart_data["Date"], ANYCOLOR_chart_data["Open"], color="orange", label="Open")
    ax.plot(ANYCOLOR_chart_data["Date"], ANYCOLOR_chart_data["High"], color="green", label="High")
    ax.plot(ANYCOLOR_chart_data["Date"], ANYCOLOR_chart_data["Low"], color="red", label="Low")

    ax.set_ylim((ANYCOLOR_chart_data["Close"].min() - 150), (ANYCOLOR_chart_data["Close"].max() + 150))
    ax.set_xlabel("Date")
    ax.set_ylabel("Close, Open, High, Low")
    ax.legend(loc = "upper left", bbox_to_anchor=(1.05, 1))
    st.pyplot(fig)

elif select_company == "COVER Corporation":
    st.subheader("COVER Corporation Stock Price Prediction In The Next 7 Days")
    st.dataframe(COVER_Prediction, height=250)

    COVER_chart_data = COVER_Prediction.copy()
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(COVER_chart_data["Date"], COVER_chart_data["Close"], color="blue", label="Close")
    ax.plot(COVER_chart_data["Date"], COVER_chart_data["Open"], color="orange", label="Open")
    ax.plot(COVER_chart_data["Date"], COVER_chart_data["High"], color="green", label="High")
    ax.plot(COVER_chart_data["Date"], COVER_chart_data["Low"], color="red", label="Low")

    ax.set_ylim((COVER_chart_data["Close"].min() - 50), (COVER_chart_data["Close"].max() + 50))
    ax.set_xlabel("Date")
    ax.set_ylabel("Close, Open, High, Low")
    ax.legend(loc = "upper left", bbox_to_anchor=(1.05, 1))
    st.pyplot(fig)
