#!/usr/bin/python3
"""
Task 4: Extending Dynamic Data Display to Include SQLite
"""

from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    """Reads and returns product data from JSON file."""
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception:
        return None


def read_csv_file():
    """Reads and returns product data from CSV file."""
    products = []
    try:
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception:
        return None


def read_sqlite_db():
    """Reads and returns product data from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()
        return products

    except Exception:
        return None


@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate source
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html",
                               error="Wrong source",
                               products=None)

    # Read data based on source
    if source == "json":
        data = read_json_file()
    elif source == "csv":
        data = read_csv_file()
    else:  # SQL
        data = read_sqlite_db()

    if data is None:
        return render_template("product_display.html",
                               error="Error reading file or database",
                               products=None)

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p["id"] == product_id]
            if not filtered:
                return render_template("product_display.html",
                                       error="Product not found",
                                       products=None)
            data = filtered
        except ValueError:
            return render_template("product_display
