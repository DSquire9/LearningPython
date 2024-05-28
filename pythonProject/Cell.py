
class Cell:

    def __init__(self, is_alive, faction):
        self.is_alive = is_alive
        self.faction = faction

    def to_str(self):
        if self.is_alive:
            return str(self.faction)
        else:
            return "0"
