import yfinance as yf
import pandas as pd

STOCK_SYMBOL = "HDFCBANK.NS"  # Use HDFCBANK.BO for BSE

def fetch_stock_data(symbol):
    try:
        print(f"Fetching stock data for {symbol}...")
        stock = yf.Ticker(symbol)
        data = stock.history(period="1mo")  # Fetch last 1 month of data
        
        if data.empty:
            print("No data found for the given symbol.")
            return None

        # Save data to CSV
        data.to_csv(f"../data/{symbol}_stock_data.csv")
        print(f"Stock data saved to ../data/{symbol}_stock_data.csv")
        return data

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    fetch_stock_data(STOCK_SYMBOL)
