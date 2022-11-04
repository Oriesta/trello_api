import json
import requests
from TrelloConstants import *

def get_cards_in_list(key, token, list_id):

    url = f"https://api.trello.com/1/lists/{list_id}/cards"

    headers = {
        "Access": "application/json"
    }

    query = {
        'key': key,
        'token': token
    }

    response = requests.request("GET", url, headers=headers, params=query)

    if (response.status_code != 200):
        print(f'ERROR: get_cards_in_list() returned error {response.status_code}')
    else:
        return json.loads(response.text)