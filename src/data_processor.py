import pandas as pd

def load_stock_data():
    try:
        # Load the CSV file containing the stock data
        df = pd.read_csv("../data/HDFCBANK.NS_stock_data.csv")
        
        # If the timestamp is not the index, you can set it as the index
        # Assuming the 'timestamp' column contains date information, adjust if needed
        df.set_index("timestamp", inplace=True)
        
        # Returning the DataFrame directly
        return df
    except FileNotFoundError:
        print("Stock data file not found!")
        return None

def process_stock_data():
    # Load stock data
    stock_data = load_stock_data()
    
    # If data is not found, exit
    if stock_data is None:
        return None

    # Renaming the columns for easier processing
    df = stock_data.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })

    # Convert the index to datetime format for easier sorting and manipulation
    df.index = pd.to_datetime(df.index)
    
    # Sort the DataFrame by date in ascending order
    df = df.sort_index()

    # Save the processed data to a CSV file
    df.to_csv("../data/processed_stock_data.csv")
    print("Processed data saved to CSV!")

if __name__ == "__main__":
    # Running the processing function
    process_stock_data()

