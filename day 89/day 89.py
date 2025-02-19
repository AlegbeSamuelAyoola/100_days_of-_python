from flask import Flask, request, redirect, url_for, render_template_string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Sample usernames and messages for seeding the database
sample_data = [
    {"username": "Alice", "message": "Hey there! How's everyone doing today?"},
    {"username": "Bob", "message": "I'm learning Flask. It's awesome!"},
    {"username": "Charlie", "message": "Does anyone want to discuss Python projects?"},
    {"username": "David", "message": "Flask-SQLAlchemy makes database work easy."},
    {"username": "Eve", "message": "Security in web apps is so important."}
]

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

login_template = '''
<!DOCTYPE html>
<html>
<head><title>Login - Community Chat</title></head>
<body>
    <h2>Login to Community Chat</h2>
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Enter your username" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
'''

chat_template = '''
<!DOCTYPE html>
<html>
<head><title>Chat Room</title></head>
<body>
    <h1>Welcome, {{ username }}</h1>
    {% if admin %}
        <form action="/admin/{{ username }}" method="get">
            <button type="submit">Admin Panel</button>
        </form>
    {% endif %}
    <div id="chat-box">
        {% for message in messages %}
            <div style="border:1px solid #ccc; padding:10px; margin:5px;">
                <strong>{{ message.username }}:</strong> {{ message.content }} <em>({{ message.timestamp }})</em>
                {% if admin %}
                    <form action="/delete_message/{{ message.id }}/{{ username }}" method="post" style="display:inline;">
                        <button type="submit">Delete</button>
                    </form>
                {% endif %}
            </div>
        {% endfor %}
    </div>
    <form action="/send_message" method="post">
        <input type="hidden" name="username" value="{{ username }}">
        <input type="text" name="content" placeholder="Enter your message" required>
        <button type="submit">Send</button>
    </form>
</body>
</html>
'''

admin_panel_template = '''
<!DOCTYPE html>
<html>
<head><title>Admin Panel</title></head>
<body>
    <h1>Admin Panel - Welcome, Admin</h1>
    <a href="/chat/admin">Back to Chat Room</a>
    <div id="chat-box">
        {% for message in messages %}
            <div style="border:1px solid #ccc; padding:10px; margin:5px;">
                <strong>{{ message.username }}:</strong> {{ message.content }} <em>({{ message.timestamp }})</em>
                <form action="/delete_message/{{ message.id }}/admin" method="post" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </div>
        {% endfor %}
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(login_template)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    if username.lower() == 'admin':
        return redirect(url_for('admin_panel', username=username))
    return redirect(url_for('chat', username=username))

@app.route('/chat/<username>')
def chat(username):
    messages = Message.query.order_by(Message.timestamp.desc()).limit(5).all()[::-1]
    admin = username.lower() == "admin"
    return render_template_string(chat_template, username=username, messages=messages, admin=admin)

@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form['username']
    content = request.form['content']
    new_message = Message(username=username, content=content)
    db.session.add(new_message)
    db.session.commit()
    return redirect(url_for('chat', username=username))

@app.route('/delete_message/<int:message_id>/<username>', methods=['POST'])
def delete_message(message_id, username):
    message = Message.query.get(message_id)
    if message:
        db.session.delete(message)
        db.session.commit()
    return redirect(url_for('admin_panel' if username.lower() == 'admin' else 'chat', username=username))

@app.route('/admin/<username>')
def admin_panel(username):
    if username.lower() != 'admin':
        return redirect(url_for('chat', username=username))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template_string(admin_panel_template, username=username, messages=messages)

# Seed database with initial random messages if empty
def seed_database():
    if Message.query.count() == 0:
        for data in sample_data:
            db.session.add(Message(username=data["username"], content=data["message"]))
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_database()
    app.run(debug=True)