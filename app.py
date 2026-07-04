from flask import Flask, render_template, request
import requests

app = Flask(__name__)
URL = "https://pokeapi.co/api/v2/pokemon"

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon_data = None
    error = None
    if request.method == "POST":
        pokemon = request.form["pokemon"].lower()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if response.status_code == 200:
            datos = response.json()
            print("Datos recibidos:", datos)  # Agrega esta línea para depuración
            pokemon_data = {
                "name": datos["name"],
                "image" : datos["sprites"]["front_default"],
                "moves": [move["move"]["name"] for move in datos["moves"]],
                "types": [type["type"]["name"] for type in datos["types"][:20]],
            }
        else:
            pokemon_data = {"error": "Pokémon not found."}
    return render_template("index.html", pokemon=pokemon_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)