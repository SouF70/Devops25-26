from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "845e51c4-d532-4567-a1d1-10ca78738b82"
GEOCODE_URL = "https://graphhopper.com/api/1/geocode"
ROUTE_URL = "https://graphhopper.com/api/1/route"

def get_coordinates(place):
    params = {
        "q": place,
        "limit": 1,
        "key": API_KEY
    }
    response = requests.get(GEOCODE_URL, params=params)
    data = response.json()
    lat = data["hits"][0]["point"]["lat"]
    lng = data["hits"][0]["point"]["lng"]
    return lat, lng

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        start = request.form["start"]
        end = request.form["end"]

        lat1, lng1 = get_coordinates(start)
        lat2, lng2 = get_coordinates(end)

        params = {
            "point": [f"{lat1},{lng1}", f"{lat2},{lng2}"],
            "vehicle": "car",
            "key": API_KEY
        }

        response = requests.get(ROUTE_URL, params=params)
        data = response.json()

        distance = round(data["paths"][0]["distance"] / 1000, 2)
        time = round(data["paths"][0]["time"] / 60000, 1)

        result = {
            "start": start,
            "end": end,
            "distance": distance,
            "time": time
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)