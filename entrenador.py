from team import teambase

class entrenadorbase:
    def __init__(self, nombre = "", password = "", equipos = []):
        self.entrenadorId = -1

        self.nombre = nombre
        self.password = password
        self.equipos = equipos
        