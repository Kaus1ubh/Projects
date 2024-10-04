import json
import os
import random
import time
import argparse
import requests
import yfinance as yf

DATA_FILE = "holdings.json"

def fetch_price(ticker, attempts=3):
    """Retrieve stock price with retry logic."""
    for _ in range(attempts):
        try:
            stock_data = yf.Ticker(ticker)
            history = stock_data.history(period="1d")
            if not history.empty:
                return history["Close"].iloc[-1]
        except requests.exceptions.RequestException:
            time.sleep(random.uniform(1, 3))  # Randomized delay to mimic human retry behavior
    return None

def track_trends():
    """Retrieve and display trending stocks."""
    top_stocks = ["AAPL", "MSFT", "NVDA", "TSLA", "GOOGL"]
    print("\nMarket Highlights:")
    for stock in top_stocks:
        price = fetch_price(stock)
        if price:
            print(f"{stock} - ${price:.2f}")

def load_data():
    """Load portfolio from file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                pass
    return {}

def save_data(data):
    """Save portfolio data."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def modify_portfolio(stock, qty, action):
    """Add or remove stocks from holdings."""
    data = load_data()
    if action == "add":
        data[stock] = data.get(stock, 0) + qty
    elif action == "remove":
        if stock in data and data[stock] >= qty:
            data[stock] -= qty
            if data[stock] == 0:
                del data[stock]
        else:
            print("Invalid operation.")
            return
    save_data(data)
    print(f"Updated {stock}: {qty} shares {action}ed.")

def display_portfolio():
    """Show current holdings with value."""
    holdings = load_data()
    if not holdings:
        print("Portfolio is empty.")
        return
    total = 0
    for stock, qty in holdings.items():
        price = fetch_price(stock)
        if price:
            value = price * qty
            total += value
            print(f"{stock}: {qty} shares @ ${price:.2f} each = ${value:.2f}")
    print(f"Total Value: ${total:.2f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["price", "trends", "add", "remove", "view"])
    parser.add_argument("--stock", help="Stock symbol")
    parser.add_argument("--qty", type=int, help="Shares quantity")
    args = parser.parse_args()
    
    if args.command == "price" and args.stock:
        p = fetch_price(args.stock)
        if p:
            print(f"{args.stock} - ${p:.2f}")
    elif args.command == "trends":
        track_trends()
    elif args.command == "add" and args.stock and args.qty:
        modify_portfolio(args.stock, args.qty, "add")
    elif args.command == "remove" and args.stock and args.qty:
        modify_portfolio(args.stock, args.qty, "remove")
    elif args.command == "view":
        display_portfolio()
    else:
        print("Invalid command.")
