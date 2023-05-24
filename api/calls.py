import requests
import os
from dotenv import load_dotenv

# Load .env vars
load_dotenv()

# Set your client ID and client secret
client_id = os.getenv("ClientID")
client_secret = os.getenv("ClientSecret")


def acquireToken():
    # Set the API endpoint and parameters
    endpoint = "https://accounts.spotify.com/api/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    # Make the POST request
    response = requests.post(endpoint, data=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the access token from the response
        access_token = response.json()
        return ("Access Token:", access_token)
    else:
        return ("Error:", response.text)


print(acquireToken())
