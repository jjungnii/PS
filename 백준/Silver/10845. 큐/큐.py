from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])