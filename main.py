import requests
from pprint import pprint

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    url = 'https://akabab.github.io/superhero-api/api/all.json' # адрес обращения
    response = requests.get(url)
    hero_list = (response.json())
    # pprint(hero_list)
    three_hero = {}
    for hero in hero_list:
        if hero['name'] == 'Captain America':
            three_hero[hero['name']] = hero['powerstats']['intelligence']
        elif hero['name'] == 'Hulk':
            three_hero[hero['name']] = hero['powerstats']['intelligence']
        elif hero['name'] == 'Thanos':
            three_hero[hero['name']] = hero['powerstats']['intelligence']
    the_smartest_superhero = max(three_hero.items(), key=lambda x: x[1])[0]
    print(the_smartest_superhero)
    return the_smartest_superhero

get_the_smartest_superhero()