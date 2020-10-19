from abc import ABC, abstractmethod

class InterfaceStorage(ABC):

    @abstractmethod
    def insert_team_data(self):
        pass

    @abstractmethod
    def insert_pokemon_data(self):
        pass

    @abstractmethod
    def get_team_data(self):
        pass