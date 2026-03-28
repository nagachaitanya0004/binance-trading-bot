from bot.config import MIN_NOTIONAL

def validate_order(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side. Use BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        raise ValueError("Invalid order type. Use MARKET, LIMIT, or STOP_MARKET")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type in ["LIMIT", "STOP_MARKET"] and price is None:
        raise ValueError("Price is required for LIMIT and STOP_MARKET orders")

    # Call notional validation
    validate_notional(price, quantity, order_type)


def validate_notional(price, quantity, order_type):
    # Only validate when price is available
    if price is not None:
        if price * quantity < MIN_NOTIONAL:
            raise ValueError(
                f"Order value must be at least {MIN_NOTIONAL} USDT"
            )