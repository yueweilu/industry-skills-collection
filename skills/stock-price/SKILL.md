---
name: stock-price
description: Retrieve real-time stock price and market data for a given ticker symbol.
---

# Stock Price Skill

This skill allows you to fetch current stock market data using the Yahoo Finance API.

## Tools

### get_stock.py

A Python script that fetches stock data and returns it in JSON format.

**Location:** `skills/stock-price/get_stock.py`

**Dependencies:**
- `yfinance`

Install via: `pip install yfinance`

**Usage:**

```bash
python skills/stock-price/get_stock.py "Ticker Symbol"
```

**Example:**

```bash
python skills/stock-price/get_stock.py "AAPL"
```

**Output Format:**

The script returns a JSON object with:
- `symbol`: Ticker symbol
- `current_price`: Current trading price
- `currency`: Currency of the price
- `market_cap`: Market capitalization
- `volume`: Trading volume

## Acknowledgments

- Uses the [yfinance](https://github.com/ranaroussi/yfinance) library.
