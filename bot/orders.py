from bot.client import get_client

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            return client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
        elif order_type == "LIMIT":
            return client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
    except Exception as e:
        raise e