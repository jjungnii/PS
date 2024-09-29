from collections import deque

N, K = map(int, input().split())

queue = deque()
visited = [[False, 0] for _ in range(200002)] 

queue.append(N)
visited[N][0] = True 

if N == K:
    print(0)
else:
    while queue:
        x = queue.popleft()

        if x > 0 and not visited[x - 1][0]:
            queue.append(x - 1)
            visited[x - 1][0] = True
            visited[x - 1][1] = visited[x][1] + 1 

        if x < 200001 and not visited[x + 1][0]: 
            queue.append(x + 1)
            visited[x + 1][0] = True
            visited[x + 1][1] = visited[x][1] + 1 

        if 2 * x < 200001 and not visited[2 * x][0]:  
            queue.append(2 * x)
            visited[2 * x][0] = True
            visited[2 * x][1] = visited[x][1] + 1  

    print(visited[K][1]) 