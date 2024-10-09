from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

visited = [[0] * m for _ in range(n)]	# 방문 여부 저장
dist = [[0] * m for _ in range(n)]		# 최단 거리 저장
queue = deque()

# 시작 위치 처리
queue.append((0, 0))
visited[0][0] = 1
dist[0][0] = 1

# 0: 상, 1: 우, 2: 하, 3: 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:	# 범위 체크
            if not visited[nx][ny] and arr[nx][ny] == 1: # 방문 체크, 조건 체크
                queue.append((nx, ny))
                visited[nx][ny] = True # 방문 처리
                dist[nx][ny] += dist[x][y] + 1
                
print(dist[n - 1][m - 1])