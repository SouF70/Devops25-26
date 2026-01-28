import sqlite3
import hashlib
from flask import Flask, request, render_template, redirect, url_for

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


# 1️⃣ Startpagina → signup
@app.route("/")
def index():
    return redirect(url_for("signup"))


# 2️⃣ Signup pagina
@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect(DB)
        c = conn.cursor()

        try:
            c.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            message = "User already exists"
            conn.close()

    return render_template("signup.html", message=message)


# 3️⃣ Login pagina
@app.route("/login", methods=["GET", "POST"])
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
        conn.close()

        if record and record[0] == hashed:
            message = "Login success"
        else:
            message = "Invalid username/password"

    return render_template("login.html", message=message)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)
