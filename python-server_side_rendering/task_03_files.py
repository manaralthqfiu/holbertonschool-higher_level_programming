#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, request, render_template
import json
import csv

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


@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate source
    if source not in ["json", "csv"]:
        return render_template("product_display.html",
                               error="Wrong source",
                               products=None)

    # Read data
    data = read_json_file() if source == "json" else read_csv_file()

    if data is None:
        return render_template("product_display.html",
                               error="Error reading file",
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
            return render_template("product_display.html",
                                   error="Invalid ID format",
                                   products=None)

    return render_template("product_display.html",
                           products=data,
                           error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
