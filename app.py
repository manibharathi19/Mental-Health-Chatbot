from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
import threading

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory user storage (replace with a database in production)
users = {}




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('chatbot'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'User already exists'
        users[username] = {'password': generate_password_hash(password)}
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/chatbot')
def chatbot():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chatbot.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

def run_gradio():
    os.system("python gradio_app.py")

if __name__ == '__main__':
    threading.Thread(target=run_gradio).start()
    app.run(debug=True)
