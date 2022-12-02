# import requests
# import json
# import TrelloUtilities

from TrelloRequestFactory import TrelloRequestFactory


class Member():
    
    initialized = False
    
    def __init__(self):

        member_data = TrelloRequestFactory().getMember()
        if member_data != '':
            self.initialized = True
            self.__dict__.update(member_data)
    
    def getBoards(self):

        self.boards = TrelloRequestFactory().getBoardNames()
        return self.boards

    
    
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