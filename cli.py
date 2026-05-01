import argparse
import logging
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

# Setup logging
setup_logging()

def main():
    parser = argparse.ArgumentParser(
        description="🚀 Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP"], help="Order type")
    parser.add_argument("--qty", type=float, required=True, help="Quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT/STOP)")
    parser.add_argument("--stopPrice", type=float, help="Stop price (required for STOP)")

    args = parser.parse_args()

    try:
        # ✅ FIX 1: pass stopPrice also
        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price,
            args.stopPrice
        )

        # 🧾 Order Summary
        print("\n================ ORDER SUMMARY ================")
        print(f"Symbol      : {args.symbol}")
        print(f"Side        : {args.side}")
        print(f"Type        : {args.type}")
        print(f"Quantity    : {args.qty}")
        if args.price:
            print(f"Price       : {args.price}")
        if args.stopPrice:
            print(f"Stop Price  : {args.stopPrice}")
        print("==============================================")

        logging.info(f"Placing order: {args}")

        # 🚀 FIX 2: pass stopPrice to function
        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price,
            args.stopPrice
        )

        # 📊 Response Output
        print("\n=============== ORDER RESPONSE ===============")
        print(f"Order ID        : {order.get('orderId')}")
        print(f"Status          : {order.get('status')}")
        print(f"Executed Qty    : {order.get('executedQty')}")
        print(f"Avg Price       : {order.get('avgPrice')}")
        print("=============================================")

        print("\n✅ Order placed successfully\n")

    except ValueError as ve:
        print(f"\n⚠️ Input Error: {str(ve)}")
        logging.warning(f"Validation error: {str(ve)}")

    except Exception as e:
        print(f"\n❌ API/Error: {str(e)}")
        logging.error(f"Runtime error: {str(e)}")


if __name__ == "__main__":
    main()