import random, statistics

from constants import TEAMS, PLAYERS

Teams = TEAMS

Players = PLAYERS




def clean_data(data):
    for player in data:
        for key, value in player.items():
            if key == 'experience':
                player[key] = bool(value)
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


def balance_teams(Teams, c_players):
    Final_Teams = []
    for team in Teams:
        team = []
        while len(team) < n_players:
            n = random.randrange(0, len(c_players))
            team.append(c_players[n])
            c_players.remove(c_players[n])
        Final_Teams.append(team)
    return Final_Teams




def experince(Team):
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
    c_players = clean_data(Players)
    Final_Teams = balance_teams(Teams, c_players)
    print('''\n\t\t\tBASKETBALL TEAM STATS TOOL
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
            print(f'''\n\t\t\tA) {Teams[0]}
            \rB) {Teams[1]}
            \rC) {Teams[2]}''')
            try:
                choice = input('Enter a new option please: ').upper()
                if choice != 'A' and choice != 'B' and choice != 'C':
                    raise ValueError('please enter A, B, or C')
            except ValueError as err:
                print(f'{err}')

            else:
                if choice == 'A':
                    print(f'''\nTeam: {Teams[0]} Stats
                    \r---------------------------------
                    \rTotal players: {len(Final_Teams[0])}
                    \rTotal experienced: {experince(Final_Teams[0])}
                     \rTotal inexperienced: {(len(Final_Teams[0]))-(experince(Final_Teams[0]))}
                     \rAverage height: {average_height(Final_Teams[0])} inches''')
                    print('\n Players on Team: \n\t\t')
                    for player in Final_Teams[0]:
                        for key, value in player.items():
                            if key == 'name':
                                print(f'{value}',end=', ')
                    print('\n')
                    print(' Guardians: \n\t\t')
                    G = set()
                    for player in Final_Teams[0]:
                        for key, value in player.items():
                            if key == 'guardians':
                                G.update(set(value))
                    for name in G:
                        print(name, end=', ')
                    print('\n')





#Solve guardians and finish the program



if __name__ == '__main__':
    menu(Teams, Players)


