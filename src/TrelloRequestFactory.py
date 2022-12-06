from .TrelloUtilities import Settings
from .TrelloRequest import TrelloRequest


baseUrl = f'https://api.trello.com'
memberRequest = f'/1/members'
boardRequest = f'/1/boards'


class TrelloRequestFactory():

    def __init__(self):

        self.settings = Settings()
        self.query = {
            "key": self.settings.credentials.key,
            "token": self.settings.credentials.token
        }
        self.headers = {
            "Accept": "application/json"
        }

    def getMember(self):

        url = f'{baseUrl}/{memberRequest}/{self.settings.userId}'
        request = TrelloRequest(url=url, params=self.query, headers=self.headers)
        return request.get()

    def getBoard(self, id):

        # GET /1/boards/{id}
        url = f'{baseUrl}/{boardRequest}/{id}'
        request = TrelloRequest(url=url, params=self.query, headers=self.headers)
        return request.get()

    def getBoardNames(self):

        url = f'{baseUrl}{memberRequest}/{self.settings.userId}/boards'

        # Need to create a custom query so that only the board name is returned
        # along with the board IDs
        query = {
            'fields': 'name',
            'key': self.query['key'],
            'token': self.query['token']
        }

        # Create a Trello Request and get response
        request = TrelloRequest(url=url,params=query,headers=self.headers)
        response = request.get()

        return response
