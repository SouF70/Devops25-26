import requests
import os

# Haal het Webex token uit de environment variable
access_token = os.environ.get("WEBEX_TOKEN")

if not access_token:
    print("ERROR: WEBEX_TOKEN is niet ingesteld")
    exit(1)

# Webex API endpoint
url = "https://webexapis.com/v1/people/me"

# HTTP headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# API call
response = requests.get(url, headers=headers)

# Resultaat tonen
print(response.status_code)
print(response.json())