import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"

loc1 = "Washington, D.C."

key = "845e51c4-d532-4567-a1d1-10ca78738b82" 

url = geocode_url + urllib.parse.urlencode({
    "q": loc1,
    "limit": "1",
    "key": key
})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code

print(json_data)