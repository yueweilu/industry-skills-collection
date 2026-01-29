import sys
import json
import yfinance as yf

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        # Using fast_info for quicker access to basic data or history for latest price
        # Note: fast_info is newer in yfinance, but history(period="1d") is very reliable
        hist = stock.history(period="1d")
        
        if hist.empty:
             return json.dumps({"error": f"No data found for symbol '{ticker}'"})
        
        current_price = hist['Close'].iloc[-1]
        info = stock.info
        
        result = {
            "symbol": ticker.upper(),
            "current_price": round(current_price, 2),
            "currency": info.get('currency', 'USD'),
            "market_cap": info.get('marketCap', 'N/A'),
            "volume": int(hist['Volume'].iloc[-1])
        }
        
        return json.dumps(result)
        
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(get_stock_price(sys.argv[1]))
    else:
        print(get_stock_price("AAPL"))
