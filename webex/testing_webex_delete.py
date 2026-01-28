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
rooms = rooms_response.json()

if "items" not in rooms or len(rooms["items"]) == 0:
    print("Geen rooms gevonden")
    exit(0)

room_id = rooms["items"][0]["id"]
room_title = rooms["items"][0]["title"]

print("Room:", room_title)

# 2. Berichten ophalen uit die room
messages_url = "https://webexapis.com/v1/messages"
params = {
    "roomId": room_id,
    "max": 1
}

messages_response = requests.get(messages_url, headers=headers, params=params)
messages = messages_response.json()

if "items" not in messages or len(messages["items"]) == 0:
    print("Geen berichten gevonden in deze room")
    exit(0)

message_id = messages["items"][0]["id"]
message_text = messages["items"][0].get("text", "<geen tekst>")

print("Te verwijderen bericht:")
print(message_text)

# 3. Bericht verwijderen
delete_url = f"https://webexapis.com/v1/messages/{message_id}"
delete_response = requests.delete(delete_url, headers=headers)

print("Delete status:", delete_response.status_code)