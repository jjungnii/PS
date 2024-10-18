from collections import deque

def check(a, b):
    n = len(a)
    different = 0
    for i in range(n):
        if a[i] != b[i]:
            if different:
                return False
            different = 1
    if different:
        return True
    return False

def solution(begin, target, words):
    answer = 0
    dists = []
    n = len(words)
    
    wordset = set(words)
    if target not in wordset:
        return answer
    
    q = deque()
    v = [0] * n
    q.append((begin, 0))
    
    while q:
        curr, time = q.popleft()
        for i, word in enumerate(words):
            if not v[i]:
                if check(curr, word):
                    if word == target:
                        dists.append(time + 1)
                        break
                    q.append((word, time + 1))
                    v[i] = 1
    if dists:
        answer = min(dists)
    
    return answer