import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"

loc = "Washington, D.C."

key = "845e51c4-d532-4567-a1d1-10ca78738b82"

url = geocode_url + urllib.parse.urlencode({
    "q": loc,
    "limit": "1",
    "key": key
})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code

if json_status == 200:
    lat = json_data["hits"][0]["point"]["lat"]
    lng = json_data["hits"][0]["point"]["lng"]

    print(f"Location: {loc}")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}")
else:
    print("API request failed")