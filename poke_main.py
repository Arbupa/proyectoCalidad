from getpass import getpass
from os import system, name

import const
from PokeApi import PokeApi
from domainInsercion import insertarDatos
from pokemon import pokebase
from team import teambase
from entrenador import entrenadorbase

def opening_screen():
    
    def clear(): 
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear') 

    clear()
    with open("pokemon_logoTB.txt") as reader:
        content = reader.read()
        print(content)

def efectoOpcionesEntrenador():
    opening_screen()
    opcionesEntrenador()

def efectoOpcionesEquipo():
    opening_screen()
    opcionesEquipo()


def insertarPokemon(datos: list):
    pass

def insercionPokemon():
    pass

def listarEquipos():
    getdatos = insertarDatos()
    getdatos.read_team_list(const.Entrenador.entrenadorId)
    opening_screen()
    efectoOpcionesEntrenador()

def listarPokemonDisponibles():
    pokeapi =  PokeApi()
    pokeapi.write_pokemon_list(const.Equipo.generacion)
    pokeapi.list_pokemon()
    efectoOpcionesEquipo()

def verEquipoActual():
    pass

def agregarPokemon():
    pass

def eliminarPokemon():
    pass

def guardarEquipo():
    pass

def verEquipo():
    pass

def crearEquipo():
    def registrarEquipo(equipo):
        try:
            guardar = insertarDatos()
            guardar.insert_team_data(equipo)
            return True
        except:
            #LogError()
            return False
    
    equipo = teambase()
    equipo.nombre = input("Nombre del equipo: ")
    equipo.generacion = int(input("Numero de generacion: "))

    if registrarEquipo(equipo): 
        opening_screen()
        const.Equipo = equipo
        # print(f'Equipo {equipo.nombre} creado')
        opcionesEquipo()
    else:
        opening_screen() 
        print("Error al registrar equipo")
        opcionesEntrenador()


def iniciarSesion():
    def validar(entrenador):
        getdatos = insertarDatos()
        
        return getdatos.get_entrenador_data(entrenador)

    entrenador = entrenadorbase()
    entrenador.nombre = input("Entrenador: ")
    entrenador.password = getpass("Password: ")

    if validar(entrenador):
        const.Entrenador = entrenador
        opening_screen()
        opcionesEntrenador()
    else:
        opening_screen()
        print("Credenciales Invalidas\n")
        opcionesInicio()

def registrarUsuario():
    def registrar(entrenador):
        try:
            guardar = insertarDatos()
            guardar.insert_entrenador_data(entrenador)
            return True
        except:
            #LogError()
            return False

    entrenador = entrenadorbase()
    entrenador.nombre = input("Entrenador: ")
    entrenador.password = getpass("Password: ")

    if registrar(entrenador): 
        opening_screen()
        print('Se registro al entrenador de manera exitosa')
    else:
        opening_screen() 
        print("Error al registrar")

    opcionesInicio()

def opcionesEquipo():

    print(f"Entrenador@: {const.Entrenador.nombre}")
    print(f"Equipo: {const.Equipo.equipoId} {const.Equipo.equiponombre}")

    opciones = {1: listarPokemonDisponibles,
                2: verEquipoActual,
                3: agregarPokemon,
                4: eliminarPokemon,
                5: guardarEquipo,
                0: efectoOpcionesEntrenador}

    print(const.MENU_EQUIPO)
    opcion = int(input())

    respuesta = opciones.get(opcion, 
                            opcionesEntrenador
                            )
    respuesta()

def opcionesEntrenador():

    print(f"Entrenador@: {const.Entrenador.nombre}")
    opciones = {1: listarEquipos,
                2: verEquipo,
                3: crearEquipo,
                0: main}

    print(const.MENU_ENTRENADOR)
    opcion = int(input())

    respuesta = opciones.get(opcion, 
                            opcionesEntrenador
                            )
    respuesta()
            
def opcionesInicio():
    opciones = {1: iniciarSesion,
                2: registrarUsuario,
                0: exit}

    print(const.MENU_INICIAL)
    opcion = int(input())

    respuesta = opciones.get(opcion, 
                            main
                            )
    respuesta()
            

def main():
    opening_screen()
    opcionesInicio()

if __name__ == "__main__":
    main()  