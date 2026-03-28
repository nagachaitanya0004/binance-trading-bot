from bot.client import get_client

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=price,
                quantity=quantity
            )

        else:
            raise ValueError("Unsupported order type")

        return response

    except Exception as e:
        raise Exception(f"Failed to place order: {str(e)}")


def get_order_status(symbol, order_id):
    client = get_client()
    return client.futures_get_order(symbol=symbol, orderId=order_id)


def format_response(response):
    return {
        "order_id": response.get("orderId"),
        "status": response.get("status"),
        "executed_qty": response.get("executedQty"),
        "avg_price": response.get("avgPrice")
    }