from ..src.TrelloRequestFactory import TrelloRequestFactory

def test_getMember():

    factory = TrelloRequestFactory()
    memberData = factory.getMember()
    assert memberData['username'] == 'patrickfreel'
    