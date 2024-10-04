import argparse
import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"
MARKET_URL = "https://api.coingecko.com/api/v3/coins/markets"

def get_price(coin, currency):
    response = requests.get(API_URL, params={"ids": coin, "vs_currencies": currency})
    if response.status_code == 200:
        price = response.json().get(coin, {}).get(currency, 'N/A')
        print(f"The current price of {coin} in {currency.upper()} is: {price}")
    else:
        print("Error: Failed to fetch price")

def market_trends():
    response = requests.get(MARKET_URL, params={"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1})
    if response.status_code == 200:
        data = response.json()
        print("\nTop 10 Cryptocurrencies by Market Cap:")
        for coin in data:
            print(f"{coin['name']} ({coin['symbol'].upper()}): ${coin['current_price']}")
    else:
        print("Error: Failed to fetch market trends")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Crypto Tracker using CoinGecko API")
    parser.add_argument("command", choices=["price", "trends"], help="Choose a command: price or trends")
    parser.add_argument("--coin", default="bitcoin", help="Cryptocurrency symbol (default: bitcoin)")
    parser.add_argument("--currency", default="usd", help="Currency to convert to (default: USD)")

    args = parser.parse_args()

    if args.command == "price":
        get_price(args.coin, args.currency)
    elif args.command == "trends":
        market_trends()
