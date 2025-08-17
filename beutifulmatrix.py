# codeforces 263A - Beautiful Matrix
matrix = [list(map(int, input().split())) for _ in range(5)]
# find the position of '1'
for i  in range(5):
    for j in range(5):
        if matrix [i][j] == 1:
            x, y = i, j
            break
# calculate the number of moves to center (2, 2)
moves = abs(x - 2) + abs(y - 2)
print(moves)