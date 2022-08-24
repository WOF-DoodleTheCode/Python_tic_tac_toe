import copy


def check_winner(marker, board):
    if is_row_same(marker, board):
        return True
    if is_col_same(marker, board):
        return True
    if is_diagonal_same(marker, board):
        return True
    return False


def is_row_same(marker, board):
    for i in range(len(board)):
        flag = True
        for j in range(len(board[i])):
            if board[i][j] != marker:
                flag = False
                break
        if flag == True:
            return True
    return False


def is_diagonal_same(marker, board):
    isPDiagSame = board[0][0] == board[1][1] == board[2][2] == marker
    isSDiagSame = board[0][2] == board[1][1] == board[2][0] == marker
    return isPDiagSame or isSDiagSame


def is_col_same(marker, board):
    rotated_board = rotate(board)
    return is_row_same(marker, rotated_board)


def rotate(board):
    new_board = copy.deepcopy(board)

    for i in range(len(new_board)):
        new_board[i].reverse()

    for i in range(len(new_board)):
        for j in range(i, len(new_board)):
            temp = new_board[i][j]
            new_board[i][j] = new_board[j][i]
            new_board[j][i] = temp
    return new_board


def get_valid_markers():
    player_1_marker = None
    player_2_marker = None
    valid_markers = ['X', '0']

    while player_1_marker not in valid_markers:
        player_1_marker = input('Player 1 select X / 0 :- ')

    player_2_marker = valid_markers[1 - valid_markers.index(player_1_marker)]

    return [player_1_marker, player_2_marker]


def is_empty_place(row_index, col_index, board):
    if row_index is None or col_index is None:
        return False
    elif board[int(row_index)][int(col_index)] != '':
        return False
    else:
        return True


def get_valid_index(players_marker, player_no, board):
    valid_indexes = ['0', '1', '2']
    row_index = None
    col_index = None

    while is_empty_place(row_index, col_index, board) == False:
        if not (is_empty_place(row_index, col_index, board)):
            if col_index != None and row_index != None:
                print('Select some other index. place not empty')

        row_index = None
        col_index = None

        row_index = get_valid_row_index(player_no, players_marker, row_index, valid_indexes)

        col_index = get_valid_col_index(col_index, player_no, players_marker, valid_indexes)

    return [int(row_index), int(col_index)]


def get_valid_col_index(col_index, player_no, players_marker, valid_indexes):
    while col_index not in valid_indexes:
        col_index = input('{} which column want to put your {} :- '.format(player_no, players_marker))
        if col_index not in valid_indexes:
            print('Enter index 0, 1, 2 only')
    return col_index


def get_valid_row_index(player_no, players_marker, row_index, valid_indexes):
    while row_index not in valid_indexes:
        row_index = input('{} which row want to put your {} :- '.format(player_no, players_marker))
        if row_index not in valid_indexes:
            print('Enter index 0, 1, 2 only')
    return row_index


def print_board(board):
    for i in range(len(board)):
        print(board[i])


def is_board_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == ''):
                return True
    return False


def start_game():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    [player_1_marker, player_2_marker] = get_valid_markers()

    while True:
        print_board(board)

        [player_1_row, player_1_column] = get_valid_index(player_1_marker, 'Player 1', board)
        board[player_1_row][player_1_column] = player_1_marker
        if check_winner(player_1_marker, board):
            print('player 1 wins')
            print_board(board)
            break

        if not (is_board_empty(board)):
            print('Its a draw')
            break

        print_board(board)
        [player_2_row, player_2_column] = get_valid_index(player_2_marker, 'Player 2', board)
        board[player_2_row][player_2_column] = player_2_marker
        if check_winner(player_2_marker, board):
            print('player 2 wins')
            print_board(board)
            break

        if not (is_board_empty(board)):
            print('Its a draw')
            break


if __name__ == '__main__':
    start_game()
