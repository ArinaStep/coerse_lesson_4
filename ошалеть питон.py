import requests

url='https://swapi.dev/api'
responce=requests.get(url).json()

planets_api=responce.get('planets')
people_api=responce.get('people')
starship_api=responce.get('starships')
def check_starship(url):
    starships=[]
    for i in range(1,6):
        responce = requests.get(f'{url}/{i}').json()
        starships.append({responce.get('name'): responce.get('max_atmosphering_speed')})
    print(starships)
check_starship(starship_api)

def check_plenets(url):
    diametr_list=[]
    for i in range(1,6):
        responce = requests.get(f'{url}/{i}').json()
        diametr_list.append({responce.get('name'): responce.get('diametr')})
    print(diametr_list)
check_plenets(planets_api)

def check_people(url):
    peopls=[]
    for i in range(1,6):
        responce = requests.get(f'{url}/{i}').json()
        peopls.append({responce.get('name'): responce.get('birth_year')})
    print(peopls)
check_people(people_api)