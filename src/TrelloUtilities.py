import json

'''
from datetime import datetime
import pytz
import TrelloMembers
import TrelloBoards
'''

class Credentials():

    key = ''
    token = ''

    def __init__(self):

        # open secrets.json to get key and token
        if self.key == '' or self.token == '':
            with open("../config/secrets.json", "r") as secrets_file:

                secrets = json.load(secrets_file)
                self.key = secrets['key']
                self.token = secrets['token']

'''
def get_secrets():

    # open secrets.json to get key and token
    with open("config/secrets.json", "r") as secrets_file:

        secrets = json.load(secrets_file)

    return secrets['key'], secrets['token']

def get_user_id():

    # open secrets.json to get key and token
    with open("config/settings.json", "r") as settings_file:

        settings = json.load(settings_file)
    
    settings_file.close()

    return settings['user_id']
        
def get_creation_date_from_id(id):

    # for trello items that have unique ids, the first 8 characters of the 
    # id contain a unix timestamp
    creation_time = datetime.fromtimestamp(int(id[0:8],16))

    # convert the timestamp to utc time
    utc_creation_time = pytz.utc.localize(creation_time)

    # return the datetime object in iso format
    return utc_creation_time

def find_board_by_name(name):

    # load authentication parameters
    # secrets = json.load(f)
    key, token = get_secrets()

    # load user settings
    user_id = get_user_id()

    # get boards
    boards = TrelloMembers.get_boards_for_member(key, token, user_id)

    for board in boards:
        if board['name'] == name:
            board_id = board['id']
            requested_board = board
            break
    
    if 'requested_board' in locals():
        return requested_board

def get_list_in_board(board_id, list_name):

    # load authentication parameters
    # secrets = json.load(f)
    key, token = get_secrets()

    lists = TrelloBoards.get_lists_from_board(key, token, board_id)

    for list in lists:
        if list['name'] == list_name:
            requested_list = list
            today_list_id = list['id']
            break

    return requested_list

def print_response(obj):

    print(json.dumps(obj, sort_keys=True, indent=4, separators=(",", ": ")))
    
'''

if __name__ == '__main__':

    credentials = Credentials()
    print(f'Key = {credentials.key}')
    print(f'Token =  {credentials.token}')
