import yfinance as yf
import pandas as pd

# Define NIFTY Index symbol
nifty_symbol = '^NSEI'  # Yahoo Finance symbol for NIFTY 50 index

# Define date range
start_date = "2025-01-01"
end_date = pd.Timestamp.today().strftime('%Y-%m-%d')

# Download historical daily data
data = yf.download(nifty_symbol, start=start_date, end=end_date, interval='1d')

# Reset index to get Date column
data.reset_index(inplace=True)

# Save to CSV
data.to_csv("nifty_index_2025_daily.csv", index=False)
print("✅ Nifty index data saved!")
