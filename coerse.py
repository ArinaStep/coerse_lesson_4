import requests
from bs4 import BeautifulSoup
from datetime import datetime

url='http://www.cbr.ru/scripts/XML_daily.asp?'

today=datetime.today()
today=today.strftime('%d/%m/%Y')
payload={'date_req':today}

responce=requests.get(url,params=payload)
xml=BeautifulSoup(responce.content,features='xml')

def getCourse(id):
    return str(xml.find('Valute',{'ID':id}).Value.text)


url1 = 'https://swapi.dev/api'
responce = requests.get(url1).json()

planets_api = responce.get('planets')

def maxRadius_of_Planets(url1):
    planets = []
    for i in range(1, 6):
        responce = requests.get(f'{url1}/{i}').json()
        planets.append({responce.get('name'): responce.get('max_diameters_of_planet')})
    print(planets)



max_diameter = 0
fastest_ship = ""

for starship_first in planets_api:
    diameter = responce.get('diameter')
    if diameter == "unknown":
        continue
    diameter1 = int(diameter)
    if diameter1 > max_diameter:
        max_speed = diameter1
        max_diameter = responce.get("name")

print("The biggest diameter in all planets have :", max_diameter)

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