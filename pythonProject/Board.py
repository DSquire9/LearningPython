from Cell import Cell
import random

random.seed()


class Board:
    def __init__(self, size):
        self.size = size
        # note: [row][column]
        self.grid = []
        self.previous = []
        for row in range(self.size):
            r = []
            for column in range(self.size):
                # if random.randint(0, 1) == 0:
                #     r.append(Cell(True, random.choice([1, 2, 3, 4])))
                # else:
                #     r.append(Cell(False, random.choice([1, 2, 3, 4])))
                if random.randint(0, 1) == 0:
                    r.append(Cell(True, 1))
                else:
                    r.append(Cell(False, 1))
            self.grid.append(r)

    def print_board(self):
        result = ""
        for row in self.grid:
            for column in row:
                result += column.to_str()

            result += "\n"

        print(result)

    def progress(self):
        self.previous = self.grid.copy()
        new_grid = []
        for row in range(self.size):
            r = []
            for column in range(self.size):
                count = 0
                if row == 0:
                    if column == 0:
                        if self.previous[row + 1][column].is_alive:
                            count += 1
                        if self.previous[row][column + 1].is_alive:
                            count += 1
                        if self.previous[row + 1][column + 1].is_alive:
                            count += 1
                    elif column == self.size - 1:
                        if self.previous[row + 1][column].is_alive:
                            count += 1
                        if self.previous[row][column - 1].is_alive:
                            count += 1
                        if self.previous[row + 1][column - 1].is_alive:
                            count += 1
                    else:
                        if self.previous[row + 1][column].is_alive:
                            count += 1
                        if self.previous[row][column + 1].is_alive:
                            count += 1
                        if self.previous[row + 1][column + 1].is_alive:
                            count += 1
                        if self.previous[row][column - 1].is_alive:
                            count += 1
                        if self.previous[row + 1][column - 1].is_alive:
                            count += 1
                elif row == self.size - 1:
                    if column == 0:
                        if self.previous[row - 1][column].is_alive:
                            count += 1
                        if self.previous[row - 1][column + 1].is_alive:
                            count += 1
                        if self.previous[row][column + 1].is_alive:
                            count += 1
                    elif column == self.size - 1:
                        if self.previous[row - 1][column].is_alive:
                            count += 1
                        if self.previous[row - 1][column - 1].is_alive:
                            count += 1
                        if self.previous[row][column - 1].is_alive:
                            count += 1
                    else:
                        if self.previous[row - 1][column].is_alive:
                            count += 1
                        if self.previous[row - 1][column + 1].is_alive:
                            count += 1
                        if self.previous[row][column + 1].is_alive:
                            count += 1
                        if self.previous[row - 1][column - 1].is_alive:
                            count += 1
                        if self.previous[row][column - 1].is_alive:
                            count += 1
                elif column == 0:
                    if self.previous[row - 1][column].is_alive:
                        count += 1
                    if self.previous[row + 1][column].is_alive:
                        count += 1
                    if self.previous[row - 1][column + 1].is_alive:
                        count += 1
                    if self.previous[row + 1][column + 1].is_alive:
                        count += 1
                    if self.previous[row][column + 1].is_alive:
                        count += 1
                elif column == self.size - 1:
                    if self.previous[row - 1][column].is_alive:
                        count += 1
                    if self.previous[row + 1][column].is_alive:
                        count += 1
                    if self.previous[row - 1][column - 1].is_alive:
                        count += 1
                    if self.previous[row + 1][column - 1].is_alive:
                        count += 1
                    if self.previous[row][column - 1].is_alive:
                        count += 1
                else:
                    if self.previous[row - 1][column - 1].is_alive:
                        count += 1
                    if self.previous[row - 1][column].is_alive:
                        count += 1
                    if self.previous[row - 1][column + 1].is_alive:
                        count += 1
                    if self.previous[row][column - 1].is_alive:
                        count += 1
                    if self.previous[row][column + 1].is_alive:
                        count += 1
                    if self.previous[row + 1][column - 1].is_alive:
                        count += 1
                    if self.previous[row + 1][column].is_alive:
                        count += 1
                    if self.previous[row + 1][column + 1].is_alive:
                        count += 1
                if count < 2 and self.previous[row][column].is_alive:
                    r.append(Cell(False, self.previous[row][column].faction))
                elif count < 4 and self.previous[row][column].is_alive:
                    r.append(Cell(True, self.previous[row][column].faction))
                elif count > 3 and self.previous[row][column].is_alive:
                    r.append(Cell(False, self.previous[row][column].faction))
                elif count == 3 and not self.previous[row][column].is_alive:
                    r.append(Cell(True, self.previous[row][column].faction))
                else:
                    r.append(Cell(False, self.previous[row][column].faction))
            new_grid.append(r)
        self.grid = new_grid
        self.print_board()
        # previous_board = ""
        # for row in self.previous:
        #     for column in row:
        #         previous_board += column.to_str()
        #
        #     previous_board += "\n"
        #
        # print(previous_board)
