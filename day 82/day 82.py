from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    lang = request.args.get('lang', 'en')

    if lang == 'fr':
        message = 'Bonjour, et bienvenue sur notre merveilleux site web!'
    else:
        message = 'Hello, and welcome to our wonderful website!'

    return f'<h1>{message}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
