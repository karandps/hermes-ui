#!/usr/bin/env python3
"""
Bio Log Handler - Logs energy and mood data to bio_log.txt
Called from dashboard when user taps 1-5 buttons
"""
import os
from datetime import datetime
from pathlib import Path

def log_bio_data(energy_level, mood_note=""):
    """
    Log energy/mood data to bio_log.txt
    energy_level: 1-5 integer
    mood_note: optional text note
    """
    log_file = Path("/home/karan/bio_log.txt")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | Energy: {energy_level}/5 | {mood_note}\n"
    
    # Append to log file
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    print(f"Logged: Energy {energy_level}/5 at {timestamp}")
    return {"status": "success", "entry": log_entry.strip()}

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        level = int(sys.argv[1])
        note = sys.argv[2] if len(sys.argv) > 2 else ""
        log_bio_data(level, note)
    else:
        print("Usage: python bio_log.py <energy_level 1-5> [mood_note]")
