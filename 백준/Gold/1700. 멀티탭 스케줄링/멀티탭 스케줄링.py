import sys
from collections import Counter
input = sys.stdin.readline

n, k = map(int, input().split())
order = list(map(int, input().split()))
multitab = set()
counter = Counter(order)
res = 0

for i, x in enumerate(order):
    counter[x] -= 1
    if x not in multitab:
        if len(multitab) >= n:
            for a in multitab:
                if counter[a] == 0:
                    multitab.remove(a)
                    res += 1
                    break
            else:
                t = set()
                for j in range(i, k):
                    if order[j] in multitab:
                        t.add(order[j])
                    if len(t) == n:
                        multitab.remove(order[j])
                        break
                res += 1
    multitab.add(x)
print(res)