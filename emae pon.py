import requests

url = 'https://swapi.dev/api'
responce = requests.get(url).json()

starship_api = responce.get('starships')


def check_starship(url):
    starships = []
    for i in range(1, 6):
        responce = requests.get(f'{url}/{i}').json()
        starships.append({responce.get('name'): responce.get('max_atmosphering_speed')})
    print(starships)


check_starship(starship_api)

max_speed = 0
fastest_ship = ""

for starship_first in starship_api:
    speed = responce.get('max_atmosphering_speed')
    if speed == "unknown":
        continue
    speed1=int(speed)
    if speed1 > max_speed:
        max_speed = speed1
        fastest_ship = responce.get("name")

print("The fastest ship is:", fastest_ship)