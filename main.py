from textwrap import dedent

# Return the neighbors of a given position
def neighbors(location) -> list:
    if location == 0:
        return [1, 6]
    elif location == 1:
        return [0, 11]
    elif location == 2:
        return [3, 7]
    elif location == 3:
        return [2, 10]
    elif location == 4:
        return [5, 8]
    elif location == 5:
        return [4, 9]
    elif location == 6:
        return [0, 7, 18]
    elif location == 7:
        return [2, 6, 8, 15]
    elif location == 8:
        return [4, 7, 12]
    elif location == 9:
        return  [5, 10, 14]
    elif location == 10:
        return [3, 9, 11, 17]
    elif location == 11:
        return [1, 10, 20]
    elif location == 12:
        return [8, 13]
    elif location == 13:
        return [12, 14, 16]
    elif location == 14:
        return [9, 13]
    elif location == 15:
        return [7, 16]
    elif location == 16:
        return [13, 15, 17, 19]
    elif location == 17:
        return [10, 16]
    elif location == 18:
        return [6, 19]
    elif location == 19:
        return [16, 18, 20]
    elif location == 20:
        return [11, 19]
    return []

# Return True if the location closes a mill else False
def closeMill(location, board) -> bool:
    check_mill = board[location]
    if board[location] in ('W', 'B'):
        if location == 0:
            return True if board[6] == check_mill and board[18] == check_mill else False
        elif location == 1:
            return True if board[11] == check_mill and board[20] == check_mill else False
        elif location == 2:
            return True if board[7] == check_mill and board[15] == check_mill else False
        elif location == 3:
            return True if board[10] == check_mill and board[17] == check_mill else False
        elif location == 4:
            return True if board[8] == check_mill and board[12] == check_mill else False
        elif location == 5:
            return True if board[9] == check_mill and board[14] == check_mill else False
        elif location == 6:
            return True if ((board[0] == check_mill and board[18] == check_mill) or (board[7] == check_mill and board[8] == check_mill)) else False
        elif location == 7:
            return True if ((board[2] == check_mill and board[15] == check_mill) or (board[6] == check_mill and board[8] == check_mill)) else False
        elif location == 8:
            return True if ((board[4] == check_mill and board[12] == check_mill) or (board[6] == check_mill and board[7] == check_mill)) else False
        elif location == 9:
            return True if ((board[5] == check_mill and board[14] == check_mill) or (board[10] == check_mill and board[11] == check_mill)) else False
        elif location == 10:
            return True if ((board[3] == check_mill and board[17] == check_mill) or (board[9] == check_mill and board[11] == check_mill)) else False
        elif location == 11:
            return True if ((board[1] == check_mill and board[20] == check_mill) or (board[9] == check_mill and board[10] == check_mill)) else False
        elif location == 12:
            return True if ((board[4] == check_mill and board[8] == check_mill) or (board[13] == check_mill and board[14] == check_mill)) else False
        elif location == 13:
            return True if ((board[12] == check_mill and board[14] == check_mill) or (board[16] == check_mill and board[19] == check_mill)) else False
        elif location == 14:
            return True if ((board[5] == check_mill and board[9] == check_mill) or (board[12] == check_mill and board[13] == check_mill)) else False
        elif location == 15:
            return True if ((board[2] == check_mill and board[7] == check_mill) or (board[16] == check_mill and board[17] == check_mill)) else False
        elif location == 16:
            return True if ((board[13] == check_mill and board[19] == check_mill) or (board[15] == check_mill and board[17] == check_mill)) else False
        elif location == 17:
            return True if ((board[3] == check_mill and board[10] == check_mill) or (board[15] == check_mill and board[16] == check_mill)) else False
        elif location == 18:
            return True if ((board[0] == check_mill and board[6] == check_mill) or (board[19] == check_mill and board[20] == check_mill)) else False
        elif location == 19:
            return True if ((board[16] == check_mill and board[13] == check_mill) or (board[18] == check_mill and board[20] == check_mill)) else False
        elif location == 20:
            return True if ((board[1] == check_mill and board[11] == check_mill) or (board[18] == check_mill and board[19] == check_mill)) else False
        else:
            return False
    return False     

def generate_remove(board, move_list) -> list:
    no_positions_added = True
    for location, piece in enumerate(board):
        if piece == 'B':
            if not closeMill(location, board):
                temp_board = list(board)
                temp_board[location] = 'x'
                temp_board = ''.join(temp_board)
                move_list.append(temp_board)
                no_positions_added = False
    if no_positions_added:
        move_list.append(board)
    return move_list

def generate_move(board) -> list:
    move_list = list()
    for location, piece in enumerate(board):
        if piece == 'W':
            neighbors_list = neighbors(location)
            for neighbor in neighbors_list:
                if board[neighbor] == 'x':
                    temp_board = list(board)
                    temp_board[location], temp_board[neighbor] = 'x', 'W'
                    temp_board = ''.join(temp_board)
                    if closeMill(neighbor, temp_board):
                        generate_remove(temp_board, move_list)
                    else:
                        move_list.append(temp_board)
    return move_list

def generate_add(board) -> list:
    add_list = list()
    for location, piece in enumerate(board):
        if piece == 'x':
            temp_board = list(board)
            temp_board[location] = 'W'
            temp_board = ''.join(temp_board)
            if closeMill(location, temp_board):
                generate_remove(temp_board, add_list)
            else:
                add_list.append(temp_board)
    return add_list

def generate_moves_opening(board) -> str:
    return generate_add(board)

def generate_hopping(board) -> list:
    hop_list = list()
    for location_i, piece_i in enumerate(board):
        if piece_i == 'W':
            for location_j, piece_j in enumerate(board):
                if piece_j == 'x':
                    temp_board = list(board)
                    temp_board[location_i], temp_board[location_j] = 'x', 'W'
                    temp_board = ''.join(temp_board)
                    if closeMill(location_j, temp_board):
                        generate_remove(temp_board, hop_list)
                    else:
                        hop_list.append(temp_board)
    return hop_list

def generate_moves_midgame_endgame(board) -> str:
    if board.count('W') == 3:
        return generate_hopping(board)
    else:
        return generate_move(board)
    
def static_estimation_opening(board) -> int:
    white_pieces, black_pieces = board.count('W'), board.count('B')
    return white_pieces - black_pieces

def static_estimation_midgame_endgame(board) -> int:
    white_pieces, black_pieces = board.count('W'), board.count('B')
    black_moves = len(generate_moves_midgame_endgame(board))
    if black_pieces <= 2:
        return 10000
    elif white_pieces <= 2:
        return -10000
    elif black_moves == 0:
        return 10000
    else:
        return 1000 * (white_pieces - black_pieces) - black_moves

# Draw the board
def draw(board) -> None:
    print(dedent(f"""\
        {board[18]}--------{board[19]}--------{board[20]}
        |        |        |
        |  {board[15]}-----{board[16]}-----{board[17]}  |
        |  |     |     |  |
        |  |  {board[12]}--{board[13]}--{board[14]}  |  |
        |  |  |     |  |  |
        {board[6]}--{board[7]}--{board[8]}     {board[9]}--{board[10]}--{board[11]}
        |  |  |     |  |  |
        |  |  {board[4]}-----{board[5]}  |  |
        |  |           |  |
        |  {board[2]}-----------{board[3]}  |
        |                 |
        {board[0]}-----------------{board[1]}\
        """))


if __name__ == "__main__":
    board = 'WxxWxxWxxxxxxxxxxxxxx'
    print(len(generate_add(board)))
    for x in generate_remove(board):
        print(x)
    