import logging
import time
from bot.client import get_client

client = get_client()


def get_current_price(symbol):
    ticker = client.futures_symbol_ticker(symbol=symbol)
    return float(ticker["price"])


def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        current_price = get_current_price(symbol)
        print(f"\n📊 Current Market Price: {current_price}")

        # Normalize inputs
        side = side.upper()
        order_type = order_type.upper()

        # ✅ LIMIT validation
        if order_type == "LIMIT":
            if side == "BUY" and price > current_price:
                raise ValueError("BUY LIMIT price must be ≤ market price")
            if side == "SELL" and price < current_price:
                raise ValueError("SELL LIMIT price must be ≥ market price")

        # ✅ STOP validation
        if order_type == "STOP":
            if side == "BUY" and stop_price < current_price:
                raise ValueError("BUY STOP trigger must be ≥ market price")
            if side == "SELL" and stop_price > current_price:
                raise ValueError("SELL STOP trigger must be ≤ market price")

        # ✅ NOTIONAL CHECK
        effective_price = price if price else current_price
        notional = quantity * effective_price

        if notional < 100:
            raise ValueError(
                f"Order notional must be ≥ 100 USDT. Current: {round(notional, 2)}"
            )

        logging.info(
            f"Placing {order_type} order | {side} | {symbol} | qty={quantity} | price={price} | stop={stop_price}"
        )

        # 🚀 Place order
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

        # ✅ NEW PART: Fetch updated order status
        time.sleep(1)  # wait a bit for execution update

        updated_order = client.futures_get_order(
            symbol=symbol,
            orderId=order["orderId"]
        )

        print("\n📊 UPDATED STATUS:")
        print(f"Status          : {updated_order.get('status')}")
        print(f"Executed Qty    : {updated_order.get('executedQty')}")
        print(f"Avg Price       : {updated_order.get('avgPrice')}")

        logging.info(f"Order Response: {updated_order}")
        return updated_order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise