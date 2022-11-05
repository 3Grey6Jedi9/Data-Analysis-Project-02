import random

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
                    player[key] = value.split('and')
                else:
                    player[key] = []
                    player[key].append(value)
    return data


c_players = clean_data(Players)




print(c_players)

n_players = len(Players) / len(Teams)



def balance_teams(Teams, c_players):
    Final_Teams = []
    for team in Teams:
        team = []
        while len(team) < n_players:
            n = random.Random(1, len(c_players) + 1)
            team.append(c_players[n])
            c_players.remove[n]
        Final_Teams.append(team)
    return Final_Teams


Final_Teams = balance_teams(Teams, c_players)

print(Final_Teams)























if __name__ == '__main__':
    pass

