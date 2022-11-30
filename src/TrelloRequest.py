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
        print(f'Response URL: {response.url}')
        if response.status_code == 200:
            data = json.loads(response.text)
        else:
            print(f'ERROR: http GET returned value {response.status_code}')
            print(f'URL: {response.url}')
            data = ''

        return data
