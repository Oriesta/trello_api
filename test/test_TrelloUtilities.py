from ..src import TrelloUtilities

'''
Function: test_getCredentials

Purpose: This function is meant to be called by pytest and verifies the ability to 
read in a Trello users public key and personal access token so that an http
request can be sent to the Trello API.
'''
def test_getCredentials():
    credentials = TrelloUtilities.Credentials()
    assert hasattr (credentials, 'key')
    assert hasattr (credentials, 'token')

'''
Function: test_getSettings

Purpose: This function is meant to be called by pytest and verifies the ability to 
read in user settings from a configuration file.
'''
def test_getSettings():
    settings = TrelloUtilities.Settings()
    assert hasattr(settings, 'userId')
    # assert hasattr(settings, 'credentials.key')
    # assert hasattr(settings, 'credentials.token')
    assert hasattr(settings, 'credentials')
    assert hasattr(settings.credentials, 'key')
    assert hasattr(settings.credentials, 'token')
