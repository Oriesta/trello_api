import requests
import json

class TrelloRequest():

    url = ''
    headers = dict
    params = dict

    def __init__(self, url, params, headers):

        self.url = url
        self.headers = headers
        self.params = params
        return
    
    def get(self):

        response = requests.get(url=self.url, params=self.params, headers=self.headers)
        if response.status_code == 200:
            data = json.loads(response.text)
        else:
            data = ''

        return data
