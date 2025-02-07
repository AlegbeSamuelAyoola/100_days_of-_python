from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Dummy user credentials
USER_CREDENTIALS = {'username': 'admin', 'password': 'password'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username  # Store user session
            return redirect(url_for('home'))  # Redirect to home page after login
        
        return render_template('login.html', error="Invalid credentials")  # Show error message

    return render_template('login.html')

@app.route('/')
def home():
    if 'user' not in session:  # Check if user is logged in
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog2.html')

@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
