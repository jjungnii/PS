from collections import deque

def solution(priorities, location):
    q = deque((i,p) for i,p in enumerate(priorities))
    answer = 0
    while True:
        curr = q.popleft()
        if any(curr[1] < process[1] for process in q):
            q.append(curr)
        else:
            answer += 1
            if curr[0] == location:
                return answer