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

if __name__ == "__main__":
    board = 'xxxxWWWxBxxxWxxBxWxBB'
    draw(board)