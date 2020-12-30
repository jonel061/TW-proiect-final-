# import cursor
import bcrypt
import mysql.connector
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'your secret key'
conn = mysql.connector.connect(host="localhost", user="root", password="BarbuJonel1226", database='autentificare')
cursor = conn.cursor()


@app.route('/map')
def map():
    return render_template('map2.html')


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login_validation', methods=['POST', 'GET'])
def login_validation():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        conn.close()

        if len(account) > 0:
            if (account['password'].encode('utf8')) == account['password'].encode('utf-8'):
                session['username'] = account['username']
                session['email'] = account['email']
            return render_template('home.html')
        # else:
        #  return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logout', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect('/')


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

    cursor.execute(
        'INSERT INTO accounts (username, email, password) VALUES (%s, %s ,%s)', (username, email, hash_password))
    conn.commit()
    session['username'] = username
    session['email'] = email
    return redirect('/home')


#  cursor.execute('INSERT INTO accounts (username, email , password) VALUES (%s ,%s ,%s)',
#                (username, email, password))


if __name__ == '__main__':
    app.run(debug=True)
