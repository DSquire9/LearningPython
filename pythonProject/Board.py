from Cell import Cell
import random

random.seed()


class Board:
    def __init__(self, size):
        self.size = size
        # note: [row][column]
        self.grid = []
        for row in range(size):
            r = []
            for column in range(size):
                if random.randint(0, 1) == 0:
                    r.append(Cell(True, random.choice([1, 2, 3, 4])))
                else:
                    r.append(Cell(False, random.choice([1, 2, 3, 4])))
            self.grid.append(r)

    def print_board(self):
        result = ""
        for row in self.grid:
            for column in row:
                result += column.to_str()

            result += "\n"

        print(result)
