import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        'name': 'bulbasaur',
        'height': 7,
        'weight': 69,
        'types': ['grass', 'poison']
    }

pokemon = getPoke("Bulbasaur")
print(pokemon)