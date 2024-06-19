import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px


st.title('Stock Data Visualizer')
symbol = st.text_input("Enter stock symbol (e.g., BTC-USD):", 'BTC-USD')
period = st.text_input("Enter stock period (e.g., 3mo):", '3mo')

# Importing Data from Yahoo Finance API
ticker = yf.Ticker(symbol)
df = ticker.history(period)
df = df.reset_index()

st.subheader("Stock Prices Over Time")

# Create a Plotly Express line plot
fig = px.line(df, x='Date', y=["Open", "High", "Low", "Close"], labels={"variable": "Price Type"},
title="Stock Prices Over Time")
st.plotly_chart(fig)

st.subheader("Stock Candlestick Chart")

# Create a Plotly Candlestick Chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
fig.update_xaxes(rangeslider_visible=False)
fig.update_layout(title="Stock Candlestick Chart")
st.plotly_chart(fig)

st.subheader("Stock 10-day SMA vs. Close Prices")

# Calculate the 10-day SMA using Pandas
df['SMA_10'] = df['Close'].rolling(window=10).mean()

# Create a Plotly Express line plot
fig = px.line(df, x='Date', y=['SMA_10', 'Close'], labels={'variable': 'Price Type'}, title="Stock 10-day SMA vs. Close Prices")
st.plotly_chart(fig)

st.subheader("Stock 10-day SMA and EMA vs. Close Prices")

# Calculate the 10-day SMA and EMA using Pandas
df['SMA_10'] = df['Close'].rolling(window=10).mean()
df['EMA_10'] = df['Close'].ewm(span=10, adjust=False).mean()

# Create a Plotly Express line plot
fig = px.line(df, x='Date', y=['SMA_10', 'EMA_10', 'Close'], labels={'variable': 'Price Type'}, title="Stock 10-day SMA and EMA vs. Close Prices")
st.plotly_chart(fig)

st.subheader("Stock MACD and Signal Line")

# Calculate MACD and Signal Line using Pandas
df['12-day EMA'] = df['Close'].ewm(span=12, adjust=False).mean()
df['26-day EMA'] = df['Close'].ewm(span=26, adjust=False).mean()
df['MACD'] = df['12-day EMA'] - df['26-day EMA']
df['Signal Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

# Create a Plotly Express line plot
fig = px.line(df, x='Date', y=['MACD', 'Signal Line'], labels={'variable': 'Indicator'}, title="Stock MACD and Signal Line")
st.plotly_chart(fig)