from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/cases/private')
def private_case():
    return render_template('cases/private.html')




if __name__ == '__main__':
    app.run(debug=True)

