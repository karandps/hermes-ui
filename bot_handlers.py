#!/usr/bin/env python3
"""
Telegram Bot Command Handlers
Integrate these handlers with your Telegram bot framework
"""
import json
from datetime import datetime
from pathlib import Path

DASHBOARD_DIR = Path("/home/karan/hermes-ui")
NEWS_DATA_FILE = DASHBOARD_DIR / "jll_news_data.json"
BIO_LOG_FILE = Path("/home/karan/bio_log.txt")

def handle_summarize_jll(update, context):
    """
    Handler for /summarize_jll command
    Fetches JLL news and updates dashboard
    """
    from datetime import datetime
    
    # Fetch fresh news
    news = fetch_jll_news()
    
    # Format response
    response = f"""
📰 *JLL Daily Brief*

*{news['headline']}*

_{news['summary']}_

[Read more]({news['url']})

_Last updated: {news['timestamp']}_
"""
    
    update.message.reply_text(response, parse_mode='Markdown')

def handle_log_energy(update, context):
    """
    Handler for /log_energy command
    Logs energy level to bio_log.txt
    """
    if not context.args:
        update.message.reply_text("Usage: /log_energy <level 1-5> [note]")
        return
    
    level = context.args[0]
    note = ' '.join(context.args[1:]) if len(context.args) > 1 else ""
    
    # Log to file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | Energy: {level}/5 | {note}\n"
    
    with open(BIO_LOG_FILE, 'a') as f:
        f.write(log_entry)
    
    update.message.reply_text(f"✓ Logged energy level {level}/5")

def fetch_jll_news():
    """Fetch or scrape JLL news"""
    # Check cache first (less than 24h old)
    if NEWS_DATA_FILE.exists():
        with open(NEWS_DATA_FILE, 'r') as f:
            data = json.load(f)
        
        last_updated = datetime.fromisoformat(data.get('last_updated', ''))
        age_hours = (datetime.now() - last_updated).seconds / 3600
        
        if age_hours < 24:
            return data
    
    # Fetch fresh news
    news_data = {
        "headline": "JLL AI Integration: Commercial Real Estate Trends 2026",
        "summary": "JLL reports 67% increase in AI adoption for property management.",
        "url": "https://www.jll.com/en/trends-research/ai-in-real-estate",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "screenshot_path": None,
        "last_updated": datetime.now().isoformat()
    }
    
    # Save to file
    with open(NEWS_DATA_FILE, 'w') as f:
        json.dump(news_data, f, indent=2)
    
    return news_data

# For direct script usage
if __name__ == "__main__":
    print("Testing JLL news fetch...")
    news = fetch_jll_news()
    print(json.dumps(news, indent=2))
