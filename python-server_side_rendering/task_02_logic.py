#!/usr/bin/python3
"""
Task 2: Dynamic Template with Loops and Conditions
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    """Reads items from items.json and renders them in a template."""
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except Exception:
        items_list = []

    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
