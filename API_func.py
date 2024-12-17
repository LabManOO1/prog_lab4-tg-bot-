import requests


def top_games():
    response = requests.get('https://www.freetogame.com/api/games?sort-by=popularity').json()
    res = [game['title'] for game in response][:20]
    return res
