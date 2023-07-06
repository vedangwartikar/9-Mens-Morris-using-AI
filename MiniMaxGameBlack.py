import argparse
import math

from utils import Board, StaticEstimation, Debug, Black

class MiniMaxGameBlack:
    def __init__(self):
        self.positions_evaulated = 0
        self.minimax_estimate = 0

        self.board_obj = Board()
        self.static_estimation_obj = StaticEstimation()
        self.black = Black()

    def MaxMin(self, board, depth):
        """
        MaxMin function for MiniMax algorithm for midgame and endgame phase for black player
        """
        minmax = maxmin = ''
        if depth:
            v = -math.inf
            depth -= 1
            for possible_move in self.board_obj.generate_moves_midgame_endgame(board):
                minmax = self.MinMax(possible_move, depth)
                static_estimate = self.static_estimation_obj.static_estimation_midgame_endgame(minmax)
                self.positions_evaulated += 1
                if v < static_estimate:
                    v = static_estimate
                    self.minimax_estimate = v
                    maxmin = possible_move
            return maxmin
        return board

    def MinMax(self, board, depth):
        """
        MinMax function for MiniMax algorithm for midgame and endgame phase for black player
        """
        minmax = maxmin = ''
        if depth:
            v = math.inf
            depth -= 1
            for possible_move in self.black.generate_black_moves_midgame_endgame(board):
                maxmin = self.MaxMin(possible_move, depth)
                static_estimate = self.static_estimation_obj.static_estimation_midgame_endgame(maxmin)
                self.positions_evaulated += 1
                if v > static_estimate:
                    v = static_estimate
                    minmax = possible_move
            return minmax
        return board

if __name__ == '__main__':

    # Parse the command line arguments using argparse module
    parser = argparse.ArgumentParser(description = 'Generates the next move for White player using MiniMax algorithm')
    parser.add_argument('input_file', type=str, metavar='board1.txt', help='Input File Name')
    parser.add_argument('output_file', type=str, metavar='board2.txt', help='Output File Name')
    parser.add_argument('depth', type=int, metavar='depth', help='Depth of the search tree')
    parser.add_argument('--print_board', type=bool, action='store', const=True, nargs='?', metavar='print_board', help='Print the board')
    args = parser.parse_args()

    input_file, output_file, depth = args.input_file, args.output_file, args.depth
    
    debug = Debug()

    try:
        with open(input_file, 'r') as f:
            board = f.readline().strip()
        board_positions = len(board)
        if board_positions != 21:
            print(f'The input board (board1.txt) has { board_positions } positions. The correct positions should be 21.')
            exit(1)
        
        minimaxgameblack = MiniMaxGameBlack()
        black = Black()

        input_board_swap = black.board_swapper(board)
        play_intermediate_for_white = minimaxgameblack.MaxMin(input_board_swap, depth)
        output_board = black.board_swapper(play_intermediate_for_white)

        # Print the board if the debug flag parameter is set
        if args.print_board:
            print(f'Input Board:\n{ debug.draw(board) }')
            print(f'Output Board:\n{ debug.draw(output_board) }')

        print(f'Board Position: { output_board }.')
        print(f'Positions evaluated by static estimation: { minimaxgameblack.positions_evaulated }.')
        print(f'MINIMAX estimate: { minimaxgameblack.minimax_estimate }.')

        with open(output_file, 'w+') as f:
            f.write(output_board)
    except FileNotFoundError as err:
        print(err)
        exit(1)

