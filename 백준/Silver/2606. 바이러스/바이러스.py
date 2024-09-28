def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

V = int(input())
E = int(input())

parent = [i for i in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    union(a, b)

root = find(1)
count = sum(1 for i in range(1, V + 1) if find(i) == root) - 1

print(count)