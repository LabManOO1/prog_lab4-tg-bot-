import requests


def top_games() -> list:  # Поиск 20-ти самых популярных игр
    response = requests.get('https://www.freetogame.com/api/games?sort-by=popularity').json()
    res = [game['title'] for game in response][:20]
    return res


def get_description_game(name: str) -> str:  # Поиск информации об игре
    response = requests.get('https://www.freetogame.com/api/games').json()
    for game in response:
        if game['title'] == name:
            game_id = game['id']
            response_id = requests.get(f'https://www.freetogame.com/api/game?id={game_id}').json()
            return response_id["description"]
    return ''


def get_category_list() -> list:  # Поиск жанров
    response = requests.get('https://www.freetogame.com/api/games').json()
    categories = []
    for game in response:
        categories.append(game['genre'])
    return list(set(categories))


def get_platforms_list() -> list:  # Поиск платформ
    response = requests.get('https://www.freetogame.com/api/games').json()
    platforms = []
    for game in response:
        platforms.append(game['platform'])
    return list(set(platforms))


def get_games_by_platforms(platform: str) -> list:  # Поиск игр определенной платформы
    platforms = {'PC (Windows)': 'pc', 'Web Browser': 'browser', 'PC (Windows), Web Browser': 'all'}

    response = requests.get(f'https://www.freetogame.com/api/games?platform={platforms[platform]}').json()
    res = [game['title'] for game in response]
    if len(res) > 20:
        res = res[:20]
    return res


def get_games_by_category(category: str) -> list:  # Поиск игр по жанру
    response = requests.get('https://www.freetogame.com/api/games').json()
    res = [game['title'] for game in response if game['genre'] == category]
    if len(res) > 20:
        res = res[:20]
    return res
