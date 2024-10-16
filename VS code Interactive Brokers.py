from ib_insync import *
import pandas as pd
import time

# Connect to the Interactive Brokers API
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

# Input the stock ticker code
ticker_code = input("Enter the stock ticker code (e.g., AAPL for Apple): ")

# Create a stock object
stock = Stock(ticker_code, 'SMART', 'USD')

# Request historical daily price data
try:
    # Make sure to specify the data type and duration you want
    historical_data = ib.reqHistoricalData(
        stock,
        endDateTime='',
        durationStr='1 M',  # Last 1 month
        barSizeSetting='1 day',
        whatToShow='MIDPOINT',  # You can use 'TRADES', 'BID', 'ASK', etc.
        useRTH=True,
        formatDate=1
    )

    # Convert to a DataFrame
    df = util.df(historical_data)

    # Check if DataFrame is empty
    if df is not None and not df.empty:
        # Save DataFrame to CSV
        output_file = f"{ticker_code}_historical_data.csv"
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
    else:
        print("No data retrieved. Please check your market data permissions.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    ib.disconnect()

