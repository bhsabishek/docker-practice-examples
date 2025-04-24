from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

# MySQL Configuration
for i in range(10):
        try:
            db = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="user_db"
            )
            print("Connected to database")
            cursor = db.cursor()  # Create a cursor object
            return db, cursor
        except Error as e:
            print(f"Attempt {i+1}: Unable to connect, retrying in 3 seconds...")
            time.sleep(3)
    raise Exception("Could not connect to the database after several attempts")

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