from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="user_db"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        return render_template("welcome.html", username=username)
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)