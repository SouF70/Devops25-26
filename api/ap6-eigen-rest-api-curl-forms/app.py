from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "DevNet Basics", "author": "Cisco"},
    {"id": 2, "title": "API Calls", "author": "Yvan"}
]

# API – GET
@app.route("/api/v1/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

# API – POST (JSON of form)
@app.route("/api/v1/books", methods=["POST"])
def add_book():
    data = request.json if request.is_json else request.form

    if "title" not in data or "author" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(new_book)
    return jsonify(new_book), 201

# Webform
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"]
        }
        books.append({
            "id": len(books) + 1,
            **new_book
        })

    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(port=5003, debug=True)