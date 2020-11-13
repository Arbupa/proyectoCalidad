from firebase import firebase
from pokemon import pokebase
from entrenador import entrenadorbase
from team import teambase


class DataBaseInteract():
    def write_team_list(self, entrenadorId: int):
        #cosas firebosas xdd
        
        pass

    def insertTeam(self,teambase):
        pass

    def insertPokemon(self,pokebase):
        Frbs=firebase.FirebaseApplication("https://pokemon-9f0ea.firebaseio.com/",None)
        
        
        datos={
            "nombre":listapoke[1],
            "HP":listapoke[2],
            "ATK":listapoke[3],
            "DEF":listapoke[4]
        }
        guardar=Frbs.post('/testDatos/pokemon2',datos)
        pass

    def insertEntrenador(self,entrenadorbase):
        Frbs=firebase.FirebaseApplication("https://pokemon-9f0ea.firebaseio.com/",None)
        datos={
            "nombre":entrenadorbase.nombre,
            "password":entrenadorbase.password,
            "equipos":entrenadorbase.equipos
        }
        guardar=Frbs.post('/pokemonbuilder/',datos)

    def getTeam(self,teambase):
        pass

    def getEntrenador(self,entrenadorbase):
        Frbs=firebase.FirebaseApplication("https://pokemon-9f0ea.firebaseio.com/",None)
        leer=Frbs.get('/pokemonbuilder/','')
        return leer

    def getPokemonData(self,pokebase):
        pass