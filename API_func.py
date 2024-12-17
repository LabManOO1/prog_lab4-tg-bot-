import requests


def top_games() -> list:
    response = requests.get('https://www.freetogame.com/api/games?sort-by=popularity').json()
    res = [game['title'] for game in response][:20]
    return res


def get_description_game(name: str) -> str:
    response = requests.get('https://www.freetogame.com/api/games').json()
    for game in response:
        if game['title'] == name:
            game_id = game['id']
            response_id = requests.get(f'https://www.freetogame.com/api/game?id={game_id}').json()
            return response_id["description"]
    return ''


def get_category_list():
    response = requests.get('https://www.freetogame.com/api/games').json()
    categories = []
    for game in response:
        categories.append(game['genre'])
    return list(set(categories))


def get_platforms_list():
    response = requests.get('https://www.freetogame.com/api/games').json()
    platforms = []
    for game in response:
        platforms.append(game['platform'])
    return list(set(platforms))



