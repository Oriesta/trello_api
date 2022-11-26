import requests
import json
import TrelloUtilities


class Member():
    
    initialized = False
    
    def __init__(self):

        settings = TrelloUtilities.Settings()
        url = f"https://api.trello.com/1/members/{settings.userId}"
        
        headers = {
            "Accept": "application/json"
            }

        query = {
            'key': settings.credentials.key,
            'token': settings.credentials.token
            }
            
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
            )
        
        if (response.status_code == 200):
            #   self.data = json.loads(response.text)
            self.__dict__.update(json.loads(response.text))
            self.initialized = True
        else:
            print(f'Error: Failed to get member data. Request returned with response {response.status_code}.')
            self.data = None

    
    
'''
import json
import requests
from TrelloConstants import *


def get_boards_for_member(key, token, user_id):

    url = f"https://api.trello.com/1/members/{user_id}/boards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': key,
        'token': token
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
    )

    return json.loads(response.text)

if __name__ == '__main__':
    
    # get authentication params
    with open("config/secrets.json","r") as f:
        
        # load authentication parameters
        secrets = json.load(f)

        # get boards
        response = get_boards_for_member(secrets)

        # show results
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
'''