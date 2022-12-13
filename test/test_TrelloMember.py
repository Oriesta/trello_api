from ..src.TrelloMember import Member

'''
Function: test_GetMember

Purpose: This function is meant to be called by pytest and verifies the ability to 
instantiate a Member object and initializes it from a Trello Member request
'''
def test_getMember():

    member = Member()

    # Verify the member's user name was retrieved
    assert member.username == 'patrickfreel'

    # Verify the member's board list was returned
    

def test_getMemberBoards():
    member = Member()
    boards = member.getBoards()
    if boards:
        assert True == True
    else:
        assert True == False
