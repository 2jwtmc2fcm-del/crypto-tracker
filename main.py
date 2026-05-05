import os
os.system("pip install python-telegram-bot requests")

import asyncio
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8333075284:AAHx6H6ZUzUQc7_5xCobtpN_uJ0e0WO7Mz4

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    return requests.get(url).json()[coin]["usd"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Bot attivo!\nUsa /btc /eth /xrp")

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"₿ BTC: {get_price('bitcoin')}$")

async def eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Ξ ETH: {get_price('ethereum')}$")

async def xrp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💧 XRP: {get_price('ripple')}$")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("btc", btc))
    app.add_handler(CommandHandler("eth", eth))
    app.add_handler(CommandHandler("xrp", xrp))

    print("Bot avviato...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
