# This code sample uses the 'requests' library:
# http://docs.python-requests.org
'''
import requests
import json
'''
from TrelloRequestFactory import TrelloRequestFactory
import json

'''
def get_lists_from_board(key, token, board_id):
    
    url = f'https://api.trello.com/1/boards/{board_id}/lists'

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': key,
        'token': token
    }

    response = requests.request("GET", url, headers=headers, params=query)

    if (response.status_code != 200):
        print(f'ERROR: get_lists_from_board() returned error {response.status_code}')
    else:
        return json.loads(response.text)
'''

def updateBoardFile():

    # Get the list 
    boards = TrelloRequestFactory().getBoardNames()

    # Write the file as long as it was update
    if boards:

        # Save the list as a json formatted file
        boards_json = json.dumps(boards, indent=4)

        # TODO: Make this relative path
        with open('/home/oriesta/repos/trello_api/data/boards.json','w') as boards_file:
            boards_file.write(boards_json)
