
from app import clean_data, experts

from constants import PLAYERS


CP = clean_data(PLAYERS)

Team = CP





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


s = experince(Team)



e = experts(Team)

print(e)