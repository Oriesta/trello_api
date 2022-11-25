import sys
sys.path.append('../src')
import TrelloUtilities


def test_getCredentials():
    credentials = TrelloUtilities.Credentials()
    assert credentials.key != ''
    assert credentials.token != ''
