import requests
import json
import TrelloUtilities

# # Uncomment me when ready to implement Member class
# settings = TrelloUtilities.Settings()

# class Member():

#   def __init__(self):
    
#     url = f"https://api.trello.com/1/members/{settings.userId}"

#     headers = {
#       "Accept": "application/json"
#     }

#     query = {
#       'key': settings.credentials.key,
#       'token': settings.credentials.token
#     }

#     response = requests.request(
#       "GET",
#       url,
#       headers=headers,
#       params=query
#     )

#     if (response.status_code == 200):
#       self.data = json.loads(response.text)
#     else:
#       print(f'Error: Failed to get member data. Request returned with response {response.status_code}.')
#       self.data = None

# # Uncomment me when ready to introduce Member class
#   def keys(self):

#     print(self.data.keys())
    
    
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

# if __name__ == '__main__':

#   member = Member()
#   member.keys()