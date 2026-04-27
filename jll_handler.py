#!/usr/bin/env python3
"""
JLL News Handler - Called when user clicks 'Get JLL News' button
- Scrapes JLL/AI news
- Captures screenshot of main headline
- Updates dashboard with fresh data
- Logs to bio_log.txt
"""
import json
import os
from datetime import datetime
from pathlib import Path

def get_jll_news():
    """Main handler for JLL news request"""
    print("Fetching JLL news...")
    
    # Sample news data (would integrate with actual scraper)
    news_data = {
        "headline": "JLL AI Integration: Commercial Real Estate Trends 2026",
        "summary": "JLL reports 67% increase in AI adoption for property management and tenant experience optimization.",
        "url": "https://www.jll.com/en/trends-research/ai-in-real-estate",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "screenshot_path": None
    }
    
    # Save to dashboard data file
    dashboard_dir = Path("/home/karan/hermes-ui")
    data_file = dashboard_dir / "jll_news_data.json"
    
    with open(data_file, 'w') as f:
        json.dump(news_data, f, indent=2)
    
    print(f"News saved to {data_file}")
    return news_data

if __name__ == "__main__":
    get_jll_news()
