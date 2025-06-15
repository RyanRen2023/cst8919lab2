from flask import Flask, render_template, request, redirect, url_for, flash
import logging
from datetime import datetime
import sys

app = Flask(__name__)
app.secret_key = 'my-secret-key'  # Required for flash messages

# Configure logging to ensure output goes to the console in Azure
# Ensure logs go to stdout for Azure App Service Linux
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Apply to app.logger (used internally by Flask + Gunicorn)
app.logger.setLevel(logging.INFO)
if not app.logger.handlers:
    app.logger.addHandler(handler)

# Apply to root logger (in case other modules use logging.warning/info)
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
if not root_logger.handlers:
    root_logger.addHandler(handler)

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
            app.logger.info(f"Successful login attempt - Username: {username}")
            print(f"Successful login attempt - Username: {username}")
            flash('Login successful!', 'success')
            return render_template('success.html')
        else:
            app.logger.warning(f"Failed login attempt - Username: {username}")
            print(f"Failed login attempt - Username: {username}")
            flash('Invalid username or password', 'error')
            
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True) 