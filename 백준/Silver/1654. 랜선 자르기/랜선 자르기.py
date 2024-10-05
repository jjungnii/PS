import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

s = 1
e = max(lines)

while s <= e:
    mid = s + (e - s) // 2
    num = 0

    for line in lines:
        num += line // mid

    if num >= N:
        s = mid + 1
    else:
        e = mid - 1

print(e)