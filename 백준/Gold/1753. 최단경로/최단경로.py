import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    dist = [float("inf")] * (V + 1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (dist[start], start))

    while queue:
        min_dist, node = heapq.heappop(queue)

        if dist[node] < min_dist:
            continue

        for neighbor, min_dist in graph[node]:
            curr_dist = dist[node] + min_dist
            if curr_dist < dist[neighbor]:
                dist[neighbor] = curr_dist
                heapq.heappush(queue, (curr_dist, neighbor))

    return dist

result = dijkstra(start)
for i in range(1, len(result)):
    print("INF" if result[i] == float("inf") else result[i])