from collections import deque

N = int(input())
queue = deque()

for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    if len(queue) == 1:
        break
    top = queue.popleft()
    queue.append(top)

print(queue.popleft())