import yfinance as yf
import pandas as pd
import numpy as np


def get_market_data(ticker, period="1d", interval="1m"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist


def execute_trade(symbol, action, quantity, price):
    order_id = np.random.randint(100000, 999999)
    return {
        "Order ID": order_id,
        "Symbol": symbol,
        "Action": action,
        "Quantity": quantity,
        "Price": price,
        "Status": "Executed",
    }


def check_risk_and_compliance(order):
    risk_threshold = 100000
    order_value = order["Quantity"] * order["Price"]
    if order_value > risk_threshold:
        return False, "Order exceeds risk threshold"
    return True, "Order within risk threshold"


def generate_report(orders):
    df = pd.DataFrame(orders)
    report = (
        df.groupby("Symbol")
        .agg({"Quantity": "sum", "Price": "mean", "Status": "count"})
        .rename(columns={"Status": "Trades Executed"})
    )
    return report


def automated_trading_system(
    ticker, action, quantity, price, period="1d", interval="1m"
):

    market_data = get_market_data(ticker, period, interval)
    print("Market Data Retrieved:\n", market_data)

    order = execute_trade(ticker, action, quantity, price)
    print("Trade Executed:\n", order)

    risk_status, risk_message = check_risk_and_compliance(order)
    if not risk_status:
        print("Risk Check Failed:", risk_message)
        return

    report = generate_report([order])
    print("Performance Report:\n", report)


automated_trading_system("AAPL", "Buy", 100, 150.25)
