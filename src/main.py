import data_fetcher
import data_processor
import visualization

def main():
    print("Fetching stock data...")
    data_fetcher.fetch_stock_data()

    print("Processing stock data...")
    data_processor.process_stock_data()

    print("Visualizing stock data...")
    visualization.plot_stock_data()

if __name__ == "__main__":
    main()
