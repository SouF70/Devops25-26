from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "PF3 Microservice",
        "status": "running"
    })

@app.route("/info")
def info():
    return jsonify({
        "course": "DevOps",
        "experiment": "PF3 - Eigen microservice",
        "technology": "Flask"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5002)
