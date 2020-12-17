def input_matrix(n):
    mat = []
    position = (0,0)
    for _ in range(n):
        mat.append(input().split())
    return mat


def output_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()


def find_B(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "B":
                return i, j


def transform(mat, dirs, B_pos):
    x = dirs[0]
    y = dirs[1]
    n = len(mat)
    while 0 <= B_pos[0] + x < n and 0 <= B_pos[1] + y < n:
        mat[B_pos[0] + x][B_pos[1] + y] = "X"
        B_pos = B_pos[0] + x, B_pos[1] + y


n = 8
mat = input_matrix(8)
position = find_B(mat)
directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

for d in directions:
    transform(mat, d, position)

print(output_matrix(mat))
