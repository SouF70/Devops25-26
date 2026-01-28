import requests
import os

access_token = os.environ.get("WEBEX_TOKEN")

if not access_token:
    print("ERROR: WEBEX_TOKEN is niet ingesteld")
    exit(1)

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# 1. Rooms ophalen
rooms_url = "https://webexapis.com/v1/rooms"
rooms_response = requests.get(rooms_url, headers=headers)

print("Rooms status:", rooms_response.status_code)
rooms = rooms_response.json()

if "items" not in rooms or len(rooms["items"]) == 0:
    print("Geen rooms gevonden")
    exit(0)

# Eerste room gebruiken
room_id = rooms["items"][0]["id"]
room_title = rooms["items"][0]["title"]

print("Room:", room_title)

# 2. Message sturen naar die room
message_url = "https://webexapis.com/v1/messages"
message_data = {
    "roomId": room_id,
    "text": "Hallo! Dit bericht werd verstuurd via een Python script (Lab 8.6.7)."
}

message_response = requests.post(message_url, headers=headers, json=message_data)

print("Message status:", message_response.status_code)
print(message_response.json())