from flask import Flask, render_template_string, request

app = Flask(__name__)

# Predefined usernames, passwords, and emails
valid_users = {
    'user1': {'password': 'password1', 'email': 'user1@example.com'},
    'user2': {'password': 'password2', 'email': 'user2@example.com'},
    'user3': {'password': 'password3', 'email': 'user3@example.com'}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username, email, and password are valid
        if (username in valid_users and 
            valid_users[username]['password'] == password and 
            valid_users[username]['email'] == email):
            return "Successful login"
        else:
            return "Invalid credentials"
    
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login Form</title>
    </head>
    <body>
        <form method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>

            <input type="submit" value="Login">
        </form>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
