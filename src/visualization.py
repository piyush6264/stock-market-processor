import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data():
    try:
        df = pd.read_csv("../data/processed_stock_data.csv", index_col=0, parse_dates=True)
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df["Close"], label="Closing Price")
        plt.xlabel("Date")
        plt.ylabel("Stock Price (INR)")
        plt.title("Stock Price Over Time")
        plt.legend()
        plt.grid()
        plt.show()
    except FileNotFoundError:
        print("Processed stock data file not found!")

if __name__ == "__main__":
    plot_stock_data()
