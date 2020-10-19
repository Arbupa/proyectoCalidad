from pokemon import Pokemon

class PokemonTeam:

    def __init__(self, **kwargs):
        self.__equipo_id = kwargs.get("equipo_id", -1)
        self.__nombre_equipo = kwargs.get("nombre_equipo", "Equipo sin titulo")
        self.__nombre_entrenador = kwargs.get("nombre_entrenador", "Entrenador(a)")
        self.pokemon_team = kwargs.get("pokemon_team", [])

        self.__datos = kwargs

    def remove_pokemon_from_team(self, pokemon_number: int) -> str:
        """ Elimina el pokemon numero x del equipo. pokemon_number: int --> Pokemon (pokemon eliminado)"""
        
        if len(self.pokemon_team) == 0:
            print("No se puede eliminar pokemon; Equipo vacio")
            return []

        return self.pokemon_team.pop(f"pokemon_{pokemon_number}", "El pokemon no estaba en el equipo")

    def add_pokemon_to_team(self, pokemon: Pokemon):
        """ Agrega pokemon al equipo.  pokemon: Pokemon --> str"""
    
        if len(self.pokemon_team) == 6:
            print("Equipo maximo de 6 pokemon")
            return 

        new_pokemon = f"pokemon_{len(self.pokemon_team) +1}"
        self.pokemon_team[new_pokemon] = pokemon

    def informacion_equipo(self) -> None:
        """ Metodo para imprimir informacion del equipo creado. no input --> None """

        print(f"{'#'*5} DATOS EQUIPO {'#'*5}")
        for k,v in self.__datos.items():
            if k != "pokemon_team":
                print(f"{k.upper()} : {v}")

        print(f"\t{'#'*3} POKEMON EN EQUIPO {'#'*3}")
        for i in self.pokemon_team.keys():
            print(f"\n\t\t{i.replace().upper()}:")
            for k,v in i.items():
                print( f"\t\t\t{k.replace().upper()}: {v}")

    ###Setters y getters
    @property
    def nombre_equipo(self):
        self.__nombre_equipo
    
    @nombre_equipo.setter
    def nombre_equipo(self, new_nombre):
        self.__nombre_equipo = new_nombre
    
    @property
    def nombre_entrenador(self):
        self.__nombre_entrenador
    
    @nombre_entrenador.setter
    def nombre_entrenador(self, new_nombre):
        self.__nombre_equipo = new_nombre
    