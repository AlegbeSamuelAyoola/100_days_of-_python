from flask import Flask, render_template_string, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# user account
admin_username = 'admin'
admin_password = 'password'

posts = []

@app.route('/')
def home():
    if 'username' in session:
        return render_template_string(admin_template, posts=posts)
    return render_template_string(home_template, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == admin_username and password == admin_password:
            session['username'] = username
            return redirect(url_for('home'))
        return "Invalid credentials!"
    return render_template_string(login_template)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/add', methods=['POST'])
def add_post():
    if 'username' in session:
        title = request.form['title']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = request.form['body']
        posts.append({'title': title, 'date': date, 'body': body})
        return redirect(url_for('home'))
    return "You are not logged in!"

home_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Blog</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .post { margin-bottom: 20px; }
        .title { font-size: 24px; font-weight: bold; }
        .date { font-size: 14px; color: gray; }
        .body { font-size: 18px; }
        .login { margin-top: 20px; }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>
    <div class="login"><a href="/login">Login</a></div>
    <div class="feed">
        {% for post in posts %}
        <div class="post">
            <div class="title">{{ post.title }}</div>
            <div class="date">{{ post.date }}</div>
            <div class="body">{{ post.body }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

login_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .login-container { width: 300px; margin: 0 auto; padding-top: 100px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; }
        input[type="text"], input[type="password"] { width: 100%; padding: 8px; }
        button { padding: 10px; width: 100%; }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form method="post" action="/login">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
"""

admin_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Admin - Blog</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .logout { margin-top: 20px; }
        .form-container { width: 300px; margin: 0 auto; padding-top: 50px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; }
        input[type="text"], textarea { width: 100%; padding: 8px; }
        button { padding: 10px; width: 100%; }
    </style>
</head>
<body>
    <h1>Admin Panel</h1>
    <div class="logout"><a href="/logout">Logout</a></div>
    <div class="form-container">
        <h2>Add New Post</h2>
        <form method="post" action="/add">
            <div class="form-group">
                <label for="title">Title</label>
                <input type="text" id="title" name="title" required>
            </div>
            <div class="form-group">
                <label for="body">Body</label>
                <textarea id="body" name="body" rows="5" required></textarea>
            </div>
            <button type="submit">Save</button>
        </form>
    </div>
    <h2>Existing Posts</h2>
    <div class="feed">
        {% for post in posts %}
        <div class="post">
            <div class="title">{{ post.title }}</div>
            <div class="date">{{ post.date }}</div>
            <div class="body">{{ post.body }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
