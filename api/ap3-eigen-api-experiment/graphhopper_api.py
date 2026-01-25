import requests

api_key = "845e51c4-d532-4567-a1d1-10ca78738b82"

geocode_url = "https://graphhopper.com/api/1/geocode"
route_url = "https://graphhopper.com/api/1/route"

from_place = "Brussels,Belgium"
to_place = "Antwerp,Belgium"

def get_coordinates(place):
    params = {
        "q": place,
        "limit": 1,
        "key": api_key
    }
    response = requests.get(geocode_url, params=params)
    data = response.json()
    lat = data["hits"][0]["point"]["lat"]
    lng = data["hits"][0]["point"]["lng"]
    return lat, lng

lat1, lng1 = get_coordinates(from_place)
lat2, lng2 = get_coordinates(to_place)

route_params = {
    "point": [f"{lat1},{lng1}", f"{lat2},{lng2}"],
    "vehicle": "car",
    "key": api_key
}

route_response = requests.get(route_url, params=route_params)
route_data = route_response.json()

distance_km = route_data["paths"][0]["distance"] / 1000
time_min = route_data["paths"][0]["time"] / 60000

print("Route:", from_place, "→", to_place)
print("Afstand:", round(distance_km, 2), "km")
print("Reistijd:", round(time_min, 1), "minuten")