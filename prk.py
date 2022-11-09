
from app import clean_data

from constants import PLAYERS


CP = clean_data(PLAYERS)

Team = CP


def sort_players(Team):
    '''This fuction will sort the players of team by their height
    it receives as an input a list of dictionaries'''
    H = []
    Sorted_Team = []
    for player in Team:
        for key, value in player.items():
            if key == 'height':
                H.append(value)
    H.sort(reverse = True)
    print(H)
    i = 0
    while len(Team) > 0:
        for player in Team:
            for key, value in player.items():
                if (key == 'height') and (value >= H[i]):
                    Sorted_Team.append(player)
                    Team.remove(player)
                    i += 1
                    break
                else:
                    continue

    return Sorted_Team


sort_players(CP)