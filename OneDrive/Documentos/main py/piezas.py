'''class zonaJuego():
    def __init__(self):
        self.piezas=[
            ['tN','cN','aN','rN','reyN','aN','cN','tN'],
            ['pN','pN','pN','pN','pN','pN','pN','pN'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--']
            ['pB','pB','pB','pB','pB','pB','pB','pB'],
            ['tB','cB','aB','rB','reyB','aB','cB','tB']
        ]'''
class ChessBoard:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
    
    def print_board(self):
        for row in self.board:
            print(' '.join(row))
    
    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = ' '
        self.board[end_row][end_col] = piece
    
    def is_valid_move(self, start_pos, end_pos):
        # Implement your own logic for validating moves
        return True

# Example usage:
board = ChessBoard()
board.print_board()

# Move a piece
start_pos = (1, 0)
end_pos = (3, 0)
if board.is_valid_move(start_pos, end_pos):
    board.move_piece(start_pos, end_pos)
    print("\nAfter moving a piece:")
    board.print_board()
else:
    print("Invalid move.")