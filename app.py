from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import time

app = Flask(__name__)
app.secret_key = 'super_secure_advanced_secret'

# Advanced Mock Database
# Now tracking 'failed_attempts' and 'lock_until'
users = {} 
todos = {}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash("Please log in to access this page.")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pw = request.form.get('password')

        if user not in users:
            flash("Invalid credentials.")
            return render_template('login.html')

        # --- ADVANCED SECURITY: RATE LIMITING CHECK ---
        current_time = time.time()
        if users[user].get('lock_until', 0) > current_time:
            remaining = int(users[user]['lock_until'] - current_time)
            flash(f"Account locked! Try again in {remaining} seconds.")
            return render_template('login.html')

        if check_password_hash(users[user]['pw'], pw):
            # Success: Reset failed attempts
            users[user]['failed_attempts'] = 0
            session['user'] = user
            return redirect(url_for('dashboard'))
        else:
            # Failure: Increment attempts
            users[user]['failed_attempts'] = users[user].get('failed_attempts', 0) + 1
            
            if users[user]['failed_attempts'] >= 3:
                users[user]['lock_until'] = current_time + 30 # Lock for 30 seconds
                flash("Too many failed attempts. Account locked for 30 seconds.")
            else:
                flash(f"Invalid credentials. ({3 - users[user]['failed_attempts']} attempts left)")
                
    return render_template('login.html')

# (Include your existing register, dashboard, and logout routes here)