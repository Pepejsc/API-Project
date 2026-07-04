import requests

URL = "https://pokeapi.co/api/v2/pokemon"

pokemon = input("Ingresa el nombre de un pokemon: ")

request = requests.get(URL + "/" + pokemon)

datos = request.json()

for move in datos["moves"]:
    print(move["move"]["name"])



