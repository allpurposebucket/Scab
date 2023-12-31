from api import get_summoner, get_masteries, champion_id_to_name, get_match_ids

class Summoner:

    def __init__(self, summoner_name=None, puuid=None):
        self.summoner_name = summoner_name
        self.puuid = puuid
        self.load_summoner()
        self.load_masteries()
        self.load_matches()
    
    def load_summoner(self):
        try:
            summoner_data = get_summoner(self.summoner_name, self.puuid)
            self.summoner_id = summoner_data["id"]
            self.account_id = summoner_data["accountId"]
            self.puuid = summoner_data["puuid"]
            self.profile_icon_id = summoner_data["profileIconId"]
            self.revision_date = summoner_data["revisionDate"]
            self.summoner_level = summoner_data["summonerLevel"]
        except Exception as e:
            print(e)
            print("Summoner not found: " + self.summoner_name)

    def load_masteries(self):
        try:
            self.masteries = {}
            masteries_data = get_masteries(self.puuid)
            for champ in masteries_data:
                champ_name = champion_id_to_name(champ["championId"])
                self.masteries[champ_name] = champ["championPoints"]
        except Exception as e:
            print(e)
            print("Masteries not found")
    
    def load_matches(self):
        try:
            self.matches = get_match_ids(self.puuid)
        except Exception as e:
            print(e)
            print("Matches not found")
    
    def __str__(self):
        return f"Summoner Name: {self.summoner_name}\nSummoner ID: {self.summoner_id}\n" \
            f"Account ID: {self.account_id}\nPUUID: {self.puuid}\n" \
            f"Profile Icon ID: {self.profile_icon_id}\nRevision Date: {self.revision_date}\n" \
            f"Summoner Level: {self.summoner_level}\n" \
            f"Masteries: {self.masteries}\n" \
            f"Matches: {self.matches}"

if __name__ == "__main__":
    smnr = Summoner("allpurposebucket")
    print(smnr)