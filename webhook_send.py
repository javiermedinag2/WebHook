import requests
import json

webhook_url = "https://webhook.site/27df9e33-d0a7-4c7f-8888-debc6ed46a9e"
message = {
    "text": "Hello, World!",
    "mustafo_data": "Chilpandolfo"
}

response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'}) 
if response.status_code == 200:    print("Message sent successfully!")
else:
    print(f"Failed to send message. Status code: {response.status_code}")  