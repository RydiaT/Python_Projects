from random import randint

player_symbol = ""
enemy_symbol = ""


def init_board(r, c):
    temp = []

    row_index = 0

    while row_index < r:
        column_index = 0
        temp.insert(row_index, [])
        while column_index < c:
            temp[row_index].append(" ")
            column_index += 1
        row_index += 1

    return temp


def print_board(board):
    rows = len(board)
    cols = len(board[0])
    line = "---"
    line_break = ""

    i = 0

    while i < cols:
        line_break += line
        i += 1

    text_board = ""

    row_idx = 0

    while row_idx < rows:
        col_idx = 0
        while col_idx < cols:
            text_board += "["
            text_board += board[row_idx][col_idx]
            text_board += "]"
            col_idx += 1
        text_board += "\n"
        row_idx += 1

    return text_board


def player_turn(board):
    player_input = input("What are the coords of your play? (hint: row, col)")
    if player_input == "stop":
        return False
    coords = player_input.split(",")

    x = 0
    y = 0

    # Wee, error handling!
    try:
        x = int(coords[0])
    except ValueError:
        print("Must be a number.")
        player_turn(board)
    try:
        y = int(coords[1])
    except ValueError:
        print("Must be a number.")
        player_turn(board)

    # More edge cases, ft. zero indexing grids
    if x < 1:
        x = 0
    else:
        x -= 1
    if y < 1:
        y = 0
    else:
        y -= 1

    if board[x][y] == player_symbol or board[x][y] == enemy_symbol:
        player_turn(board)

    board[x][y] = player_symbol

    return board


def opponent_turn(board):
    x = randint(0, len(board) - 1)
    y = randint(0, len(board[0]) - 1)

    if board[x][y] == player_symbol or board[x][y] == enemy_symbol:
        opponent_turn(board)
    else:
        board[x][y] = enemy_symbol

    return board


def check_win(board, check):

    # Left To Right
    i = 0
    while i < len(board):
        temp = []
        j = 0
        while j < len(board[0]):
            temp.append(board[i][j] == check)
            j += 1
        i += 1
        if temp.__contains__(False):
            continue
        else:
            return True

    # Up and Down
    j = 0
    while j < len(board[0]):
        i = 0
        temp = []
        while i < len(board):
            temp.append(board[i][j] == check)
            i += 1
        j += 1
        if temp.__contains__(False):
            continue
        else:
            return True
    # X Algorithms, Only Works for Square Boards.
    # Top Left to Bottom Right

    temp = []
    i = 0
    if len(board) == len(board[0]):
        while i < len(board):
            temp.append(board[i][i] == check)
            i += 1
        if not temp.__contains__(False):
            return True

    # Top Right to Bottom Left

    temp = []
    i = 0
    if len(board) == len(board[0]):
        while i < len(board):
            temp.append(board[i][(len(board[0]) - i) - 1] == check)
            i += 1
        if not temp.__contains__(False):
            return True
    return False


def check_stalemate(board):
    i = 0

    while i < len(board):
        if board[i].__contains__(" "):
            return False
        i += 1

    return True


def run():
    global player_symbol
    global enemy_symbol
    print("Game Start")

    board = init_board(3, 3)
    player_symbol = input("What do you want to play as? ")
    enemy_symbol = input("What should the enemy play as? ")

    while True:
        proxy = player_turn(board)

        if proxy is False:
            break

        if check_stalemate(board):
            print("It's a tie!")
            break

        proxy = opponent_turn(proxy)

        print("\n" + print_board(proxy))

        board = proxy

        if check_win(board, player_symbol):
            print("You win!")
            break
        elif check_win(board, enemy_symbol):
            print("You lost!")
            break
        elif check_stalemate(board):
            print("It's a tie!")
            break
