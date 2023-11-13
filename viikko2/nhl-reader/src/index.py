import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    players = [Player(player_data) for player_data in response if player_data['nationality'] == 'FIN']

    print("Players from FIN\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
