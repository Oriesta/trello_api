from .TrelloRequestFactory import TrelloRequestFactory
from .TrelloBoard import TrelloBoard


class Member():
    
    # Constructor
    def __init__(self):

        # Add Trello member data to the object
        request_factory = TrelloRequestFactory()
        member_data = request_factory.getMember()
        if member_data != '':
            self.initialized = True
            self.__dict__.update(member_data)
        
            # Get all boards for member
            self.boards = dict()
            for id in self.idBoards:
                board = TrelloBoard(id=id)
                self.boards[board.name] = board

    def getBoards(self):
        
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
'''
