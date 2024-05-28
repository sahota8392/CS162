# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 8/11/23
# Description: Create a variant of chess with the provided rules for the pieces and starting position

import matplotlib.pyplot as plt
import numpy as np  # import numpy to use algebraic notation for chess board
from matplotlib.colors import ListedColormap


class ChessVar:
    def __init__(self):
        """
        Initialize following:
            player turn set to White
            game status set to Unfinished
            player turn count to 0
            board position set for white and black pieces
            white and black captured pieces to empty list
        """
        self._player_turn = 'White'
        self._game_status = 'UNFINISHED'
        self._turn_count = 0
        self._board = [
            ['', '', '', '', '', '', '', ''],  # row 8
            ['', '', '', '', '', '', '', ''],  # row 7
            ['', '', '', '', '', '', '', ''],  # row 6
            ['', '', '', '', '', '', '', ''],  # row 5
            ['', '', '', '', '', '', '', ''],  # row 4
            ['', '', '', '', '', '', '', ''],  # row 3
            ['', '', '', '', '', '', '', ''],  # row 2
            ['', '', '', '', '', '', '', ''],  # row 1
        ]
        self._captured_pieces_white = []
        self._captured_pieces_black = []

        # set initial location of pieces on the board (lowercase = white, uppercase = black)
        self._board[6][0] = 'r'  # White Rook
        self._board[7][0] = 'k'  # White King
        self._board[7][1] = 'b'  # White Bishop
        self._board[6][1] = 'b'  # White Bishop
        self._board[7][2] = 'n'  # White Knight
        self._board[6][2] = 'n'  # White Knight

        self._board[6][7] = 'R'  # Black Rook
        self._board[7][7] = 'K'  # Black King
        self._board[7][6] = 'B'  # Black Bishop
        self._board[6][6] = 'B'  # Black Bishop
        self._board[7][5] = 'N'  # Black Knight
        self._board[6][5] = 'N'  # Black Knight

    def get_game_state(self):
        """Return 1 of 4 game results based on outcome:
            'UNFINISHED' - if King piece of player reaches row 8, other player has one move still
            'WHITE_WON' - white King has reached row 8 and black king did not reach row 8 in next move
            'BLACK_WON' - black King has reached row 8 and white king did not reach row 8 in next move
            'TIE' - first player King reached row 8 and other player also reached row 8 or neither could
        """
        if self._game_status == 'UNFINISHED':
            white_won = any(piece == 'k' for piece in self._board[0])
            black_won = any(piece == 'K' for piece in self._board[0])

            # if white king reaches row 8, black has 1 turn to tie else white wins
            if white_won and not black_won and self._player_turn == 'Black':
                self._game_status = 'WHITE_WON'

            # if black reaches row 8, black wins, no turns for white
            if black_won and not white_won:
                self._game_status = 'BLACK_WON'

            # Black ties
            elif white_won and black_won:
                self._game_status = 'TIE'

        return self._game_status

    def valid_moves(self, from_row, from_col, to_row, to_col):
        """Check if the move for the appropriate piece is a valid move upon their limitation"""
        piece = self._board[from_row][from_col]  # define piece
        piece_to = self._board[to_row][to_col]

        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # define pieces
        knight = piece.lower() == 'n' or piece.upper() == 'N'
        bishop = piece.lower() == 'b' or piece.upper() == 'B'
        rook = piece.lower() == 'r' or piece.upper() == 'R'
        king = piece.lower() == 'k' or piece.upper() == 'K'

        # Moves allowed for each piece
        if knight:  # Knight can jump pieces but if ending square is King, it can not execute move
            if piece.isupper() and piece_to.isupper():
                return False
            if piece.islower() and piece_to.islower():
                return False
            return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

        if bishop:
            if piece.isupper() and piece_to.isupper():
                return False
            if piece.islower() and piece_to.islower():
                return False

            if row_diff != col_diff:  # check if move is diagonal else False
                return False

            row_direction = 1 if to_row > from_row else -1  # directions of row/col
            col_direction = 1 if to_col > from_col else -1

            row = from_row + row_direction
            col = from_col + col_direction

            while row != to_row and col != to_col:  # if there is a piece in path return False
                if self._board[row][col] != '':
                    return False
                row += row_direction
                col += col_direction

            return row_diff == col_diff

        if rook:  # Rook can not move to a square occupied by own player
            if from_row == to_row:  # Row
                min_col = min(from_col, to_col)
                max_col = max(from_col, to_col)
                for col in range(min_col + 1, max_col):
                    if self._board[from_row][col] != '':
                        return False

            if from_col == to_col:  # Column
                min_row = min(from_row, to_row)
                max_row = max(from_row, to_row)
                for row in range(min_row + 1, max_row):
                    if self._board[row][from_col] != '':
                        return False

            # Stops from capturing own player piece
            if piece.isupper() and piece_to.isupper():
                return False
            if piece.islower() and piece_to.islower():
                return False

            return from_row == to_row or from_col == to_col

        if king:  # King can not move to square occupied by own player
            if piece.isupper() and piece_to.isupper():
                return False
            if piece.islower() and piece_to.islower():
                return False
            return row_diff == 1 or col_diff == 1

    def make_move(self, move_from, move_to):
        """
        2 parameters - strings of square moved from and square moved to
        Return False if move_from square has no piece belonging to player or not a legal move or game won
        Return True if it's a valid move - remove any captured piece, update game status, update turn status
        """
        # break move_from by index per row and column and move to desired square based on index
        from_row, from_col = 8 - int(move_from[1]), ord(move_from[0]) - ord('a')
        to_row, to_col = 8 - int(move_to[1]), ord(move_to[0]) - ord('a')

        piece = self._board[from_row][from_col]  # defines piece that will be referenced
        capture_piece = self._board[to_row][to_col]  # piece that will be captured by opponent

        if self._player_turn == 'White':  # if it's white player turn based on chess piece lowercase, else go to Black
            if piece.islower():
                if self.valid_moves(from_row, from_col, to_row, to_col):  # check piece makes valid move
                    self._board[from_row][from_col] = ''  # set the move from square to empty string
                    self._board[to_row][to_col] = piece  # piece being moved to splitting row-col

                    if capture_piece and capture_piece.upper() != 'K':  # if white captures black piece exclude King
                        if capture_piece.isupper():
                            self._captured_pieces_black.append(capture_piece)  # append to black captured list
                            self._board[to_row][to_col] = ''  # remove from the self.board
                    self._board[to_row][to_col] = piece

                    self._turn_count += 1  # increment turn count for user purpose
                    print('Turn', self._turn_count,
                          'Player:', self._player_turn,
                          'Winner:', self.get_game_state(),
                          'Black Captured', self._captured_pieces_black)
                    self._player_turn = 'Black'  # after move is made, it's the next players turn
                    return True
        else:
            if piece.isupper():
                if self.valid_moves(from_row, from_col, to_row, to_col):
                    self._board[from_row][from_col] = ''
                    self._board[to_row][to_col] = piece

                    if capture_piece and capture_piece.lower() != 'k':
                        if capture_piece.islower():
                            self._captured_pieces_white.append(capture_piece)
                            self._board[to_row][to_col] = ''
                    self._board[to_row][to_col] = piece
                    self._turn_count += 1
                    print('Turn', self._turn_count,
                          'Player:', self._player_turn,
                          'Winner:', self.get_game_state(),
                          'White Captured', self._captured_pieces_white)
                    self._player_turn = 'White'
                    return True
            return False


def display(chess_var):
    """Creates and displays the chess board for initial positioning and moving of pieces"""
    board = np.tile([1, 0], (8, 4))
    for i in range(board.shape[0]):
        board[i] = np.roll(board[i], i % 2)
    cmap = ListedColormap(['lightslategray', 'steelblue'])
    plt.matshow(board, cmap=cmap)

    # Label each square on the x and y axis
    plt.xticks(np.arange(8), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    plt.yticks(np.arange(8), ['8', '7', '6', '5', '4', '3', '2', '1'])

    # Label both sides for left-right and top-bottom
    plt.tick_params(axis='y', labelleft=True, labelright=True)
    plt.tick_params(axis='x', labeltop=True, labelbottom=True)

    # Display of pieces and color of text based on player
    start_position = chess_var._board
    for row in range(8):
        for col in range(8):
            piece = start_position[row][col]
            if piece != '':
                font_color = 'white' if piece.islower() else 'black'
                plt.text(col, row, piece, ha='center', va='center', fontsize=6, color=font_color)
    plt.show()


game = ChessVar()
t1 = game.make_move('c2', 'e3')
t2 = game.make_move('f1', 'e3')
t3 = game.make_move('b2', 'd4')
t4 = game.make_move('f2', 'd3')
t5 = game.make_move('d4', 'e3')
t6 = game.make_move('g1', 'e3')
t7 = game.make_move('a2', 'g2')
t8 = game.make_move('d3', 'c1')
t9 = game.make_move('g2', 'h2')
t10 = game.make_move('c1', 'a2')
t11 = game.make_move('b1', 'a2')
t12 = game.make_move('e3', 'f2')
t13 = game.make_move('h2', 'f2')
t14 = game.make_move('h1', 'g1')
t15 = game.make_move('a2', 'c4')
t16 = game.make_move('g1', 'f2')
t17 = game.make_move('c4', 'e2')
t18 = game.make_move('f2', 'e2')
t19 = game.make_move('a1', 'a2')
t20 = game.make_move('e2', 'e3')
t21 = game.make_move('a2', 'a3')
t22 = game.make_move('e3', 'e4')
t23 = game.make_move('a3', 'a4')
t24 = game.make_move('e4', 'e5')
t25 = game.make_move('a4', 'b5')
t26 = game.make_move('b5', 'c6')
t27 = game.make_move('e5', 'd6')
t28 = game.make_move('b5', 'c6')
t29 = game.make_move('d6', 'd7')
t30 = game.make_move('c6', 'c7')
t31 = game.make_move('d7', 'e7')
t32 = game.make_move('c7', 'c8')
t33 = game.make_move('e7', 'e8')

display(game)
state = game.get_game_state()
