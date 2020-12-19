def input_board():
    board = []
    for _ in range(9):
        board.append([int(elem) if elem != '.' else elem for elem in input().split()])
    return board


def is_valid(board, num, pos):
    # Check row
    for j in range(len(board[0])):
        if board[pos[0]][j] == num:  # and pos[1] != j:
            return False

    # if num in board[pos[0]]:
    #     return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num:  # and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3 * 3
    box_y = pos[0] // 3 * 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num:  # and (i,j) != pos:
                return False

    return True


def solve(board):
    pos = find_empty(board)
    if not pos:
        return True
    i, j = pos[0], pos[1]
    for num in range(1, 10):
        if is_valid(board, num, pos):
            board[i][j] = num
            if solve(board):
                return True
            board[i][j] = '.'
    return False


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(str(board[i][j]), end=" ")
        print()


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                return i, j  # row, col
    return None


def output_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()

board =  [
    ['.', 1, '.', '.', '.', '.', '.', '.', 2],
    [8, '.', '.', '.', '.', '.', '.', '.', 1],
    ['.', 4, '.', '.', '.', 3, '.', '.', '.'],
    ['.', '.', 1, '.', '.', 6, '.', '.', '.'],
    ['.', '.', 7, '.', '.', '.', 4, '.', '.'],
    ['.', '.', '.', 5, '.', '.', '.', 9, '.'],
    ['.', 9, '.', '.', '.', '.', '.', 1, '.'],
    ['.', '.', '.', 6, '.', 1, '.', '.', '.'],
    ['.', '.', 2, '.', '.', '.', 8, '.', '.'],
]

print(solve(board))
print(output_matrix(board))
