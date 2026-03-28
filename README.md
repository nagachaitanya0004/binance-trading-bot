# 🚀 Binance Futures Testnet Trading Bot (Python)

## 📌 Overview

This project is a simplified trading bot built using Python that interacts with the Binance Futures Testnet (USDT-M). It allows users to place MARKET and LIMIT orders via a command-line interface (CLI) with proper validation, logging, and error handling.

The goal of this project is to demonstrate clean code structure, API integration, and basic trading system design.

---

## ⚙️ Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* CLI-based user input using `Typer`
* Input validation and error handling
* Structured project architecture (modular design)
* Logging of requests, responses, and errors
* Secure API key management using `.env`

---

## 🧱 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client setup
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── .env                   # API credentials (not shared)
├── requirements.txt
└── logs/
    └── bot.log            # Log file
```

---

## 🔑 Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

---

## 🌐 Binance Testnet Setup

1. Visit: https://testnet.binancefuture.com
2. Login and generate API keys
3. Add keys to `.env` file

---

## ▶️ Usage

### 🔹 Place a MARKET Order

```
python3 cli.py BTCUSDT BUY MARKET 0.002
```

### 🔹 Place a LIMIT Order

```
python3 cli.py BTCUSDT SELL LIMIT 0.002 --price 70000
```

---

## 📦 Output Example

* Order Summary (symbol, side, type, quantity)
* Order Response (orderId, status, executedQty, avgPrice)
* Success or error messages

---

## 📝 Logging

* Logs are stored in:

```
logs/bot.log
```

* Includes:

  * API requests
  * API responses
  * Errors

---

## ⚠️ Notes / Assumptions

* Binance Futures requires a **minimum notional value of 100 USDT** per order
* MARKET orders on testnet may show `NEW` status initially due to simulated liquidity
* API keys must be valid and testnet-enabled

---

## 📌 Requirements

* Python 3.x
* python-binance
* typer
* loguru
* python-dotenv

---

## 💡 Future Improvements

* Add Stop-Loss / Stop-Market orders
* Improve CLI UX with prompts
* Add real-time order tracking
* Build a simple UI dashboard

---

## 🙌 Conclusion

This project demonstrates the ability to build a clean, modular Python application with real-world API integration, proper logging, and user input handling.

---
