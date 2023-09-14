from api import champion_id_to_name

class Champion:
    def __init__(self, champion_id):
        self.champion_id = champion_id
        self.champion_name = champion_id_to_name(champion_id)

if __name__ == "__main__":
    champ = Champion(21)
    print(champ.champion_name)