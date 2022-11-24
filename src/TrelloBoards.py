# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

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


    # debug print
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
