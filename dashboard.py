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

#Company selection
select_company = st.selectbox(
    "Select a company", 
    ["ANYCOLOR Inc.", "COVER Corporation"],
    index = None,
    placeholder = "...",
    accept_new_options= True
    )

input_company = st.sidebar.text_input("Enter a company name or ticker", placeholder="...")
if input_company:
    # subprocess.run(["python", "data to excel.py", input_company])
    # subprocess.run(["python", "model.py", input_company])
    st.success(f"Data for {input_company} has been processed. Please select it from the dropdown to view the results.")

# Show dataframe
show_data = st.checkbox("Show Stock History", value=False)
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

    st.markdown("Select series to show in the chart")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        show_ANYCOLOR_close = st.checkbox("Close", value=True)
    with c2:
       show_ANYCOLOR_open = st.checkbox("Open", value=True) 
    with c3:
       show_ANYCOLOR_high = st.checkbox("High", value=True)
    with c4:
       show_ANYCOLOR_low = st.checkbox("Low", value=True)
    with c5:
        show_ANYCOLOR_volume = st.checkbox("Volume", value=False)

    ANYCOLOR_chart_data = ANYCOLOR_Prediction.copy()
    fig, ax = plt.subplots(figsize=(8, 4))

    if show_ANYCOLOR_close:
        ax.plot(ANYCOLOR_chart_data["Date"], ANYCOLOR_chart_data["Close"], color="blue", label="Close")
    if show_ANYCOLOR_open:
        ax.plot(ANYCOLOR_chart_data["Date"], ANYCOLOR_chart_data["Open"], color="orange", label="Open")
    if show_ANYCOLOR_high:
        ax.plot(ANYCOLOR_chart_data["Date"], ANYCOLOR_chart_data["High"], color="green", label="High")
    if show_ANYCOLOR_low:
        ax.plot(ANYCOLOR_chart_data["Date"], ANYCOLOR_chart_data["Low"], color="red", label="Low")
    if show_ANYCOLOR_volume:
        average_volume = ANYCOLOR_chart_data["Volume"].mean()
        ax.text(1.11, 0.5, f"Average Volume: ", transform=ax.transAxes, va = "center", ha = "center")
        ax.text(1.11, 0.42, f"{average_volume:.2f}", transform=ax.transAxes, va = "center", ha = "center")

    ax.set_ylim((ANYCOLOR_chart_data["Low"].min() - 20), (ANYCOLOR_chart_data["High"].max() + 20))
    ax.set_xlabel("Date")
    ax.set_ylabel("Close, Open, High, Low")
    ax.legend(loc = "upper left", bbox_to_anchor=(1.05, 1))
    st.pyplot(fig)

elif select_company == "COVER Corporation":
    st.subheader("COVER Corporation Stock Price Prediction In The Next 7 Days")
    st.dataframe(COVER_Prediction, height=250)

    st.markdown("Select series to show in the chart")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:    
        show_COVER_close = st.checkbox("Close", value=True)
    with c2:
        show_COVER_open = st.checkbox("Open", value=True)
    with c3:
        show_COVER_high = st.checkbox("High", value=True)
    with c4:
        show_COVER_low = st.checkbox("Low", value=True)
    with c5:
        show_COVER_volume = st.checkbox("Volume", value=False)

    COVER_chart_data = COVER_Prediction.copy()
    fig, ax = plt.subplots(figsize=(8, 4))

    if show_COVER_close:
        ax.plot(COVER_chart_data["Date"], COVER_chart_data["Close"], color="blue", label="Close")
    if show_COVER_open:
        ax.plot(COVER_chart_data["Date"], COVER_chart_data["Open"], color="orange", label="Open")
    if show_COVER_high:
        ax.plot(COVER_chart_data["Date"], COVER_chart_data["High"], color="green", label="High")
    if show_COVER_low:
        ax.plot(COVER_chart_data["Date"], COVER_chart_data["Low"], color="red", label="Low")
    if show_COVER_volume:
        average_volume = COVER_chart_data["Volume"].mean()
        ax.text(1.11, 0.5, f"Average Volume: ", transform=ax.transAxes, va = "center", ha = "center")
        ax.text(1.11, 0.42, f"{average_volume:.2f}", transform=ax.transAxes, va = "center", ha = "center")

    ax.set_ylim((COVER_chart_data["Low"].min() - 20), (COVER_chart_data["High"].max() + 20))
    ax.set_xlabel("Date")
    ax.set_ylabel("Close, Open, High, Low")
    ax.legend(loc = "upper left", bbox_to_anchor=(1.05, 1))
    st.pyplot(fig)

