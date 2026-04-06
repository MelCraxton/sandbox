# Description: Stock market dashboard to show charts and data on a stock

import streamlit as st
import pandas as pd
import datetime

st.write("""
# Stock Market Web App
**Visually** show data on a stock!

Date range 2025–2026
""")

st.sidebar.header('User Input')

def get_input():
    start_date = st.sidebar.date_input("Start date", value = datetime.date(2025, 4, 3))
    end_date = st.sidebar.date_input("End date", value=datetime.date(2026, 4, 2))
    
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    
    return start_date, end_date, stock_symbol


def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'TSLA':
        return 'Tesla'
    elif symbol == 'GOOG':
        return 'Alphabet'
    elif symbol == 'MSFT':
        return 'Microsoft'
    elif symbol == 'AAPL':
        return 'Apple'
    elif symbol == 'SP500':
        return '^GSPC'
    else:
        return 'Unknown'  # FIXED


def get_data(symbol, start, end):
    symbol = symbol.upper()

    if symbol == 'AMZN':
        df = pd.read_csv("data/AMZN_data.csv")
    elif symbol == 'TSLA':
        df = pd.read_csv("data/TSLA_data.csv")
    elif symbol == 'GOOG':
        df = pd.read_csv("data/GOOG_data.csv")
    elif symbol == 'MSFT':
        df = pd.read_csv("data/MSFT_data.csv")
    elif symbol == 'AAPL':
        df = pd.read_csv("data/AAPL_data.csv")
    elif symbol == 'SP500':
        df = pd.read_csv("data/^GSPC_data.csv")
    else:
        return pd.DataFrame()  # FIXED

    # Convert dates (handles mixed timezone issues)
    df['Date'] = pd.to_datetime(df['Date'], utc=True)

    # Convert inputs
    start = pd.to_datetime(start, utc=True)
    end = pd.to_datetime(end, utc=True)

    # Set index and filter
    df = df.set_index('Date')
    df = df.loc[start:end]

    return df  # FIXED


# Get user input
start_date, end_date, symbol = get_input()

# Safety check
if start_date > end_date:
    st.error("Start date must be before end date.")
    st.stop()

# Load data
df = get_data(symbol, start_date, end_date)

# Safety check
if df is None or df.empty:
    st.error("No data found. Check your stock symbol or date range.")
    st.stop()

# Get company name
company_name = get_company_name(symbol.upper())

# Charts
st.header(company_name + " Close Price")
st.line_chart(df['Close'])

st.header(company_name + " Volume")
st.line_chart(df['Volume'])

# Stats
st.header('Data Stats')
st.write(df.describe())