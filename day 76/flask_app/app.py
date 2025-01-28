from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask web server!"

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/linktree')
def linktree():
    return render_template('linktree.html')

if __name__ == '__main__':
    app.run(debug=True)
