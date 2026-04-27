# Hermes Dashboard - JLL News Integration

## Overview
Personal dashboard with sticky daily brief, energy tracking, and social skills challenges.

## Features

### 📰 Sticky Daily Brief
- Top JLL/AI news displayed at top
- Updates once per day automatically
- Manual refresh button available
- Screenshot integration for main headline

### ⚡ Energy & Mood Tracker
- 1-5 scale buttons
- Logs to `bio_log.txt` on ThinkPad
- Timestamp each entry

### 🎯 Social Skills
- Daily challenge display
- Today: "Listen 80%, Talk 20%"

## Files

- `index.html` - Main dashboard UI
- `summarize_jll.py` - Main handler for /summarize_jll command
- `jll_handler.py` - JLL news fetching logic
- `scrape_jll_news.py` - News scraping utility
- `bio_log.py` - Energy/mood logging script
- `jll_news_data.json` - Cached news data (auto-generated)

## Usage

### Trigger News Update
```bash
python3 summarize_jll.py
```

### Log Energy Level
```bash
python3 bio_log.py 3 "Feeling good"
```

### Bot Integration
The `/summarize_jll` command triggers the news fetch and dashboard update.

## Dashboard URL
Access via Telegram Web App integration.
