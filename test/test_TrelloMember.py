from ..src.TrelloMember import Member

'''
Function: test_GetMember

Purpose: This function is meant to be called by pytest and verifies the ability to 
instantiate a Member object and initializes it from a Trello Member request
'''
def test_getMember():
    member = Member()
    assert member.initialized == True
    assert member.username == 'patrickfreel'

def test_getMemberBoards():
    member = Member()
    boards = member.getBoards()
    if boards:
        assert True == True
    else:
        assert True == False
