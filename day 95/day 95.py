from flask import Flask, render_template_string
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API Credentials
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

app = Flask(__name__)

# Initialize Spotify API
def init_spotify():
    client_credentials_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
    )
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Fetch latest global news from GNews API
def get_latest_news():
    url = f"https://gnews.io/api/v4/top-headlines?lang=en&token={GNEWS_API_KEY}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": f"GNews API Error: {response.status_code}, {response.text}"}

    news_data = response.json()
    if "articles" not in news_data or not news_data["articles"]:
        return {"error": "No articles found."}

    return news_data["articles"][:5]  # Get top 5 articles

# Extract keywords (first 3 words of the headline)
def extract_keywords(headline):
    words = headline.split()[:3]
    return " ".join(words) if words else None

# Search for a song where the title contains the keywords
def search_spotify_track(sp, query):
    if not query:
        return None

    results = sp.search(q=query, limit=10, type="track")  # Get 10 tracks

    for track in results.get("tracks", {}).get("items", []):
        song_title = track.get("name", "").lower()
        if all(word.lower() in song_title for word in query.split()):  # Ensure all words are in title
            return {
                "name": track.get("name", "Unknown Song"),
                "artist": track["artists"][0]["name"] if track.get("artists") else "Unknown Artist",
                "preview_url": track.get("preview_url", None),
            }

    return None  # No matching song found

@app.route('/')
def index():
    headlines = get_latest_news()

    if "error" in headlines:
        return render_template_string(HTML_TEMPLATE, error=headlines["error"])

    sp = init_spotify()  # Initialize Spotify client
    results = []

    for article in headlines:
        keywords = extract_keywords(article["title"])
        track_info = search_spotify_track(sp, keywords)

        results.append({
            "news": article["title"],
            "news_url": article["url"],
            "search_query": keywords,
            "song": track_info if track_info else None
        })

    return render_template_string(HTML_TEMPLATE, results=results)

# HTML Template with CSS (Embedded)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest News & Music</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: auto;
            text-align: center;
        }

        h1 {
            color: #333;
        }

        .card {
            background: white;
            padding: 15px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: left;
        }

        .card h2 a {
            text-decoration: none;
            color: #007bff;
        }

        .card h2 a:hover {
            text-decoration: underline;
        }

        p {
            color: #555;
        }

        .error {
            color: red;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📰 Latest News & 🎵 Matching Songs</h1>

        {% if error %}
            <p class="error">{{ error }}</p>
        {% else %}
            {% for item in results %}
                <div class="card">
                    <h2><a href="{{ item.news_url }}" target="_blank">{{ item.news }}</a></h2>
                    <p><strong>Search Query:</strong> {{ item.search_query }}</p>
                    
                    {% if item.song %}
                        <p><strong>🎶 Song:</strong> {{ item.song.name }} - {{ item.song.artist }}</p>
                        {% if item.song.preview_url %}
                            <audio controls>
                                <source src="{{ item.song.preview_url }}" type="audio/mpeg">
                                Your browser does not support the audio element.
                            </audio>
                        {% else %}
                            <p>No song preview available.</p>
                        {% endif %}
                    {% else %}
                        <p>No matching song found.</p>
                    {% endif %}
                </div>
            {% endfor %}
        {% endif %}
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
