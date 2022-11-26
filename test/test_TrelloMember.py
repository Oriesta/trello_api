from ..src.TrelloMember import Member

'''
Function: test_GetMember

Purpose: This function is meant to be called by pytest and verifies the ability to 
instantiate a Member object and initializes it from a Trello Member request
'''
def test_GetMember():
    member = Member()
    assert member.initialized == True
