import subprocess

from storageInterface import IStorage
from baseConection import DataBaseInteract
from team import teambase
from pokemon import pokebase
from entrenador import entrenadorbase

class insertarDatos(IStorage):

    def insert_team_data(self,teambase):
        base=DataBaseInteract()
        base.insertTeam(teambase)
    
    def insert_pokemon_data(self,pokebase):
        base=DataBaseInteract()
        base.insertPokemon(pokebase)

    def get_team_data(self,teambase):
        base=DataBaseInteract()
        base.getTeam(teambase)

    def get_pokemon_data(self,pokebase):
        base=DataBaseInteract()
        base.getPokemonData(pokebase)

    def insert_entrenador_data(self,entrenadorbase):
        base=DataBaseInteract()
        base.insertEntrenador(entrenadorbase)


    def read_team_list(self, entrenadorId: int):
        base=DataBaseInteract()
        base.write_team_list(entrenadorbase)

        subprocess.run("less teams_list.txt", shell = True)

    def get_entrenador_data(self,entrenadorbase):
        base=DataBaseInteract()
        llave=False
        valor=False

        entrenadores=base.getEntrenador(entrenadorbase)
        # print(entrenadores)
        for _,v in entrenadores.items():
            for kk,vv in v.items():
                if kk=='nombre':
                    if vv==entrenadorbase.nombre:
                        llave=True
                if kk=='password':
                    if vv==entrenadorbase.password:
                        valor=True
            if llave==True and valor==True:
                 break
            else:
                llave=False
                valor=False
        
        if llave==True and valor==True:
            return True

        
    