import yfinance as yf

stocks = ["AAPL", "MSFT", "TSLA", "GOOG", "AMZN", "^GSPC"]

for stock in stocks:
    ticker = yf.Ticker(stock)
    df = ticker.history(period="1y")
    df.to_csv(f"data/{stock}_data.csv")
    print(df.head())
    
