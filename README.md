# 🚀 Binance Futures Testnet Trading Bot

A modular, CLI-based Python trading bot that interacts with Binance Futures Testnet (USDT-M).
It supports MARKET, LIMIT, and STOP (Stop-Limit) orders with proper validation, logging, and clean architecture.

---

## 📌 Features

* Place MARKET, LIMIT, and STOP orders
* Supports BUY and SELL
* CLI-based interaction using argparse
* Input validation (side, type, quantity, price)
* Real-time market price validation
* Minimum notional validation (≥ 100 USDT)
* Logging of API requests, responses, and errors
* Fetch updated order status after execution
* Clean modular structure (client, orders, validators)

---

## 🛠️ Tech Stack

* Python 3.x
* python-binance
* argparse
* logging
* python-dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/aniket-dev30/trading-bot-binance.git

cd trading-bot-binance

---

### 2. Create Virtual Environment (Recommended)

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Setup Environment Variables

Create a `.env` file in the root directory:

API_KEY=your_api_key
API_SECRET=your_api_secret

Get your credentials from:
https://testnet.binancefuture.com

⚠️ Never commit your `.env` file to GitHub.

---

## ▶️ Usage

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002

---

### LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.002 --price 80000

---

### STOP (Stop-Limit) Order

python cli.py --symbol BTCUSDT --side SELL --type STOP --qty 0.002 --price 74000 --stopPrice 75000

---

## 📊 Example Output

```
================ ORDER SUMMARY ================
Symbol      : BTCUSDT
Side        : BUY
Type        : MARKET
Quantity    : 0.002
==============================================

📊 Current Market Price: 77950.0

=============== ORDER RESPONSE ===============
Order ID        : 12345678
Status          : FILLED
Executed Qty    : 0.002
Avg Price       : 77950.0
=============================================

✅ Order placed successfully
```

## 📁 Project Structure

trading_bot/
│
├── bot/
│   ├── client.py        # Binance API client
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   └── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
└── bot.log              # Logs

---

## 📝 Logging

All API requests, responses, and errors are stored in:

bot.log

---

## ⚠️ Assumptions

* Only USDT trading pairs supported (e.g., BTCUSDT)
* Minimum order value must be ≥ 100 USDT
* STOP orders use basic trigger logic

---

## 🤝 Contribution Guidelines

1. Fork the repository

2. Create a feature branch:
   git checkout -b feature/your-feature-name

3. Commit your changes:
   git commit -m "Add new feature"

4. Push your branch:
   git push origin feature/your-feature-name

5. Open a Pull Request

---

## 🧪 Testing

Use Binance Futures Testnet only.
Do not use real API keys.

---

## 🚀 Future Improvements

* Add OCO / Trailing Stop orders
* Add interactive CLI (Click / Typer)
* Add web dashboard (React + FastAPI)
* Add automated trading strategies
* Add unit testing

---

## 🔒 Security Notes

* Never expose API keys publicly
* Always use `.env` for secrets
* Add `.env` to `.gitignore`

---

## 👤 Author

Developed as part of a Python Developer assignment.
Focused on clean architecture, validation, and real-world trading constraints.

---

## ⭐ If you found this useful

Give it a star on GitHub!
