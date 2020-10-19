from random import uniform
from math import floor
from Movimiento import Move

class Pokemon:

    moves = set()   # Es un set por que no puede haber movimientos repetidos en un mismo pokemon
    stats = {"HP": 0,
             "Attack": 0,
             "Defense": 0,
             "Sp. Attack": 0,
             "Sp. Defense": 0,
             "Speed": 0,
            }

    def __init__(self, **kwargs):
        self.pokemon_id = kwargs.get("pokemon_id", -1)
        self.pokedex_id = kwargs.get("pokedex_id", -1)
        self.name = kwargs.get("pokemon_name", "") #Quiero que el nombre default del pokemon sea la especie, pero aun no se como
        self.tipo = kwargs.get("type", "???") #??? es como sale en los juegos cuando es un pokemon "especial" jsjjs
        self.habilidad = kwargs.get("abillity", None) #Quiero que la habilidad default sea la habilidad default del pokemon, pero aun no se como
        self.nature = kwargs.get("nature", "Bashful") #Puse Bashful por default por que Bashful no tiene efecto en los stats
        
        ##los ivs solo pueden ser de 0 a 31 por cada stat, con un minimo total de 0 y un maximo total de 186. 
        # En los juegos se determinan al azar al momento de captura y no son modificables. 
        # Aqui va a haber una funcion opcional para settearlos, de asi quererlo
        self.ivs = [floor(uniform(0,31)) for i in range(6)]

        # Un pokemon puede tener un total de 510 evs, pero solo puede haber un maximo de 252 Evs por stat
        # En los juegos se van modificando dependiendo de los enemigos que combatas
        # Aqui va a haber una funcion opcional para settearlos, de asi quererlo
        self.evs = [0 for i in range(6)]

    def add_move(self, movimiento: Move):
            if not movimiento.is_learnable_by(self.pokedex_id):
                return f"{self.name} no puede aprender {movimiento.name}"
            
            self.moves.add(movimiento)
            
            return f"{movimiento.name} aprendido!"

    def remove_move(self, movimiento: Move):
            pass

    def set_evs(self, evs: list):
            pass

    def set_ivs(self, ivs: list):
            pass