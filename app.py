from flask import Flask, render_template, request, redirect, url_for, flash
import logging
from datetime import datetime
import sys

app = Flask(__name__)
app.secret_key = 'my-secret-key'  # Required for flash messages

# Configure logging to ensure output goes to the console in Azure
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)

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
            logger.info(f"Successful login attempt - Username: {username}")
            print(f"Successful login attempt - Username: {username}")
            flash('Login successful!', 'success')
            return render_template('success.html')
        else:
            logger.warning(f"Failed login attempt - Username: {username}")
            print(f"Failed login attempt - Username: {username}")
            flash('Invalid username or password', 'error')
            
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True) 