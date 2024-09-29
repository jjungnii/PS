import heapq

N = int(input())
original = list(map(int, input().split()))
heap = list(set(original))
changed = {}
result = []

heapq.heapify(heap)
curr = 0
while len(heap):
    val = heapq.heappop(heap)
    changed[val] = curr
    curr += 1

for num in original:
    result.append(changed[num])

print(*result)