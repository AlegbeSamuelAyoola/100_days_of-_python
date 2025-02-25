from flask import Flask, request, render_template_string, redirect, url_for
import os

app = Flask(__name__)

# Example storage for saved jokes, replace with your database solution
saved_jokes = []

@app.route('/')
def home():
    return render_template_string('''
    <h1>Random Dad Joke</h1>
    <p id="joke"></p>
    <p><strong>Joke ID:</strong> <span id="joke-id"></span></p>
    <form id="save-joke-form" method="post" action="{{ url_for('save_joke') }}">
        <input type="hidden" id="joke-id-input" name="joke_id" value="">
        <input type="hidden" id="joke-text-input" name="joke_text" value="">
        <input type="submit" value="Save Joke" style="background-color: lightblue; cursor: pointer; border: none; padding: 5px 10px; display: block;">
    </form>
    <form method="get" action="{{ url_for('view_saved_jokes') }}">
        <input type="submit" value="View Saved Jokes" style="background-color: lightblue; cursor: pointer; border: none; padding: 5px 10px; display: block;">
    </form>
    <button onclick="loadJoke()" style="background-color: lightblue; cursor: pointer; border: none; padding: 5px 10px; display: block;">Load New Joke</button>

    <script>
    async function fetchJoke() {
        const response = await fetch("https://icanhazdadjoke.com/", { headers: { "Accept": "application/json" } });
        const joke = await response.json();
        return joke;
    }

    function displayJoke(joke) {
        document.getElementById('joke').textContent = joke.joke;
        document.getElementById('joke-id').textContent = joke.id;
        document.getElementById('joke-id-input').value = joke.id;
        document.getElementById('joke-text-input').value = joke.joke;
    }

    async function loadJoke() {
        const joke = await fetchJoke();
        displayJoke(joke);
    }

    // Load the joke when the page is loaded
    loadJoke();
    </script>
    ''')

@app.route('/save_joke', methods=['POST'])
def save_joke():
    joke_id = request.form['joke_id']
    joke_text = request.form['joke_text']
    joke_data = {"id": joke_id, "text": joke_text}
    if joke_data not in saved_jokes:
        saved_jokes.append(joke_data)
    return redirect(url_for('home'))

@app.route('/view_saved_jokes')
def view_saved_jokes():
    return render_template_string('''
    <h1>Saved Jokes</h1>
    <ul>
        {% for joke in saved_jokes %}
            <li>{{ joke.text }}</li>
        {% endfor %}
    </ul>
    <form method="get" action="{{ url_for('home') }}">
        <input type="submit" value="Back to Home" style="background-color: lightblue; cursor: pointer; border: none; padding: 5px 10px; display: block;">
    </form>
    ''', saved_jokes=saved_jokes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)