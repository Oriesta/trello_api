from ..src.TrelloUtilities import Settings
from ..src.TrelloRequest import TrelloRequest

def test_getTrelloRequest():

    # create URL
    settings = Settings()
    url = f"https://api.trello.com/1/members/{settings.userId}"

    # create headers
    headers = {
        "Accept": "application/json"
        }

    # create params
    query = {
        'key': settings.credentials.key,
        'token': settings.credentials.token
        }
    
    # instantiate request object
    request = TrelloRequest(url, headers, query)

    # send request
    response = request.get()

    # check response
    assert response != ''
    assert response['username'] == 'patrickfreel'
