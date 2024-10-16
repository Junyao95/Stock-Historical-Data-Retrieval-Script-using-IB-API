# Stock Historical Data Retrieval Script using IB API
This script retrieves historical daily price data for a specified stock using the Interactive Brokers (IB) API and saves the data to a CSV file. The script utilizes the ib_insync library to connect to the IB API, request data, and handle the connection.

## Prerequisites
1. ### Python Libraries

Before running this script, you need to install the required Python libraries:
- ib_insync
- pandas
You can install these libraries via pip:
```
bash

pip install ib_insync pandas
```
2. ### Interactive Brokers TWS/Gateway
Ensure that you have the Interactive Brokers Trader Workstation (TWS) or IB Gateway running and properly configured to allow API connections. Make sure to enable the following:
- Enable API Access in TWS or IB Gateway.
- Set the correct port (default is 7496 for TWS and 4002 for IB Gateway).
- Set a unique clientId to avoid connection conflicts.

3. ### Market Data Subscription
Ensure that your Interactive Brokers account has access to the market data for the stock you are querying. Depending on your subscription, you may need specific market data permissions (e.g., real-time data).

## How to Run the Script
1. Clone or download this repository.
2. Ensure that your IB TWS/Gateway is running and connected.
3. Open a terminal or command prompt and navigate to the directory where the script is saved.
4. Run the script using Python:
```
bash

python stock_data_retrieval.py
```
5. You will be prompted to input the stock ticker symbol. Enter a valid ticker symbol (e.g., AAPL for Apple).
6. The script will retrieve the historical data for the past month, save it to a CSV file, and display a message indicating where the file has been saved.

## Code Breakdown
- Connect to Interactive Brokers API: The script connects to the IB API using ib_insync.IB(), specifying 127.0.0.1 as the host and 7496 as the port (TWS default).
- Input Stock Ticker Code: The script prompts the user for a stock ticker symbol (e.g., AAPL).
- Stock Object Creation: The script creates a Stock object, specifying the stock's symbol, exchange (SMART), and currency (USD).
- Request Historical Data: The reqHistoricalData method requests daily price data for the past month, using the MIDPOINT as the price type. Data is returned in the form of candlesticks.
- Data Handling: The retrieved data is converted to a Pandas DataFrame, and if data is successfully retrieved, it is saved as a CSV file named <ticker_code>_historical_data.csv.
- Error Handling: The script includes a try-except block to catch and display any errors encountered during the data retrieval process.
- Disconnect: The script safely disconnects from the IB API after completion.

## Notes 
- You can modify the script to fetch other types of data by changing the whatToShow parameter. Available options include TRADES, BID, ASK, and others.
- You can adjust the data duration by modifying the durationStr parameter (e.g., '1 D' for one day, '1 W' for one week).
- Ensure you have the correct market data subscription for the stock and data type you wish to retrieve. If permissions are lacking, no data will be retrieved.

## License

[MIT](https://choosealicense.com/licenses/mit/)