import os
import requests
import sqlite3
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# List of interests to filter articles
INTERESTS = ["Python", "JavaScript", "Cybersecurity", "Machine Learning", "AI"]

DB_FILE = "events.db"

def setup_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id TEXT PRIMARY KEY,
            title TEXT,
            link TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    
    # Check if the 'sent' column exists, if not add it.
    cursor.execute("PRAGMA table_info(events)")
    columns = [col[1] for col in cursor.fetchall()]
    if "sent" not in columns:
        cursor.execute("ALTER TABLE events ADD COLUMN sent INTEGER DEFAULT 0")
        conn.commit()
        print("✅ Added column 'sent' to events table.")
    conn.close()

# Scrape dev.to articles using the public API
def scrape_devto():
    url = "https://dev.to/api/articles"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"per_page": 30}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"❌ Failed to retrieve data from dev.to (Status: {response.status_code})")
        return []
    
    articles = response.json()
    events = []
    print("🔍 Scraped dev.to articles:")
    for article in articles:
        title = article.get("title", "").strip()
        link = article.get("url", "")
        event_id = str(article.get("id", ""))
        print(f"- {title} ({link})")  # Debug print
        
        if any(interest.lower() in title.lower() for interest in INTERESTS):
            events.append((event_id, title, link))
    
    print(f"✅ Found {len(events)} relevant events on dev.to.")
    return events

# Check for new (or unsent) articles and send notifications
def check_and_notify():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    events = scrape_devto()
    new_events = []
    
    for event_id, title, link in events:
        cursor.execute("SELECT sent FROM events WHERE id=?", (event_id,))
        result = cursor.fetchone()
        if not result:  # New event, insert into DB
            cursor.execute("INSERT INTO events (id, title, link, sent) VALUES (?, ?, ?, ?)", (event_id, title, link, 0))
            new_events.append((event_id, title, link))
        elif result[0] == 0:  # Already exists but not sent
            new_events.append((event_id, title, link))
    
    conn.commit()
    conn.close()
    
    if new_events:
        send_email(new_events)
        mark_as_sent(new_events)
    else:
        print("📭 No new events found.")

def mark_as_sent(events):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for event_id, _, _ in events:
        cursor.execute("UPDATE events SET sent = 1 WHERE id=?", (event_id,))
    conn.commit()
    conn.close()
    print("✅ Marked events as sent in database.")

def send_email(events):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = "🚀 New dev.to Articles Matching Your Interests!"
    
    body = "Here are the new articles you might be interested in:<br><br>"
    for _, title, link in events:
        body += f"- <a href='{link}'>{title}</a><br>\n"
    
    msg.attach(MIMEText(body, "html"))
    
    try:
        print(f"📧 Sending email to {EMAIL_RECEIVER}...")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Run scraper immediately and schedule every 6 hours
setup_db()
check_and_notify()  # Immediate run
schedule.every(6).hours.do(check_and_notify)

print("🔄 dev.to Article Scraper is running...")
while True:
    schedule.run_pending()
    time.sleep(60)
