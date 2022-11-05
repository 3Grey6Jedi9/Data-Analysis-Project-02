from constants import TEAMS, PLAYERS

Teams = TEAMS

Players = PLAYERS

def clean_data():
    for player in Players:
        for key, value in player.items():
            if key == 'experience':
                bool(value)
            elif key == 'guardians':
                if 'and' in value:
                    value.split('and')
                else:
                    value.split()











if __name__ == '__main__':
    pass

