# import sys
# sys.path.append('../src')
# import TrelloUtilities
from ..src import TrelloUtilities

'''
Function: test_getCredentials

Purpose: This function is meant to be called by pytest and verifies the ability to 
read in a Trello users public key and personal access token so that an http
request can be sent to the Trello API.
'''
def test_getCredentials():
    credentials = TrelloUtilities.Credentials()
    # assert credentials.key != ''
    assert hasattr (credentials, 'key')
    # assert credentials.token != ''
    assert hasattr (credentials, 'token')


def test_getSettings():
    settings = TrelloUtilities.Settings()
    assert hasattr(settings, 'userId')
    
