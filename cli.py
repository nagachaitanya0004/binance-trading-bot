import typer
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

app = typer.Typer()
logger = setup_logger()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        logger.info(f"Placing order: {symbol} {side} {order_type}")

        response = place_order(symbol, side, order_type, quantity, price)

        print("\n✅ Order Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")

        print("\n📦 Response:")
        print(f"Order ID: {response.get('orderId')}")
        status = response.get("status")
        if status == "NEW":
            print("Status: Order placed successfully (pending execution)")
        else:
            print(f"Status: {status}")

        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

        logger.info(f"Order Success: {response}")

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    app()