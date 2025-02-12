from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    lang = request.args.get('lang', 'en')

    if lang == 'fr':
        message = 'Bonjour, et bienvenue sur notre merveilleux site web!'
    else:
        message = 'Hello, and welcome to our wonderful website!'

    return f'<h1>{message}</h1>'

@app.route('/theme1')
def theme1():
    lang = request.args.get('lang', 'en')

    if lang == 'fr':
        message = 'Bonjour, et bienvenue sur notre merveilleux site web! (Thème 1)'
    else:
        message = 'Hello, and welcome to our wonderful website! (Theme 1)'

    theme = """
    <style>
        body { background-color: lightblue; color: darkblue; }
        h1 { font-family: Arial, sans-serif; }
    </style>
    <h1>{{ message }}</h1>
    """

    return render_template_string(theme, message=message)

@app.route('/theme2')
def theme2():
    lang = request.args.get('lang', 'en')

    if lang == 'fr':
        message = 'Bonjour, et bienvenue sur notre merveilleux site web! (Thème 2)'
    else:
        message = 'Hello, and welcome to our wonderful website! (Theme 2)'

    theme = """
    <style>
        body { background-color: lightgreen; color: darkgreen; }
        h1 { font-family: Verdana, sans-serif; }
    </style>
    <h1>{{ message }}</h1>
    """

    return render_template_string(theme, message=message)

if __name__ == '__main__':
    app.run(debug=True)
