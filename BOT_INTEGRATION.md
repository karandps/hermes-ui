# Bot Integration Guide

## Setting up Telegram Bot Handlers

### Option 1: Python Telegram Bot (python-telegram-bot)

```python
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from bot_handlers import handle_summarize_jll, handle_log_energy

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to Hermes Dashboard!')

def main():
    application = Application.builder().token("YOUR_BOT_TOKEN").build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("summarize_jll", handle_summarize_jll))
    application.add_handler(CommandHandler("log_energy", handle_log_energy))
    
    application.run_polling()

if __name__ == "__main__":
    main()
```

### Option 2: FastAPI Webhook

```python
from fastapi import FastAPI
from telegram import Update
import asyncio

app = FastAPI()

@app.post("/webhook/telegram")
async def telegram_webhook(update: dict):
    bot_update = Update.de_json(update)
    
    if bot_update.message and bot_update.message.text:
        text = bot_update.message.text
        
        if text == "/summarize_jll":
            from bot_handlers import fetch_jll_news
            news = fetch_jll_news()
            # Send response via bot
    
    return {"ok": True}
```

### Option 3: Direct Script Call

```bash
# Call from any script
python3 /home/karan/hermes-ui/summarize_jll.py
```

## Dashboard Data Flow

1. User clicks "Get JLL News" button
2. Dashboard sends `/summarize_jll` to Telegram bot
3. Bot calls `handle_summarize_jll()` function
4. Function fetches news, saves to `jll_news_data.json`
5. Dashboard reloads and displays new data

## Energy Logging Flow

1. User taps energy button (1-5)
2. Dashboard sends `/log_energy <level>` to bot
3. Bot calls `handle_log_energy()` function
4. Function appends to `/home/karan/bio_log.txt`

## Files to Integrate

- `bot_handlers.py` - Main command handlers
- `summarize_jll.py` - News fetching logic
- `bio_log.py` - Energy logging utility
- `jll_news_data.json` - Shared data file

## Testing

```bash
# Test news fetch
python3 summarize_jll.py

# Test energy log
python3 bio_log.py 3 "Feeling good"

# Check bio log
cat /home/karan/bio_log.txt
```
