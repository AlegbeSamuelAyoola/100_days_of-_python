import os
import requests
from flask import Flask, render_template_string
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

app = Flask(__name__)

def get_top_news():
    """Fetch top news stories from NewsAPI"""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    return response.json().get("articles", [])[:5]  # Get top 5 articles

def extract_first_paragraph(text):
    """Extracts the first paragraph from the given text."""
    if not text:  
        return "No content available"
    
    paragraphs = text.split("\n\n")  
    return paragraphs[0] if paragraphs else "No content available"

@app.route('/news')
def news():
    articles = get_top_news()
    if not articles:
        return "Failed to fetch news", 500

    # Process the articles to extract first paragraphs
    news_list = []
    for article in articles:
        title = article.get("title", "No Title")
        content = article.get("description", "No content available")
        first_paragraph = extract_first_paragraph(content)
        image_url = article.get("urlToImage", "https://via.placeholder.com/400")  # Default placeholder image
        url = article.get("url", "#")  # News link

        news_list.append({
            "title": title,
            "summary": first_paragraph,
            "image_url": image_url,
            "url": url
        })

    # Inline HTML + CSS Template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Latest News</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 80%;
                margin: 20px auto;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            .news-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            .news-card {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease-in-out;
            }
            .news-card:hover {
                transform: translateY(-5px);
            }
            .news-card img {
                width: 100%;
                height: 200px;
                object-fit: cover;
                border-radius: 5px;
            }
            .news-card h2 {
                font-size: 18px;
                color: #333;
                margin: 15px 0;
            }
            .news-card p {
                font-size: 14px;
                color: #666;
            }
            .news-card a {
                display: inline-block;
                margin-top: 10px;
                padding: 10px 15px;
                background-color: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            .news-card a:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Latest News</h1>
            <div class="news-grid">
                {% for article in news_list %}
                <div class="news-card">
                    <img src="{{ article.image_url }}" alt="News Image">
                    <h2>{{ article.title }}</h2>
                    <p>{{ article.summary }}</p>
                    <a href="{{ article.url }}" target="_blank">Read More</a>
                </div>
                {% endfor %}
            </div>
        </div>
    </body>
    </html>
    """

    return render_template_string(html_template, news_list=news_list)

if __name__ == '__main__':
    app.run(debug=True)
