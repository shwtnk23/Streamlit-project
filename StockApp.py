import streamlit as st
import yfinance as yf
import datetime


# dic = {"Apple": "APPL", "Microsoft": "MSFT"}

st.title("Stock Price Analyzer!")


symbol = st.text_input("Please enter the ticker", "AAPL")


col1, col2= st.columns(2)

with col1:
    start_date = st.date_input("Please enter start date", datetime.date(2023, 10, 1))
with col2:
   end_date = st.date_input("Please enter end date", datetime.date(2024, 10, 1))

ticker_data = yf.Ticker(symbol)

ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

st.write("Here is the raw day wise stock price.")
st.dataframe(ticker_df.head())

st.write("Price movement over time.")
st.line_chart(ticker_df['Close'])

st.write("Volume movement over time.")
st.line_chart(ticker_df['Volume'])