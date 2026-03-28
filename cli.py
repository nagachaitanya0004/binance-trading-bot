import typer
from bot.orders import place_order, get_order_status, format_response
from bot.validators import validate_order
from bot.logging_config import setup_logger

app = typer.Typer()
logger = setup_logger()


@app.command()
def trade(
    symbol: str = typer.Argument(..., help="Trading pair (e.g., BTCUSDT)"),
    side: str = typer.Argument(..., help="BUY or SELL"),
    order_type: str = typer.Argument(..., help="MARKET, LIMIT, STOP_MARKET"),
    quantity: float = typer.Argument(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price for LIMIT/STOP orders")
):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        logger.info(
            f"Order Request: Symbol={symbol}, Side={side}, Type={order_type}, Qty={quantity}, Price={price}"
        )

        response = place_order(symbol, side, order_type, quantity, price)

        # Format response
        formatted = format_response(response)

        # Fetch latest status
        order_status = get_order_status(symbol, formatted["order_id"])

        print("\n✅ Order Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")

        print("\n📦 Response:")
        print(f"Order ID: {formatted['order_id']}")

        status = formatted["status"]
        if status == "NEW":
            print("Status: Order placed successfully (pending execution)")
        else:
            print(f"Status: {status}")

        print(f"Executed Qty: {formatted['executed_qty']}")
        print(f"Avg Price: {formatted['avg_price']}")

        print(f"\n🔄 Latest Status: {order_status['status']}")

        logger.info(f"Order Success: {formatted}")

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    app()