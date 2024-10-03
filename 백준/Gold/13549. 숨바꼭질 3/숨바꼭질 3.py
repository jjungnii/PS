from collections import deque

def bfs(N, K):
    MAX = 100001
    visited = [-1] * MAX
    queue = deque([N])
    visited[N] = 0

    while queue:
        x = queue.popleft()

        if x == K:
            return visited[x]

        if 2 * x < MAX and visited[2 * x] == -1:
            visited[2 * x] = visited[x]
            queue.appendleft(2 * x)

        if x - 1 >= 0 and visited[x - 1] == -1:
            visited[x - 1] = visited[x] + 1
            queue.append(x - 1)

        if x + 1 < MAX and visited[x + 1] == -1:
            visited[x + 1] = visited[x] + 1
            queue.append(x + 1)

N, K = map(int, input().split())
print(bfs(N, K))