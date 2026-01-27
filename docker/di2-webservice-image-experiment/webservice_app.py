from flask import Flask
from flask import render_template
from flask import request

webservice = Flask(__name__)

@webservice.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    webservice.run(host="0.0.0.0", port=5050, threaded=False)