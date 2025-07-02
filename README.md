# Telegram Gift Marketplace Bot

This simple Telegram bot periodically checks gift marketplaces and alerts when a rare model is listed below a configured price threshold.

## Configuration

Set the following environment variables before running the bot:

- `TG_BOT_TOKEN` – token for the Telegram bot.
- `TG_CHAT_ID` – chat ID where alerts will be sent.
- `PRICE_THRESHOLD` – numeric threshold; rare models priced below this will trigger an alert. Default is `10`.

## Running

Install dependencies and run the bot:

```bash
pip install python-telegram-bot
python main.py
```

The parsing logic is located in `parse_marketplace()` inside `main.py` and must be implemented to fetch real data from the chosen marketplaces.
