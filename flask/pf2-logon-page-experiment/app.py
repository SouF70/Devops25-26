import sqlite3
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__)
DB = "users.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        record = c.fetchone()

        if record and record[0] == hashed:
            message = "Login success"
        else:
            message = "Invalid username/password"

        conn.close()

    return render_template("login.html", message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)