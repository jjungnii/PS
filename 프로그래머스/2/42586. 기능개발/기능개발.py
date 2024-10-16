from collections import deque

def solution(progresses, speeds):
    answer = []
    times = []
    n = len(progresses)

    for i in range(n):
        todo = 100 - progresses[i]
        if todo % speeds[i] == 0:
            times.append(todo // speeds[i])
        else:
            times.append(todo // speeds[i] + 1)

    q = deque()
    q.append(0) 
    i = 0

    while i < n:
        cnt = 1
        time = times[i]
        i += 1
        while i < n and times[i] <= time:
            cnt += 1
            i += 1
        answer.append(cnt)

    return answer