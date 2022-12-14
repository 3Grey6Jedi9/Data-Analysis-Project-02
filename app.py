import random, statistics

import sys

from constants import TEAMS, PLAYERS

Teams = TEAMS

Players = PLAYERS




def clean_data(data):
    '''This function cleans the data PLAYERS like'''
    for player in data:
        for key, value in player.items():
            if key == 'experience' and value == 'YES':
                player[key] = bool(value)
            elif key == 'experience' and value == 'NO':
                player[key] = False
        for key, value in player.items():
            if key == 'guardians':
                if 'and' in value:
                    player[key] = value.split(' and ')
                else:
                    player[key] = []
                    player[key].append(value)
        for key, value in player.items():
            if key == 'height':
                player[key] = int(((value.split(' ')[0])))

    return data



n_players = len(Players) / len(Teams)



def balance_teams(Teams, Players):
    '''This function set up the Teams'''
    c_players =  clean_data(Players)
    exppt = experience(c_players) / len(Teams)
    Final_Teams = []
    for team in Teams:
        team = []
        while experience(team) < exppt:
            n = random.randrange(0, len(c_players))
            for key, value in c_players[n].items():
                if key == 'experience' and value == True:
                    team.append(c_players[n])
                    c_players.remove(c_players[n])
                else:
                    continue
        while (len(team) < n_players):
            n = random.randrange(0, len(c_players))
            for key, value in c_players[n].items():
                if key == 'experience' and value == False:
                    team.append(c_players[n])
                    c_players.remove(c_players[n])
                else:
                    continue

        Final_Teams.append(team)
    return Final_Teams




def experience(Team):
    '''This function returns the number of experienced players'''
    number_experts = 0
    for players in Team:
        for key, value in players.items():
            if key == 'experience':
                if players[key]:
                    number_experts += 1
                else:
                    continue
    return number_experts




def average_height(Team):
    heights = []
    for player in Team:
        for key, value in player.items():
            if key == 'height':
                heights.append(player[key])
            else:
                continue
    average = statistics.mean(heights)
    return average









def menu(Teams, Players):
    '''This would be the main function'''
    Final_Teams = balance_teams(Teams, Players)
    final_teams = []
    again = ''
    while again != 'q':
        print('''\n\t\t\t\033[1;3mBASKETBALL TEAM STATS TOOL\033[0m
\r---- MENU ----
Here are your choices:
A) Display Team Stats
B) Quit''')
        try:
            choice = input('Enter an option: ').upper()
            if choice != 'A' and choice != 'B':
                raise ValueError('please enter A or B')
        except ValueError as err:
            print(f'{err}')
        else:
            if choice == 'A':
                print(f'''\nA) {Teams[0]}
                \rB) {Teams[1]}
                \rC) {Teams[2]}''')
                while ValueError and again != 'q':
                    try:
                        choice = input('\nEnter a new option please: ').upper()
                        if choice != 'A' and choice != 'B' and choice != 'C':
                            raise ValueError('please enter A, B, or C')
                    except ValueError as err:
                        print(f'{err}')

                    else:
                        i = 0
                        if choice == 'A':
                            i = 0
                        elif choice == 'B':
                            i = 1
                        elif choice == 'C':
                            i = 2
                        else:
                            pass

                        print(f'''\nTeam: {Teams[i]} Stats
                        \r---------------------------------
                        \r\033[1;3mTotal players:\033[0m {len(Final_Teams[i])}
                        \r\033[1;3mTotal experienced:\033[0m {experience(Final_Teams[i])}
                        \r\033[1;3mTotal inexperienced:\033[0m {(len(Final_Teams[i]))-(experience(Final_Teams[i]))}                     
                        \r\033[1;3mAverage height:\033[0m {average_height(Final_Teams[i])} inches''')
                        print('\n \033[1;3mPlayers on Team:\033[0m \n\t\t')
                        PL = []
                        for player in sort_players(Final_Teams[i]):
                            for key, value in player.items():
                                if key == 'name':
                                    print(f' {value},',end=' ')
                                    PL.append(value)
                        print('\n')
                        print(' \033[1;3mGuardians:\033[0m \n\t\t')
                        G = set()
                        GU = []
                        for player in Final_Teams[i]:
                            for key, value in player.items():
                                if key == 'guardians':
                                    G.update(set(value))
                        for name in G:
                            print(f' {name},', end=' ')
                            GU.append(name)
                        print('\n')
                        final_team = {'team name': Teams[i].upper(),
                                      'players': PL,
                                      'guardians': GU,
                                      'num_of_experienced': experience(Final_Teams[i]),
                                      'num_of_unexperienced': (len(Final_Teams[i]))-(experience(Final_Teams[i])),
                                      'average_height': average_height(Final_Teams[i])}
                        final_teams.append(final_team)
                        print(final_teams)
                    break
            elif choice == 'B':
                sys.exit()
        again = input('\nPress ENTER to continue... or enter "q" if you want to quit: ').lower()


def sort_players(Team):
    '''This fuction will sort the players of team by their height
    it receives as an input a list of dictionaries'''
    H = []
    Sorted_Team = []
    Team_copy = Team.copy()
    for player in Team_copy:
        for key, value in player.items():
            if key == 'height':
                H.append(value)
    H.sort(reverse = True)
    i = 0
    while len(Team_copy) > 0:
        for player in Team_copy:
            for key, value in player.items():
                if (key == 'height') and (value >= H[i]):
                    Sorted_Team.append(player)
                    Team_copy.remove(player)
                    i += 1
                    break
                else:
                    continue

    return Sorted_Team












if __name__ == '__main__':
    menu(Teams, Players)





