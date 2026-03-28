def validate_order(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT orders")
    
def validate_notional(price, quantity):
    if price and price * quantity < 100:
        raise ValueError("Order value must be at least 100 USDT")