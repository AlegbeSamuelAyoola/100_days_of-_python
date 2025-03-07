import requests
from bs4 import BeautifulSoup
import sqlite3
import smtplib
import os
import time
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from .env
load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# Define your products on AliExpress with sample URLs and your target prices.
PRODUCTS = [
    {
        "name": "Sample Product 1",
        "url": "https://www.aliexpress.com/item/100500XXX.html",  # Replace with a valid URL
        "target_price": 50.0  # Your target price after a 20% drop
    },
    {
        "name": "Sample Product 2",
        "url": "https://www.aliexpress.com/item/100500YYY.html",  # Replace with a valid URL
        "target_price": 100.0
    }
]

# Database file for storing product info.
DB_FILE = "prices_aliexpress.db"

def setup_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT UNIQUE,
            current_price REAL,
            target_price REAL,
            last_checked TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def scrape_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return None
    if response.status_code != 200:
        print(f"❌ Failed to retrieve {url}, status code {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    # Try to find a price element: many AliExpress pages include a span with class "price-current"
    price_tag = soup.select_one("span.price-current") or soup.select_one("span[class*='price']")
    if price_tag:
        try:
            price_str = price_tag.get_text().replace("$", "").replace(",", "").strip()
            return float(price_str)
        except Exception as e:
            print(f"❌ Error parsing price from {price_tag.get_text()}: {e}")
            return None
    else:
        print("❌ Price element not found for URL:", url)
        return None

def check_prices(test_mode=True):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for product in PRODUCTS:
        name = product["name"]
        url = product["url"]
        target_price = product["target_price"]
        # In test_mode, simulate a price drop by setting current_price to 80% of target_price.
        current_price = scrape_price(url) if not test_mode else target_price * 0.8

        if current_price is None:
            print(f"❌ Failed to retrieve price for {name}")
            continue

        print(f"🔍 {name}: Current Price = ${current_price}, Target = ${target_price}")

        cursor.execute("""
            INSERT INTO product_prices (name, url, current_price, target_price)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
                current_price=excluded.current_price,
                last_checked=CURRENT_TIMESTAMP
        """, (name, url, current_price, target_price))
        conn.commit()

        if current_price <= target_price:
            send_email(name, url, current_price)

    conn.close()

def send_email(name, url, current_price):
    subject = f"🔥 Price Drop Alert: {name} is now ${current_price}!"
    body = f"The price for {name} has dropped to ${current_price}!\nCheck it out here: {url}"
    
    # Create a MIME message with UTF-8 encoding.
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print(f"📧 Email sent: {subject}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    setup_db()
    while True:
        print("🔄 Checking product prices...")
        # Set test_mode=True to simulate a price drop (for testing); set to False in production.
        check_prices(test_mode=True)
        # Wait 24 hours (86400 seconds) before the next check.
        time.sleep(86400)
