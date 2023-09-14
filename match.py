from api import get_match
from summoner import Summoner

class Match:
    def __init__(self, matchId):
        self.matchId = matchId

        self.load_match()

    def load_match(self):
        self.summoners = []
        match = get_match(self.matchId)
        for participant in match['metadata']['participants']:
            summoner = Summoner(puuid=participant)
            self.summoners.append(summoner)

if __name__ == '__main__':
    match = Match('NA1_4772229601')
    