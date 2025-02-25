from flask import Flask, render_template_string
import requests
from datetime import datetime

app = Flask(__name__)

LATITUDE = '6.6156'
LONGITUDE = '3.3334'
LOCATION_NAME = 'Lagos, Nigeria'

HTML_TEMPLATE = """"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🌡️ Weather Forecast - {{ location }}</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        .forecast { margin-top: 20px; font-size: 1.2em; }
        table { margin: 0 auto; border-collapse: collapse; }
        th, td { padding: 10px; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <h1>🌍 Weather Forecast for {{ location }}</h1>
    <p class="forecast">Current Temperature: <strong>{{ current_temp }}°C 🌡️</strong></p>
    <h2>Next Hours Forecast</h2>
    <table>
        <tr>
            <th>Time (UTC)</th>
            <th>Temperature (°C)</th>
        </tr>
        {% for time, temp in forecast %}
        <tr>
            <td>{{ time }}</td>
            <td>{{ temp }}°C</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def weather_forecast():
    url = (
        f'https://api.open-meteo.com/v1/forecast'
        f'?latitude={LATITUDE}&longitude={LONGITUDE}&hourly=temperature_2m'
    )
    response = requests.get(url)
    data = response.json()

    # Handle errors
    if response.status_code != 200 or 'hourly' not in data:
        return f"API Error: {response.status_code}, {data.get('reason', 'No details available')}"

    # Extract temperature and time data
    temperatures = data['hourly']['temperature_2m']
    times = data['hourly']['time']

    # Convert UTC time to 12-hour format with AM/PM
    formatted_times = [
        datetime.strptime(time_str, "%Y-%m-%dT%H:%M").strftime("%I:%M %p") for time_str in times
    ]

    # Pair the time and temperature for the next 6 hours
    forecast = list(zip(formatted_times[:6], temperatures[:6]))

    # Current temperature (first hour's temperature)
    current_temp = temperatures[0]

    return render_template_string(
        HTML_TEMPLATE,
        location=LOCATION_NAME,
        current_temp=current_temp,
        forecast=forecast
    )

if __name__ == '__main__':
    app.run(debug=True)
