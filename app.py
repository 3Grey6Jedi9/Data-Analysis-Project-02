import random

from constants import TEAMS, PLAYERS

Teams = TEAMS

Players = PLAYERS


def menu():
    print('''\t\t\tBASKETBALL TEAM STATS TOOL
\r---- MENU ----
Here are your choices:
A) Display Team Stats
B) Quit''')





def clean_data(data):
    for player in data:
        for key, value in player.items():
            if key == 'experience':
                player[key] = bool(value)
        for key, value in player.items():
            if key == 'guardians':
                if 'and' in value:
                    player[key] = value.split('and')
                else:
                    player[key] = []
                    player[key].append(value)
    return data


c_players = clean_data(Players)


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


Final_Teams = balance_teams(Teams, c_players)

#print(len(Final_Teams[0]))

#MENU



























if __name__ == '__main__':
    pass

