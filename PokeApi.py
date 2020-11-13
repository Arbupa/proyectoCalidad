import requests
import subprocess
import json

class PokeApi():

    def write_pokemon_list(self, generation: int):
        total_pokemon_by_gen = [151, 251, 386, 493, 649, 721, 809, 898]
        pokeURL = "https://pokeapi.co/api/v2/pokemon?limit={}"

        r = requests.get(pokeURL.format(total_pokemon_by_gen[generation - 1]))
        data = r.json()

        with open("pokemon_list.txt", "w") as handle:
            i = 1
            for pokemon in data.get("results"):
                handle.write(f"{i} " + pokemon["name"] + "\n")
                i += 1

    def write_move_list(self, pokemon: int):
        pokeURL = "https://pokeapi.co/api/v2/pokemon/{}"

        r = requests.get(pokeURL.format(pokemon))
        data = r.json()

        with open("move_list.txt", "w") as handle:
            for i in data.get("moves"):
                handle.write(i["move"]["name"] + "\n")

    def list_pokemon(self):
        subprocess.run("less pokemon_list.txt", shell= True)

    def search_pokemon(self, to_search: str):
        command = f"less pokemon_list.txt | grep {to_search.lower()}"

        subprocess.run(command, shell= True)



####
api = PokeApi()
api.write_move_list(151)