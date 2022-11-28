from TrelloUtilities import Settings
from TrelloRequest import TrelloRequest



baseUrl = f'https://api.trello.com'
memberRequest = f'/1/members'


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

        url = f'{baseUrl}{memberRequest}/{self.settings.userId}'
        request = TrelloRequest(url=url, params=self.query, headers=self.headers)
        return request.get()
