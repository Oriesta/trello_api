from datetime import datetime
import pytz
import json
from TrelloLists import *
from TrelloMembers import *
from TrelloBoards import *
from TrelloCards import *
import TrelloUtilities

if __name__ == "__main__":


    # # load authentication parameters
    # key, token = get_secrets()

    # # load user settings
    # user_id = get_user_id()

    # # get boards
    # boards = get_boards_for_member(key, token, user_id)

    # for board in boards:
    #     if board['name'] == "Routines":
    #         board_id = board['id']
    #         break
    
    # print(f'Routines board id: {board_id}')
    routine_board = TrelloUtilities.find_board_by_name('Python Test Board')
    TrelloUtilities.print_response(routine_board)


    # # get lists from board
    # lists = get_lists_from_board(key, token, board_id)

    # for list in lists:
    #     if list['name'] == 'Today':
    #         today_list_id = list['id']
    #         break
    
    # print(f'Today list id: {today_list_id}')

    # # get cards on daily task list
    # cards = get_cards_in_list(key, token, today_list_id)

    # for card in cards:

    #     card_id = card['id']

    #     # the due date for a card will be set to 22:00 hours of the creation date
    #     creation_date = get_creation_date_from_id(card_id)
    #     due_date = creation_date.replace(hour=22, minute=0, second=0)
        
    #     # set the due date
    #     update_a_card(key, token, card_id, field='due', value=due_date.isoformat())


