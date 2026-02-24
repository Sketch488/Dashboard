import pandas as pd
import streamlit as st
import yfinance as yf

st.title("Sketch's Stock Prediction Model", text_alignment="center")
st.subheader("Made By Sewruttan Shared", text_alignment="center")

ticker = st.text_input(
    "Enter A Company Ticker",
    placeholder="Enter Here...",
)

if "is_valid_ticker" not in st.session_state:
    st.session_state.is_valid_ticker = False
if "validated_ticker" not in st.session_state:
    st.session_state.validated_symbol = ""

symbol = ticker.strip().upper()

if symbol != st.session_state.validated_symbol:
    st.session_state.is_valid_ticker = False

PERIOD_UNIT_MAP = {
    "Days": "d",
    "Months": "mo",
    "Years": "y",
    "Year to Date": "ytd",
    "Max": "max",
}

INTERVAL_UNIT_MAP = {
    "Days": "d",
    "Weeks": "wk",
    "Months": "mo",
}

# Date and Interval periods
t1, t2= st.columns(2)
with t1:
    st.markdown("Date Period", help = "How much data you want")
    p_left, p_right = st.columns([1, 1])
    with p_left:
        period_value = st.number_input("Value", min_value=1, value=1, step=1, key="period_value")
    with p_right:
        period_unit_label = st.selectbox(
            "Unit",
            list(PERIOD_UNIT_MAP.keys()),
            key="period_unit",
        )
        period_unit = PERIOD_UNIT_MAP[period_unit_label]

    if period_unit in ["ytd", "max"]:
        period = period_unit
    else:
        period = f"{int(period_value)}{period_unit}"

with t2:
    st.markdown("Interval", help = "Time between each data point")
    i_left, i_right = st.columns([1, 1])
    with i_left:
        interval_value = st.number_input("Value", min_value=1, value=1, step=1, key="interval_value")
    with i_right:
        interval_unit_label = st.selectbox(
            "Unit ",
            list(INTERVAL_UNIT_MAP.keys()),
            key="interval_unit",
        )
        interval_unit = INTERVAL_UNIT_MAP[interval_unit_label]

    interval = f"{int(interval_value)}{interval_unit}"

search_button = st.button("Search")
if search_button:
    if not symbol:
        st.warning("Enter a company name or ticker.")
        st.session_state.is_valid_ticker = False
        st.stop()

    data = yf.download(symbol, period=period, interval=interval, progress=False)

    if data.empty:
        st.error(f"No data found for '{symbol}'.")
        st.session_state.is_valid_ticker = False
    else:
        st.session_state.is_valid_ticker = True
        st.session_state.validated_symbol = symbol
        display_df = data.reset_index().copy()

        if isinstance(display_df.columns, pd.MultiIndex):
            flat_columns = []
            for col in display_df.columns.to_flat_index():
                chosen = next((part for part in col if part not in ("", None)), col[0])
                flat_columns.append(str(chosen))
            display_df.columns = flat_columns
            display_df = display_df.loc[:, ~display_df.columns.duplicated()].copy()

        for col in ["Open", "High", "Low", "Close", "Volume"]:
            if col in display_df.columns:
                display_df[col] = pd.to_numeric(display_df[col], errors="coerce").round(0).astype("Int64")

        date_col = "Date" if "Date" in display_df.columns else "Datetime"
        if date_col in display_df.columns:
            display_df[date_col] = pd.to_datetime(display_df[date_col], errors="coerce")
            display_df = display_df.sort_values(by=date_col, ascending=False).reset_index(drop=True)
            display_df[date_col] = display_df[date_col].dt.strftime("%Y-%m-%d")

        st.dataframe(display_df, height=250)

        csv_data = display_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download File",
            data=csv_data,
            file_name=f"{symbol}_{period}_{interval}.csv",
            mime="text/csv",
        )
else:
    st.info("Enter inputs and click Search")

#Prediction
if st.session_state.is_valid_ticker:

    st.header("Prediction Section")

    st.markdown("Prediction Period", help = "How many days to predict")
    prediction_value = st.number_input()

    predict_button = st.button("Predict")
    if predict_button:
        st.write("Prediction innit")