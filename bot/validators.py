def validate_inputs(symbol, side, order_type, quantity, price, stop_price=None):
    # Normalize inputs
    side = side.upper()
    order_type = order_type.upper()
    symbol = symbol.upper()

    # ✅ Side validation
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    # ✅ Order type validation
    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Type must be MARKET, LIMIT, or STOP")

    # ✅ Quantity validation
    if quantity is None or quantity <= 0:
        raise ValueError("Quantity must be a positive number")

    # ✅ LIMIT order validation
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        if price <= 0:
            raise ValueError("Price must be positive")

    # ✅ STOP-LIMIT validation
    if order_type == "STOP":
        if price is None or stop_price is None:
            raise ValueError("Both price and stopPrice required for STOP order")
        if price <= 0 or stop_price <= 0:
            raise ValueError("Price and stopPrice must be positive")

    # ✅ Optional: Basic symbol check
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs supported (e.g., BTCUSDT)")

    return True