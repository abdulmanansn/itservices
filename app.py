
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

os.makedirs("database", exist_ok=True)

def init_db():
    conn = sqlite3.connect("database/users.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/contact", methods=["POST"])
def contact():

    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid JSON"}), 400

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not all([name, email, message]):
        return jsonify({"message": "All fields are required"}), 400

    conn = sqlite3.connect("database/users.db")

    conn.execute(
        "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Your message was sent successfully!"
    })


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
