H, W = map(int, input().split())
board = [[0] * W for _ in range(H)]
numbers = []

for i in range(H):
    string = input()
    for j in range(W):
        if string[j] == 'W':
            board[i][j] = 1

for i in range(H - 8 + 1):
    for j in range(W - 8 + 1):
        for k in range(2):
            number = 0
            for l in range(i, i + 8):
                for m in range(j, j + 8):
                    if board[l][m] != (l + m + k) % 2:
                        number += 1
            numbers.append(number)

print(min(numbers))