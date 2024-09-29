from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
cnt = [0, 0]

queue.append(((0, 0), N))

while queue:
    loc, length = queue.popleft()
    y, x = loc[0], loc[1]

    color = sum(sum(row[x:x + length]) for row in board[y:y + length])

    if color == 0:
        cnt[0] += 1
    elif color == length ** 2:
        cnt[1] += 1
    elif length > 1:
        new_length = length // 2
        queue.append(((y, x), new_length))
        queue.append(((y, x + new_length), new_length))
        queue.append(((y + new_length, x), new_length))
        queue.append(((y + new_length, x + new_length), new_length))

print(cnt[0])
print(cnt[1])