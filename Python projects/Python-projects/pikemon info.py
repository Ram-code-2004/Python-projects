import requests
base_url ="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data =response.json()
        return data
    else:
        print("failed to retrive data")

    

pokemon_name = input("Enter the name of the Pokémon: ").lower()   
pokemon_info =get_pokemon_info(pokemon_name)
if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"id: {pokemon_info['id']}")
    print("Abilities:")
    for ability in pokemon_info['abilities']:
        print(f"- {ability['ability']['name']}")