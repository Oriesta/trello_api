import json
import requests
from TrelloConstants import *

def update_a_card(key, token, id, field, value):

    url = f"https://api.trello.com/1/cards/{id}"

    headers = {
    "Accept": "application/json"
    }

    query = {
    field: value,
    'key': key,
    'token': token,
    }

    response = requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )


def get_actions_on_card(secrets, id):

    url = f"https://api.trello.com/1/cards/{id}/actions"

    headers = {
    "Accept": "application/json"
    }

    query = {
    'key': secrets['key'],
    'token': secrets['token']
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
    )

    return json.loads(response.text)
