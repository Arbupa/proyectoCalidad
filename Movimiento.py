class Move:
    
    def __init__(self, **kwargs):
        self.move_id = kwargs.get("move_id", -1)
        self.name = ""

    def fill_move_information(self):
        pass

    def learned_by(self) -> list:
        pass

    def is_learnable_by(self, pokedex_id: int) -> bool:
        pass