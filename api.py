import requests
import json
import os
from config import api_key

base_url = "https://na1.api.riotgames.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}

def get_summoner(summoner_name):
    req_url = base_url + f"/lol/summoner/v4/summoners/by-name/{summoner_name}"
    r = requests.get(req_url, headers=headers).text
    return json.loads(r)

def get_masteries(puuid):
    req_url = base_url + f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"
    r = requests.get(req_url, headers=headers).text
    return json.loads(r)

def pull_champion_list():
    champ_list = {}
    req_url = "http://ddragon.leagueoflegends.com/cdn/13.18.1/data/en_US/champion.json"
    r = requests.get(req_url).text

    for champ in json.loads(r)["data"]:
        champ_list[json.loads(r)["data"][champ]["key"]] = json.loads(r)["data"][champ]["id"]

    return champ_list

def champion_id_to_name(champ_id):
    champ_list = pull_champion_list()
    return champ_list[str(champ_id)]

def get_champion_splash_art(champ_name):
    # check if file exists
    if os.path.exists(f"assets/{champ_name}.jpg"):
        print("File already exists")
        return
    req_url = f"http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champ_name}_0.jpg"
    r = requests.get(req_url, stream=True)
    if r.status_code == 200:
        with open(f"assets/{champ_name}.jpg", 'wb') as f:
            for chunk in r:
                f.write(chunk)

if __name__ == "__main__":
    get_champion_splash_art("Belvethfff")