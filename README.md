# Stock Data Visualizer

This is a simple Streamlit web application that allows users to visualize stock data using the Yahoo Finance API and Plotly graphs.

## Description

This application fetches stock data based on the user-provided stock symbol and period. It provides several visualizations to analyze the stock prices and indicators.

## Installation

1. Make sure you have Python installed.
2. Clone this repository:

    ```bash
    git clone https://github.com/your-username/stock-data-visualizer.git
    ```

3. Navigate to the project directory and install the required dependencies:

    ```bash
    cd stock-data-visualizer
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the application.

## Features

- **Stock Prices Over Time**: Visualizes the stock prices over time using a line plot.
- **Stock Candlestick Chart**: Displays the stock data using a candlestick chart.
- **Stock 10-day SMA vs. Close Prices**: Compares the 10-day Simple Moving Average (SMA) with the Close prices.
- **Stock 10-day SMA and EMA vs. Close Prices**: Compares the 10-day SMA and Exponential Moving Average (EMA) with the Close prices.
- **Stock MACD and Signal Line**: Displays the Moving Average Convergence Divergence (MACD) and Signal Line.

## Technologies Used

- Streamlit
- yfinance
- Plotly

## Credits

This application uses the following libraries:
- [Streamlit](https://streamlit.io/)
- [yfinance](https://pypi.org/project/yfinance/)
- [Plotly](https://plotly.com/)

## Webapp

[stockvisualizer](https://stockvisualizer.streamlit.app/)
