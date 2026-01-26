from flask import Flask, jsonify, request

app = Flask(__name__)

# Simpele in-memory data
books = [
    {"id": 1, "title": "DevNet Basics", "author": "Cisco"},
    {"id": 2, "title": "API Calls", "author": "Yvan"}
]

# GET – alle boeken
@app.route("/api/v1/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

# POST – nieuw boek toevoegen
@app.route("/api/v1/books", methods=["POST"])
def add_book():
    data = request.json

    if not data or "title" not in data or "author" not in data:
        return jsonify({"error": "Invalid JSON"}), 400

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(new_book)
    return jsonify(new_book), 201


if __name__ == "__main__":
    app.run(port=5001, debug=True)
