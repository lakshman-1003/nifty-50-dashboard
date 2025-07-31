import yfinance as yf
import pandas as pd

# Nifty 50 tickers
nifty_50 = [
    'ADANIENT.NS', 'ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS',
    'BAJFINANCE.NS', 'BAJAJFINSV.NS', 'BPCL.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS',
    'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS',
    'GRASIM.NS', 'HCLTECH.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS',
    'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'ITC.NS', 'INDUSINDBK.NS',
    'INFY.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LTIM.NS', 'LT.NS',
    'M&M.NS', 'MARUTI.NS', 'NTPC.NS', 'NESTLEIND.NS', 'ONGC.NS',
    'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SUNPHARMA.NS',
    'TCS.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TECHM.NS',
    'TITAN.NS', 'UPL.NS', 'ULTRACEMCO.NS', 'WIPRO.NS', 'HINDPETRO.NS'
]

# Download today's intraday 1-minute data
data = yf.download(tickers=nifty_50, period='1d', interval='1m', group_by='ticker', threads=True)

# Extract metrics per ticker
latest_data = []
for ticker in nifty_50:
    try:
        df = data[ticker].dropna(subset=['Open', 'Close'])
        if not df.empty:
            open_price = df.iloc[0]['Open']
            last_row = df.iloc[-1]
            close_price = last_row['Close']
            pct_change = ((close_price - open_price) / open_price) * 100

            latest_data.append({
                'symbol': ticker.replace('.NS', ''),
                'open': open_price,
                'high': last_row['High'],
                'low': last_row['Low'],
                'close': close_price,
                'volume': last_row['Volume'],
                'datetime': last_row.name,
                'pct_change': round(pct_change, 2)
            })
    except Exception as e:
        print(f"Error with {ticker}: {e}")

# Save final output
final_df = pd.DataFrame(latest_data)
final_df.to_csv("nifty_50_realtime_complete.csv", index=False)
print("✅ File saved: nifty_50_realtime_complete.csv")
