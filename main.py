from textwrap import dedent

# Draw the board
def draw(board):
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

# Return the neighbors of a given position
def neighbors(location):
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
    else:
        return []

# Return True if the location closes a mill else False
def closeMill(location, board):
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

if __name__ == "__main__":
    board = 'xxxxWWWxBxxxWxxBxWxBB'
    draw(board)
    