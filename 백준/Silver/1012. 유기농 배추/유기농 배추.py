from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    def bfs(i, j):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited[i][j] = True
        queue = deque()
        queue.append((i, j))
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny >= 0 and ny < N and nx >= 0 and nx < M:
                    if not visited[ny][nx] and board[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append((ny, nx))

    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] == 1:
               bfs(i, j)
               cnt += 1

    print(cnt)