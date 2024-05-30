from Board import Board


board = Board(10)
board.print_board()
for _ in range(50):
    board.progress()
