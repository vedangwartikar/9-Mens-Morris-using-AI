import argparse
import math

from main import *

positions_evaulated = 0
minimax_estimate = 0

def MaxMin(board, depth):
    maxmin, minmax = list(), list()
    if depth:
        v = -math.inf
        depth -= 1
        for possible_move in generate_moves_opening(board):
            minmax = MinMax(possible_move, depth)
            static_estimate = static_estimation_opening(minmax)
            global positions_evaulated
            positions_evaulated += 1
            if v < static_estimate:
                v = static_estimate
                global minimax_estimate
                minimax_estimate = v
                maxmin = possible_move
        return maxmin
    return board

def MinMax(board, depth):
    minmax, maxmin = list(), list()
    if depth:
        v = math.inf
        depth -= 1
        for possible_move in generate_moves_opening(board):
            maxmin = MaxMin(possible_move, depth)
            static_estimate = static_estimation_opening(maxmin)
            global positions_evaulated
            positions_evaulated += 1
            if v > static_estimate:
                v = static_estimate
                minmax = possible_move
        return minmax
    return board

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Generates the next move for White player using MiniMax algorithm')
    parser.add_argument('input_file', type=str, metavar='board1.txt', help='Input File Name')
    parser.add_argument('output_file', type=str, metavar='board2.txt', help='Output File Name')
    parser.add_argument('depth', type=int, metavar='depth', help='Depth of the search tree')
    args = parser.parse_args()

    input_file, output_file, depth = args.input_file, args.output_file, args.depth
    
    try:
        with open(input_file, 'r') as f:
            board = f.readline().strip()
        board_positions = len(board)
        if board_positions != 21:
            print(f'The input board (board1.txt) has { board_positions } positions. The correct positions should be 21.')
            exit(1)
        
        output_board = MaxMin(board, depth)
        print(f'Board Position: { output_board }.')
        print(f'Positions evaluated by static estimation: { positions_evaulated }.')
        print(f'MINIMAX estimate: { minimax_estimate }.')

        with open(output_file, 'w+') as f:
            f.write(output_board)
    except FileNotFoundError as err:
        print(err)
        exit(1)

