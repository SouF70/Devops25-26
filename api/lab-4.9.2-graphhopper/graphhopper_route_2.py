import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"

key = "845e51c4-d532-4567-a1d1-10ca78738b82"


def geocode(location):
    url = geocode_url + urllib.parse.urlencode({
        "q": location,
        "limit": "1",
        "key": key
    })

    reply = requests.get(url)
    data = reply.json()

    lat = data["hits"][0]["point"]["lat"]
    lng = data["hits"][0]["point"]["lng"]

    return lat, lng


loc1 = input("Geef vertrekplaats: ")
loc2 = input("Geef bestemming: ")
vehicle = input("Vehicle (car, bike, foot): ")

lat1, lng1 = geocode(loc1)
lat2, lng2 = geocode(loc2)

route_params = {
    "point": [f"{lat1},{lng1}", f"{lat2},{lng2}"],
    "vehicle": vehicle,
    "key": key
}

route_request = requests.get(route_url, params=route_params)
route_data = route_request.json()

distance = route_data["paths"][0]["distance"] / 1000
time = route_data["paths"][0]["time"] / 1000 / 60

print("\nRoute resultaat")
print(f"Van: {loc1}")
print(f"Naar: {loc2}")
print(f"Vehicle: {vehicle}")
print(f"Afstand: {distance:.2f} km")
print(f"Reistijd: {time:.2f} minuten")