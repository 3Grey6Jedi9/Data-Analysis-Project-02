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


c_player = clean_data(Players)

for i, v  in c_player[0].items():
    print(type(v))


print(c_player)





def balance_teams(Teams):
    for team in Teams:
        team = []
        pass
















if __name__ == '__main__':
    pass

