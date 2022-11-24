import sys
sys.path.append('../src')
import TrelloUtilities

def test_getKey():
    credentials = TrelloUtilities.Credentials()
    assert credentials.key != ''
