import requests
from bs4 import BeautifulSoup
import cloudscraper

def get_hacker_news_headlines():
    url = "https://thehackernews.com/"
    
    scraper = cloudscraper.create_scraper()  # Bypasses Cloudflare
    try:
        response = scraper.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    
    for article in soup.find_all("a", class_="story-link"):
        title_tag = article.find("h2")
        if title_tag:
            headlines.append(title_tag.text.strip())
    
    return headlines

def main():
    headlines = get_hacker_news_headlines()
    if headlines:
        print("Top Headlines from The Hacker News:")
        for headline in headlines:
            print(f"- {headline}")
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
