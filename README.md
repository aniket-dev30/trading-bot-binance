# 🚀 Binance Futures Testnet Trading Bot

A simple Python-based CLI trading bot that places MARKET, LIMIT, and STOP orders on Binance Futures Testnet (USDT-M).

---

## 📌 Features

- Place MARKET and LIMIT orders
- Support for BUY and SELL
- Bonus: STOP (Stop-Limit) order support
- CLI-based input using argparse
- Input validation (side, type, quantity, price)
- Real-time market price validation
- Notional value validation (≥ 100 USDT)
- Logging of API requests, responses, and errors
- Fetch updated order status after execution

---

## 🛠️ Tech Stack

- Python 3.x
- python-binance
- argparse
- logging
- python-dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd trading_bot