from flask import Flask, render_template, request, redirect, url_for, flash
import logging
from datetime import datetime
import sys

app = Flask(__name__)
app.secret_key = 'my-secret-key'  # Required for flash messages

# Configure logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Dummy user credentials for demonstration
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            logging.info(f"Successful login attempt - Username: {username}")
            flash('Login successful!', 'success')
            return render_template('success.html')
        else:
            logging.warning(f"Failed login attempt - Username: {username}")
            flash('Invalid username or password', 'error')
            
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True) 