import smtplib
import random
import schedule
import time
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get email credentials from environment variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# List of quotes
quotes = [
    "The only true wisdom is in knowing you know nothing. — Socrates",
    "In the midst of chaos, there is also opportunity. — Sun Tzu",
    "It is not titles that honor men, but men that honor titles. — Niccolò Machiavelli",
    "The man who moves a mountain begins by carrying away small stones. — Confucius",
    "Do, or do not. There is no try. — Yoda",
    "An unexamined life is not worth living. — Socrates",
    "With great power comes great responsibility. — Uncle Ben (Spider-Man)",
    "The more I read, the more I acquire, the more certain I am that I know nothing. — Voltaire",
    "Opportunities multiply as they are seized. — Sun Tzu",
    "All warfare is based on deception. — Sun Tzu"
]

def send_email():
    """Function to send an email with a random quote"""
    msg = EmailMessage()
    msg["Subject"] = "Your Daily Quote"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL
    msg.set_content(random.choice(quotes))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Send email immediately when the script runs
send_email()

# Schedule the job to run once a day at 8:00 AM
schedule.every().day.at("08:00").do(send_email)  

print("Scheduled task running... Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
