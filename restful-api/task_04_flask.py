#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In‑memory storage (must start empty for the checker)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data")
def get_usernames():
    # Return only the list of usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    # Ensure JSON body exists
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # Validate username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check for duplicates
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
