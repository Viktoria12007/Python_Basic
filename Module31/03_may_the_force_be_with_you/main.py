import requests
import json
from typing import List

result: object = requests.get('https://swapi.dev/api/starships/10/')
data: dict = json.loads(result.text)

pilots: List[dict] = list(map(lambda pilot: json.loads(requests.get(pilot).text), data['pilots']))
data['pilots'] = pilots

starship_keys: List[str] = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']
pilots_keys: List[str] = ['name', 'height', 'mass', 'homeworld']
pilots_keys_for_del: set = set(data['pilots'][0].keys()) - set(pilots_keys)

data: dict = {key: value for key, value in data.items() if key in starship_keys}

for pilot in data['pilots']:
    for key in pilots_keys_for_del:
        pilot.pop(key, None)
    pilot['homeworld_name'] = json.loads(requests.get(pilot['homeworld']).text)['name']

starship_str: str = f'''
Название коробля: {data['name']}
Максимальная скорость: {data['max_atmosphering_speed']}
Класс: {data['starship_class']}
Пилоты:'''

pilots_str: str = ''.join([f'''
     {index + 1}. Имя: {pilot['name']}
        Рост: {pilot['height']}
        Вес: {pilot['mass']}
        Родная планета: {pilot['homeworld_name']}
        Cсылка на информацию о родной планете: {pilot['homeworld']}''' for index, pilot in enumerate(data['pilots'])])

total_str: str = f'{starship_str}{pilots_str}'

with open('stars_wars.json', 'w') as file:
    json.dump(data, file, indent=4)

print(total_str)

