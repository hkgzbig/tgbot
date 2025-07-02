import os
import asyncio
from typing import List, Dict

from telegram import Bot
from telegram.ext import Application, CommandHandler


# Placeholder for marketplace parsing logic
async def parse_marketplace() -> List[Dict[str, str]]:
    """Parse marketplace for gift prices.

    This function should be implemented to fetch real data from the
    marketplaces. It must return a list of dictionaries with at least
    "model" and "price" keys.
    """
    # TODO: Implement real parsing logic
    return [
        {"model": "Rare Gift 1", "price": 10},
        {"model": "Common Gift", "price": 5},
    ]


async def check_prices(bot: Bot, chat_id: int, price_threshold: int):
    """Check marketplace prices and alert if a rare model is cheap."""
    items = await parse_marketplace()
    for item in items:
        if "rare" in item["model"].lower() and item["price"] <= price_threshold:
            message = (
                f"Found cheap rare model: {item['model']} for {item['price']} units"
            )
            await bot.send_message(chat_id=chat_id, text=message)


async def start(update, context):
    await update.message.reply_text("Bot is running")


async def main():
    token = os.environ.get("TG_BOT_TOKEN")
    chat_id = int(os.environ.get("TG_CHAT_ID", "0"))
    price_threshold = int(os.environ.get("PRICE_THRESHOLD", "10"))

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))

    # Periodically check prices
    async def periodic():
        while True:
            await check_prices(application.bot, chat_id, price_threshold)
            await asyncio.sleep(60)

    # Run the periodic task in the background
    application.create_task(periodic())

    # Start the bot
    await application.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
