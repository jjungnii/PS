N = int(input())

visited = [0] * (N + 1)
connected = {}

for _ in range(N - 1):
    i, j = map(int, input().split())
    if i not in connected:
        connected[i] = []
    if j not in connected:
        connected[j] = []
    connected[i].append(j)
    connected[j].append(i)


def find_children_iterative(x):
    stack = [x]

    while stack:
        parent = stack.pop()
        for child in connected[parent]:
            if visited[child] == 0:
                visited[child] = parent
                stack.append(child)


visited[1] = -1
find_children_iterative(1)

for i in range(2, N + 1):
    print(visited[i])
