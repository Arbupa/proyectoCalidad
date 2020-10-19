from equipo import PokemonTeam
from pokemon import Pokemon
from Movimiento import Move

class TeamBuilder():
    
    def __init__(self, **kwargs):
        self.equipo = PokemonTeam(**kwargs)

    def add_pokemon(self, pokemon: Pokemon):
        self.equipo.add_pokemon_to_team(Pokemon)

    def add_move(self, pokemon_number: int, move: Move):
        self.equipo.pokemon_team[pokemon_number].add_move(move)

    def build_team(self):
        return self.equipo
