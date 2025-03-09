from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = '3c5a790b2d08429488504b67ceca2648'  # Needed for flashing messages
bcrypt = Bcrypt(app)


client = MongoClient('mongodb://localhost:27017/')
db = client['CaseFlowDB']  # Your database name
users = db['users']  # Collection for user data
cases = db['cases']  # Collection for cases


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['email']  # using 'email' field to collect user_id
        password = request.form['password']

        user = users.find_one({'user_id': user_id})

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user_id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid User ID or Password.', 'error')

    return render_template('login.html')

# SIGNUP ROUTE
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        user_id = request.form['email']  # using 'email' field as user_id
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('signup'))

        if users.find_one({'user_id': user_id}):
            flash('User ID already exists. Try another.', 'error')
            return redirect(url_for('signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        users.insert_one({
            'full_name': full_name,
            'user_id': user_id,
            'password': hashed_password
        })

        flash('Signup successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# LOGOUT ROUTE
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/cases/private')
def private_case():
    return render_template('cases/private.html')

if __name__ == '__main__':
    app.run(debug=True)
