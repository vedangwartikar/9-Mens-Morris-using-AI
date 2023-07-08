import argparse
import math

from utils import Board, StaticEstimation, Debug, Black


class MiniMaxOpening:
    def __init__(self):
        self.positions_evaulated = 0
        self.minimax_estimate = 0

        self.board_obj = Board()
        self.static_estimation_obj = StaticEstimation()
        self.black = Black()

        self.final_board = ''

    def MaxMin(self, board, depth):
        """
        MaxMin function for MiniMax algorithm for opening game
        """
        # print('yo')
        if depth:
            v = -math.inf
            # depth -= 1
            for possible_move in self.board_obj.generate_moves_opening(board):
                minmax_estimate = self.MinMax(possible_move, depth - 1)
                if v < minmax_estimate:
                    v = minmax_estimate
                    # print('inside yo')
                    self.final_board = possible_move
            return v
        self.positions_evaulated += 1
        return self.static_estimation_obj.static_estimation_opening(board)

    def MinMax(self, board, depth):
        """
        MinMax function for MiniMax algorithm for opening game
        """
        # print('not yo')
        if depth:
            v = math.inf
            # depth -= 1
            for possible_move in self.black.generate_black_moves_opening(board):
                maxmin_estimate = self.MaxMin(possible_move, depth - 1)
                if v > maxmin_estimate:
                    v = maxmin_estimate
                    # print('inside not yo')
                    # self.final_board = possible_move
            return v
        self.positions_evaulated += 1
        return self.static_estimation_obj.static_estimation_opening(board)

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
        
        minimaxopening = MiniMaxOpening()
        minimaxopening.minimax_estimate = minimaxopening.MaxMin(board, depth)
        output_board = minimaxopening.final_board

        # Print the board if the debug flag parameter is set
        if args.print_board:
            print(f'Input Board:\n{ debug.draw(board) }')
            print(f'Output Board:\n{ debug.draw(output_board) }')

        print(f'Board Position: { output_board }.')
        print(f'Positions evaluated by static estimation: { minimaxopening.positions_evaulated }.')
        print(f'MINIMAX estimate: { minimaxopening.minimax_estimate }.')

        with open(output_file, 'w+') as f:
            f.write(output_board)
    except FileNotFoundError as err:
        print(err)
        exit(1)

