import requests
base_url = "https://pokeapi.co/api/v2/pokemon/"
def get_pokemon(pokemon_name):
    response = requests.get(base_url + pokemon_name)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos de {pokemon_name}. Status code: {response.status_code}")
        return None 
pokemon_name = "pikachu"
pokemon_data = get_pokemon(pokemon_name)
if pokemon_data:
    print(f"Nombre: {pokemon_data['name']}")
    print(f"Altura: {pokemon_data['height']}")
    print(f"Peso: {pokemon_data['weight']}")
    print("Habilidades:")
    for ability in pokemon_data['abilities']:
        print(f"- {ability['ability']['name']}")
else:
    print("No se pudo obtener la información del Pokémon.")
    